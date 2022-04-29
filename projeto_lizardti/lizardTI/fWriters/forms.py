from django import forms
from .models import Postagem, Inscricao


class PostagemForms(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = [
            'titulo',
            'texto',
            'criterio'
        ]


class InscricaoForms(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = [
            'nome',
            'email',
            'senha'
        ]
