from django import forms


class NuevoUsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=51)
    apellido = forms.CharField(max_length=51)
    edad = forms.IntegerField(required=True)  
    usuario_id = forms.CharField(max_length=18)  
    password = forms.CharField(max_length=18)  
    email = forms.EmailField(max_length=200)
    profesion_trabajo = forms.CharField(max_length=51)  

class NuevoProyectoFormulario(forms.Form):
    proyecto_id = forms.CharField(max_length=51)  
    nombre_proyecto = forms.CharField(max_length=51)
    breve_descripcion = forms.CharField(max_length=1250)

class NuevaConsultaFormulario(forms.Form):
    consulta_id = forms.CharField(max_length=18)  # PK
    consulta = forms.CharField(max_length=5000) 

class BuscaProyectoFormulario(forms.Form):
    autor_proyecto = forms.CharField(max_length=51)  # Podrías agregar opciones para seleccionar
    nombre_proyecto = forms.CharField(max_length=51)

