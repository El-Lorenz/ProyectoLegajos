from django.shortcuts import render, HttpResponse

# Create your views here.

def home (request):
    return render(request, "ProyectoLegajosApp/home.html")

def candidato (request):
    return render(request, "ProyectoLegajosApp/candidato.html")

def contacto (request):
    return render(request, "ProyectoLegajosApp/contacto.html")