from django.urls import path
from .views import home, thankyou
from . import views

urlpatterns = [
    path("", home, name="home"),
    path('thankyou.html/', views.thankyou, name='thankyou'),
]
