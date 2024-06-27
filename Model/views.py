from django.contrib.auth.views import LoginView


# Create your views here
class Connexion(LoginView):
    template_name = 'connexion.html'