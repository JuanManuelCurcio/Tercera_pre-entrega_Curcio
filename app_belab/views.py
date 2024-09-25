from django.shortcuts import render
from .forms import NuevoUsuarioFormulario, NuevoProyectoFormulario
from .models import Usuario, Proyectos, Consulta

def main(req):
    return render(req, "main.html", {})

def inicio(req):
    return render(req, "inicio.html", {})


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