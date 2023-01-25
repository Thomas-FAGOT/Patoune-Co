"""patouneCo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.defaults import server_error

from patouneCo.views import accueil, actualite, connexion, demarrage, inscription, messagerie, profilAnimal, profilUtilisateur, recherche

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accueil, name="accueil"),
    path('Actualité/', actualite, name="actualite"),
    path('Connexion/', connexion, name="connexion"),
    path('Demarrage/', demarrage, name="demarrage"),
    path('Inscription/', inscription, name="inscription"),
    path('Messagerie/', messagerie, name="messagerie"),
    path('ProfilAnimal/', profilAnimal, name="profilAnimal"),
    path('ProfilUtilisateur/', profilUtilisateur, name="profilUtilisateur"),
    path('Recherche/', recherche, name="recherche"),
]
