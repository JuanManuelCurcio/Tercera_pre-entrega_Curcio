from django.shortcuts import render
from .forms import NuevoUsuarioFormulario, NuevoProyectoFormulario, NuevaConsultaFormulario
from .models import Usuario, Proyectos, Consulta

def main(req):
    return render(req, "main.html", {})

def inicio(req):
    return render(req, "inicio.html", {})

def proyecto_boton(req):
    return render(req, "proyectos.html", {})

def busqueda_proyecto(req):
    return render(req, "busqueda_proyecto.html")

def resultado_proyecto(req):
    nombre_proyecto = req.GET["nombre_proyecto"]
    proyectos = Proyectos.objects.filter(nombre_proyecto__icontains=nombre_proyecto)
    return render(req, "resultado_proyecto.html", {"proyectos": proyectos, "nombre_proyecto": nombre_proyecto})

def belab_tools(req):
    return render(req, "belab_tools.html")


def NuevoUsuario(req):
    if req.method == 'POST':
        form_nuevo_usuario = NuevoUsuarioFormulario(req.POST)

        if form_nuevo_usuario.is_valid():  
            nuevo_usuario = Usuario(
                nombre=form_nuevo_usuario.cleaned_data['nombre'],
                apellido=form_nuevo_usuario.cleaned_data['apellido'],
                edad=form_nuevo_usuario.cleaned_data['edad'],
                NickName=form_nuevo_usuario.cleaned_data['NickName'],
                password=form_nuevo_usuario.cleaned_data['password'],
                email=form_nuevo_usuario.cleaned_data['email'],
                profesion_trabajo=form_nuevo_usuario.cleaned_data['profesion_trabajo'],
            )
            nuevo_usuario.save()  
            return render(req, "usuario_creado.html", {})  
    else:
        form_nuevo_usuario = NuevoUsuarioFormulario()  

    return render(req, "nuevo_usuario.html", {"form_nuevo_usuario": form_nuevo_usuario})

def NuevoProyecto(req):
    if req.method == 'POST':
        form_nuevo_proyecto = NuevoProyectoFormulario(req.POST)

        if form_nuevo_proyecto.is_valid():  
            nuevo_proyecto = Proyectos(
                    NickName= form_nuevo_proyecto.cleaned_data["NickName"],
                    nombre_proyecto = form_nuevo_proyecto.cleaned_data["nombre_proyecto"],
                    breve_descripcion = form_nuevo_proyecto.cleaned_data["breve_descripcion"],
            )
            nuevo_proyecto.save()  
            return render(req, "proyecto_creado.html", {})  
    else:
        form_nuevo_proyecto = NuevoProyectoFormulario()  

    return render(req, "nuevo_proyecto.html", {"form_nuevo_proyecto": form_nuevo_proyecto})

def NuevaConsulta(req):
    if req.method == 'POST':
        form_nueva_consulta = NuevaConsultaFormulario(req.POST)

        if form_nueva_consulta.is_valid():  
            nueva_consulta = Consulta(
                    NickName= form_nueva_consulta.cleaned_data["NickName"],
                    titulo_consulta = form_nueva_consulta.cleaned_data["titulo_consulta"],
                    consulta = form_nueva_consulta.cleaned_data["consulta"],
            )
            nueva_consulta.save()  
            return render(req, "consulta_creada.html", {})  
    else:
        form_nueva_consulta = NuevaConsultaFormulario()  

    return render(req, "nueva_consulta.html", {"form_nueva_consulta": form_nueva_consulta})