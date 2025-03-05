from django.shortcuts import render, redirect
from .models import Registration

def home(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name", "")
        age = request.POST.get("age", None)
        phone_number = request.POST.get("phone_number", "")
        email = request.POST.get("email", "")
        university = request.POST.get("university", "")
        major = request.POST.get("major", "")
        city = request.POST.get("city", "")
        is_aiesecer = request.POST.get("is_aiesecer", "")
        topics_interested = request.POST.get("topics_interested", "")
        how_did_you_hear = request.POST.get("how_did_you_hear", "")

        # Save to database
        Registration.objects.create(
            full_name=full_name,
            age=age if age else None,
            phone_number=phone_number,
            email=email,
            university=university,
            major=major,
            city=city,
            is_aiesecer=is_aiesecer,
            topics_interested=topics_interested,
            how_did_you_hear=how_did_you_hear
        )

        return redirect("home")  # Refresh the page after submission to prevent duplicate entries

    return render(request, "registration.html")
