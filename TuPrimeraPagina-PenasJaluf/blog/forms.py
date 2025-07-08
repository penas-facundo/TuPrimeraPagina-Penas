from django import forms
from .models import Autor, Categoria, Articulo

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

class BuscarArticuloForm(forms.Form):
    titulo = forms.CharField(label='Buscar por título')