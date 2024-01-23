from django.shortcuts import render, HttpResponse

# Create your views here.

def home (request):
    return HttpResponse("Home")

def candidato (request):
    return HttpResponse("Candidato")

def contacto (request):
    return HttpResponse("Contacto")