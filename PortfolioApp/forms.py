from django.forms import ModelForm
from .models import *
from django import forms



class ContactForm(ModelForm):
    class Meta:
        model = ContactMoi
        fields = ["Full_name", "email", "number", "sujet", "messages"]
        widgets = {
            'Full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'sujet': forms.TextInput(attrs={'class': 'form-control'}),
            'messages': forms.Textarea(attrs={'class': 'form-control'}),
            'date_publication': forms.DateInput(attrs={'class': 'form-control'}),
            "number": forms.NumberInput(attrs={'class': 'form-control'}),
        }


