from .views import home, start_payment, paymob_callback, get_registrations
from django.urls import path
from django.views.generic import TemplateView
from django.shortcuts import redirect
def static_thank_you(request):
    return redirect('/static/pages/thank-you.html')


urlpatterns = [
    path("", home, name="home"),
    path("start_payment/", start_payment, name="start_payment"),
    path("paymob_callback/", paymob_callback, name="paymob_callback"),
    path("api/registrations/", get_registrations, name="get_registrations"),  # ✅ New API endpoint
]



