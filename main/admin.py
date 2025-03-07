from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone_number", "university", "major", "city", "is_aiesecer", "how_did_you_hear","promo")
    search_fields = ("full_name", "email", "university", "city")
    list_filter = ("university", "major", "city", "is_aiesecer", "how_did_you_hear")
    ordering = ("full_name",)
