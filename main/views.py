from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Registration
from .forms import RegistrationForm

def home(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to the database
            return redirect("/thankyou.html")  # ✅ Redirects to "https://youth2business.aiesec.org.eg/thankyou.html"
    else:
        form = RegistrationForm()

    return render(request, "registration.html", {"form": form})


def thankyou(request):
    return redirect("thankyou.html")