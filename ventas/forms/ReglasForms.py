from django import forms
from ventas.models import Reglas

class ReglasForm(forms.ModelForm):
    class Meta:
        model = Reglas
        fields = '__all__'