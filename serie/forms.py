from django import forms
from django.forms import fields
from .models import Serie

class SerieForm(forms.ModelForm):

    class Meta:
        model=Serie
        fields='__all__'