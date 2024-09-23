from django.urls import path, include
from django.http import HttpResponse


# Uma função simples para a página inicial
def home(request):
    return HttpResponse("Bem-vindo à API!")

urlpatterns = [
    path('users/', include('users.urls')),
    path('', home),

    # path("__reload__/", include("django_browser_reload.urls")), Se a gente quiser que ao acessar o django pela browser exiba os metodos GET, PUT, DELETE, POST...
]
