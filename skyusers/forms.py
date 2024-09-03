from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['codigo', 'nome', 'ip', 'cnpj', 'qt_usuarios', 'grupo']
