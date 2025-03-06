from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            "full_name", "age", "phone_number", "email", "university",
            "major", "city", "is_aiesecer", "topics_interested", "how_did_you_hear"
        ]

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age and age < 0:
            raise forms.ValidationError("Age cannot be negative.")
        return age

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Registration.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
