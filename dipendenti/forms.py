from django import forms
from .models import Dipendenti

class AddDipendenti(forms.ModelForm):

    class Meta:
        model = Dipendenti
        fields = '__all__'