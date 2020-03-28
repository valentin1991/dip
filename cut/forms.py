from .models import ListLink
from django import forms
from django.forms import ModelForm

class Links(forms.ModelForm):
    class Meta:
        model = ListLink
        fields = ['long_link','short_link']
