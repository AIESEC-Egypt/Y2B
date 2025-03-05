from django import forms
from .models import Registration

UNIVERSITIES = [
    ("Ain Shams University", "Ain Shams University"),
    ("Alexandria University", "Alexandria University"),
    ("Al-Azhar University", "Al-Azhar University"),
    ("AUC", "AUC"),
    ("AAST Aswan", "AAST Aswan"),
    ("AAST Port Said", "AAST Port Said"),
    ("AAST in Alexandria", "AAST in Alexandria"),
    ("AAST in Cairo University", "AAST in Cairo University"),
    ("Assiut University", "Assiut University"),
    ("Badr University in Cairo", "Badr University in Cairo"),
    ("Benha University", "Benha University"),
    ("Beni Suef University", "Beni Suef University"),
    ("BUE", "BUE"),
    ("Cairo University", "Cairo University"),
    ("Chinese University in Egypt", "Chinese University in Egypt"),
    ("Coventry University Egypt", "Coventry University Egypt"),
    ("Delta University for Science and Technology", "Delta University for Science and Technology"),
    ("Delta Academy", "Delta Academy"),
    ("Damietta University", "Damietta University"),
    ("Egyptian Russian University", "Egyptian Russian University"),
    ("Egyptian Aviation Academy", "Egyptian Aviation Academy"),
    ("ESLSCA University Egypt", "ESLSCA University Egypt"),
    ("Fayoum University", "Fayoum University"),
    ("FUE", "FUE"),
    ("Galala University", "Galala University"),
    ("GUC", "GUC"),
    ("Helwan University", "Helwan University"),
    ("Heliopolis University for Sustainable Development", "Heliopolis University for Sustainable Development"),
    ("Mansoura University", "Mansoura University"),
    ("MIU", "MIU"),
    ("MUST", "MUST"),
    ("New Giza University", "New Giza University"),
    ("Nile University", "Nile University"),
    ("Pharos University in Alexandria", "Pharos University in Alexandria"),
    ("Suez Canal University", "Suez Canal University"),
    ("Zagazig University", "Zagazig University"),
]

MAJORS = [
    ("Accounting", "Accounting"),
    ("Actuarial Science", "Actuarial Science"),
    ("Advertising", "Advertising"),
    ("Aerospace Engineering", "Aerospace Engineering"),
    ("Agricultural Engineering", "Agricultural Engineering"),
    ("Anthropology", "Anthropology"),
    ("Applied Arts", "Applied Arts"),
    ("Architecture", "Architecture"),
    ("Artificial Intelligence", "Artificial Intelligence"),
    ("Automotive Engineering", "Automotive Engineering"),
    ("Banking & Finance", "Banking & Finance"),
    ("Biochemistry", "Biochemistry"),
    ("Biotechnology", "Biotechnology"),
    ("Biomedical Engineering", "Biomedical Engineering"),
    ("Business Administration", "Business Administration"),
    ("Chemical Engineering", "Chemical Engineering"),
    ("Civil Engineering", "Civil Engineering"),
    ("Computer Science", "Computer Science"),
    ("Dentistry", "Dentistry"),
    ("Economics", "Economics"),
    ("Education", "Education"),
    ("Electrical Engineering", "Electrical Engineering"),
    ("Finance", "Finance"),
    ("Human Resource Management", "Human Resource Management"),
    ("Industrial Engineering", "Industrial Engineering"),
    ("Marketing", "Marketing"),
    ("Mathematics", "Mathematics"),
    ("Mechanical Engineering", "Mechanical Engineering"),
    ("Medicine", "Medicine"),
    ("Pharmacy", "Pharmacy"),
    ("Political Science", "Political Science"),
    ("Psychology", "Psychology"),
    ("Software Engineering", "Software Engineering"),
]

CITIES = [
    ("Alexandria", "Alexandria"),
    ("Aswan", "Aswan"),
    ("Asyut", "Asyut"),
    ("Beheira", "Beheira"),
    ("Beni Suef", "Beni Suef"),
    ("Cairo", "Cairo"),
    ("Dakahlia", "Dakahlia"),
    ("Damietta", "Damietta"),
    ("Giza", "Giza"),
    ("Ismailia", "Ismailia"),
    ("Mansoura", "Mansoura"),
    ("Minya", "Minya"),
    ("Suez", "Suez"),
]

class RegistrationForm(forms.ModelForm):
    university = forms.ChoiceField(choices=UNIVERSITIES)
    major = forms.ChoiceField(choices=MAJORS)
    city = forms.ChoiceField(choices=CITIES)

    class Meta:
        model = Registration
        fields = '__all__'
