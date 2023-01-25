from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def accueil(request):
    return render(request, "accueil.html")

def actualite(request):
    return render(request, "actualité.html")

def connexion(request):
    return render(request, "connexion.html")

def demarrage(request):
    return render(request, "demarrage.html")

def inscription(request):
    return render(request, "inscription.html")

def messagerie(request):
    return render(request, "messagerie.html")

def profilAnimal(request):
    return render(request, "profilAnimal.html")

def profilUtilisateur(request):
    return render(request, "profilUtilisateur.html")

def recherche(request):
    return render(request, "recherche.html")