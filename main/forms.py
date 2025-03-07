from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            "full_name", "age", "phone_number", "email", "university",
            "major", "city", "is_aiesecer", "topics_interested", "how_did_you_hear","promo"
        ]
