from django.contrib import messages
from django.shortcuts import render, redirect
from PortfolioApp.forms import *
from PortfolioApp.models import *

def index(request):
    # Initialisation du formulaire
    form = ContactForm(request.POST, request.FILES)
    context = {
        "form" :form,
        "projets": Projet.objects.all(),
        "portfolios": Portfolio.objects.all()
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre message a été envoyé avec succès !')
            return redirect('index')

    return render(request, 'PortfolioApp/index.html', context)


def test(request):
    context = {
        "form": ContactForm(),
        "title": "Test Form",
    }
    return render(request, 'PortfolioApp/test.html', context)


def sms(request):
     informations = ContactMoi.objects.all()
     return render(request, 'PortfolioApp/sms.html', {'informations': informations})
