from django.http import JsonResponse
from django.shortcuts import render
from .models import Registration
from .forms import RegistrationForm

def home(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})  # ✅ Return success response (no redirect)
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)

    form = RegistrationForm()
    return render(request, "registration.html", {"form": form})
