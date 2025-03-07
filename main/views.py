from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Registration
from .forms import RegistrationForm
import requests
from django.conf import settings
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import json
import hmac
import hashlib
from django.utils.dateparse import parse_datetime

def home(request):
    """ Handles user registration """
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save()  # Save form data
            return redirect("start_payment")
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)

    form = RegistrationForm()
    return render(request, "registration.html", {"form": form})


def get_auth_token():
    """ Authenticate with PayMob and return auth token """
    url = "{}/auth/tokens".format(settings.PAYMOB_URL)
    payload = {"api_key": settings.PAYMOB_API_KEY}

    response = requests.post(url, json=payload)
    if response.status_code == 201:
        return response.json().get("token")
    return None


def start_payment(request):
    """ Start PayMob Payment Process using user registration details """
    
    # Retrieve the most recent user registration
    try:
        latest_registration = Registration.objects.latest('id')
    except Registration.DoesNotExist:
        return JsonResponse({"error": "No user found in the database"}, status=400)

    full_name = latest_registration.full_name.strip().split()
    first_name = full_name[0]
    last_name = full_name[-1] if len(full_name) > 1 else "N/A"

    email = latest_registration.email
    phone_number = latest_registration.phone_number

    token = get_auth_token()
    if not token:
        return JsonResponse({"error": "Failed to authenticate with PayMob"}, status=400)

    # Step 1: Create Order
    url = "{}/ecommerce/orders".format(settings.PAYMOB_URL)
    payload = {
        "auth_token": token,
        "delivery_needed": False,
        "amount_cents": "500",
        "currency": "EGP",
        "items": [],
    }

    response = requests.post(url, json=payload)
    if response.status_code != 201:
        return JsonResponse({"error": "Failed to create order"}, status=400)

    order_id = response.json().get("id")

    # Step 2: Generate Payment Key with User Data
    payment_key_url = "{}/acceptance/payment_keys".format(settings.PAYMOB_URL)
    payment_payload = {
        "auth_token": token,
        "amount_cents": "500",
        "expiration": 3600,
        "order_id": order_id,
        "currency": "EGP",
        "integration_id": settings.PAYMOB_INTEGRATION_ID,
        "billing_data": {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone_number": phone_number,
            "city": "Cairo",
            "country": "EG",
            "street": "Street Name",
            "building": "1",
            "floor": "2",
            "apartment": "3",
            "postal_code": "12345",
        },
    }

    response = requests.post(payment_key_url, json=payment_payload)
    if response.status_code != 201:
        return JsonResponse({"error": "Failed to generate payment key"}, status=400)

    payment_key = response.json().get("token")

    # Step 3: Redirect to PayMob's Payment Page
    iframe_url = "https://accept.paymob.com/api/acceptance/iframes/{}?payment_token={}".format(
        settings.PAYMOB_IFRAME_ID, payment_key
    )
    return redirect(iframe_url)


@csrf_exempt
def paymob_callback(request):
    """ Handle PayMob payment callback and verify HMAC signature """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("CALLBACK RECEIVED:", data)  # Debugging

            # Extract required fields
            order_id = data.get("order")
            transaction_id = data.get("id")
            payment_status = data.get("success")
            amount_cents = data.get("amount_cents")
            received_hmac = request.headers.get("hmac")

            # Use the correct HMAC Secret Key from settings
            secret_key = settings.PAYMOB_HMAC_SECRET
            if not secret_key:
                return JsonResponse({"error": "HMAC secret key is missing in settings"}, status=500)

            # Compute HMAC
            sorted_data = json.dumps(data, separators=(',', ':'), sort_keys=True).encode()
            calculated_hmac = hmac.new(secret_key.encode(), sorted_data, hashlib.sha512).hexdigest()

            # Validate HMAC
            if received_hmac and received_hmac != calculated_hmac:
                print("⚠️ Invalid HMAC! Expected:", calculated_hmac)
                return JsonResponse({"error": "Invalid HMAC signature"}, status=400)

            if payment_status:
                print(f"✅ Payment Successful: Order {order_id}, Amount: {amount_cents}")
                return JsonResponse({"message": "Payment confirmed"})
            else:
                print(f"❌ Payment Failed: Order {order_id}")
                return JsonResponse({"message": "Payment failed"}, status=400)

        except Exception as e:
            print("CALLBACK ERROR:", str(e))
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)


def get_registrations(request):
    """ Fetch all registrations or filter by timestamp """
    
    timestamp = request.GET.get("timestamp")  # Get timestamp from request (if provided)
    
    try:
        if timestamp:
            timestamp = parse_datetime(timestamp)
            if not timestamp:
                return JsonResponse({"error": "Invalid timestamp format"}, status=400)

            registrations = Registration.objects.filter(timestamp__gt=timestamp).order_by("timestamp")
        else:
            registrations = Registration.objects.all().order_by("-timestamp")

        data = list(registrations.values("id", "timestamp", "full_name", "email", "phone_number", 
                                         "university", "major", "city", "is_aiesecer", 
                                         "how_did_you_hear", "promo"))

        return JsonResponse({"count": len(data), "registrations": data}, safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
