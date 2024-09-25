from django.shortcuts import render
from .forms import NuevoUsuarioFormulario

def main(req):
    return render(req, "main.html", {})

def inicio(req):
    return render(req, "inicio.html", {})

def NuevoUsuario(req):
    print(f'Los datos ingresados son: {req.POST}')
    if req.method == 'POST':
        form_nuevo_usuario = NuevoUsuarioFormulario(req.POST)

        if form_nuevo_usuario.is_valid(): # para ver si cumple con lo ingresaro en el modelo de formulario
            data = form_nuevo_usuario.cleaned_data   
            nuevo_usuario = NuevoUsuarioFormulario(nombre=data['nombre'], apellido=data['apellido'], edad=data['edad'],
        profesion_trabajo=data['profesion_trabajo'])
            nuevo_usuario.save() # y se guarda
            return render(req, "usuario_creado.html", {}) # para renderizar algo, pero deberia ser un nuevo html agradeciendo
    else:
        form_nuevo_usuario = NuevoUsuarioFormulario()
    return render(req, "nuevo_usuario.html", {"form_nuevo_usuario": form_nuevo_usuario})