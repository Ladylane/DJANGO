from django import forms
#from django.forms import fields
from genero.models import Genero

class GeneroForm(forms.ModelForm):

    class Meta:
        model=Genero
        fields='__all__'

