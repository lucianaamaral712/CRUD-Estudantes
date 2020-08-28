from django import forms
from .models import Studant
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class StudantForm(forms.ModelForm):
    class Meta:
        model = Studant
        fields = '__all__'

        widgets = {
                'birth_date': forms.TextInput(attrs={'type': 'date'}),
            }