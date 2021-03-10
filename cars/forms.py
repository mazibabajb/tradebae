from django import forms
from django.contrib.auth.models import User
from .models import Contact_us


class contactform(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = '__all__'
       