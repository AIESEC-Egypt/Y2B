from .views import home
from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.shortcuts import redirect

def static_thank_you(request):
    return redirect('/static/pages/thank-you.html')
urlpatterns = [
    path("", home, name="home"),

    path('thank-you/', static_thank_you, name="thank-you"),
]

