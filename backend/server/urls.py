from django.urls import path, include
from django.http import HttpResponse

# Uma função simples para a página inicial
def home(request):
    return HttpResponse("Bem-vindo à API!")

urlpatterns = [
    path('users/', include('users.urls')),
]
