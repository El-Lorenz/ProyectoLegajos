from django.urls import path

from ProyectoLegajosApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('candidato', views.candidato, name="Candidato"),
    path('contacto', views.contacto, name="Contacto"),

]