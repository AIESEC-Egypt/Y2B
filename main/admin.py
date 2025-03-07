from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("formatted_timestamp", "full_name", "email", "phone_number", "university", "major", "city", "is_aiesecer", "how_did_you_hear","promo")
    search_fields = ("full_name", "email", "university", "city")
    list_filter = ("university", "major", "city", "is_aiesecer", "how_did_you_hear")
    ordering = ("-timestamp",)

    def formatted_timestamp(self, obj):
        return obj.timestamp.strftime("%Y-%m-%d %H:%M:%S")  # ✅ Show formatted date in Django Admin

    formatted_timestamp.admin_order_field = "timestamp"
    formatted_timestamp.short_description = "Timestamp"
