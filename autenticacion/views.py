from typing import Any
from django.shortcuts import render

from django.contrib.auth.views import LoginView

# Create your views here.

def autenticacion (request):
    
    return render(request, "registro/base_login.html")

# Algorisoft.
class   LoginFormView(LoginView):
    template_name='base_login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context