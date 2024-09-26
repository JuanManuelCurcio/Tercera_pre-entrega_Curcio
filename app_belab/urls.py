from django.urls import path
from .views import main, inicio, NuevoUsuario, NuevoProyecto, NuevaConsulta, proyecto_boton, busqueda_proyecto, resultado_proyecto  
from .views import belab_tools
urlpatterns = [
    path("main/", main, name="main"),
    path("inicio/", inicio, name="inicio"),
    path("nuevo_usuario/",NuevoUsuario, name = "NuevoUsuario"),
    path("nuevo_proyecto/",NuevoProyecto, name = "NuevoProyecto"),
    path("nueva_consulta/",NuevaConsulta, name = "NuevaConsulta"),
    path("proyecto_boton/", proyecto_boton, name = "proyecto_boton"),
    path("busqueda_proyecto/", busqueda_proyecto, name = "busqueda_proyecto"),
    path("resultado_proyecto/", resultado_proyecto, name = "resultado_proyecto"),
    path("belab_tools/",belab_tools, name="belab_tools"),
    path("", inicio, name="inicio") # Como no hay nada, viene de urls.app de la carpeta proyecto http://127.0.0.1:8000/app_coder/ FUNCIONA
]