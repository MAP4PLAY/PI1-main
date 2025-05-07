from django import forms
from .models import Quadra

class QuadraForm(forms.ModelForm):
    class Meta:
        model = Quadra
        fields = ['nome', 'endereco', 'estrutura_fisica', 'informacoes_jogos']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'estrutura_fisica': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'informacoes_jogos': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
