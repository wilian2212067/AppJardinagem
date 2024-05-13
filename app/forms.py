from django import forms
from .models import Cliente, Servico

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'