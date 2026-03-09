from django import forms
from . models import Filme, Comentario

class PostarFilmes(forms.ModelForm):

    class Meta:
        model = Filme
        fields = ('titulo','descricao', 'capa', 'categorias' )

class CometarioEpsodio(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('texto',)

