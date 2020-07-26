from django import forms
from main.models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model =Patient
        fields='__all__'


class FooterForm(forms.Form):
    f_email=forms.EmailField()