from django import forms
from ventas.models import Ventas

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = '__all__'
