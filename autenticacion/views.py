from django.shortcuts import render

# Algorisoft.
#from django.contrib.auth.views import LoginView

# Create your views here.

def autenticacion (request):
    
#    return render(request, "registro/base_login.html")
    return render(request, "registro/registro.html")


# Algorisoft.
#class   LoginFormView(LoginView):
#   template_name='base_login.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        return context