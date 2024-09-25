from django.urls import path
from .views import main, inicio, NuevoUsuario  # Asegúrate de que esta línea sea correcta

urlpatterns = [
    path("main/", main, name="main"),
    path("inicio/", inicio, name="inicio"),  # Usar el nombre como string
    path("nuevo_usuario",NuevoUsuario, name = "NuevoUsuario")
]