from django import forms


class NuevoUsuarioFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()  
    NickName = forms.CharField()  
    password = forms.CharField()  
    email = forms.EmailField()
    profesion_trabajo = forms.CharField()  

class NuevoProyectoFormulario(forms.Form):
    NickName= forms.CharField()
    nombre_proyecto = forms.CharField()
    breve_descripcion = forms.CharField()

class NuevaConsultaFormulario(forms.Form):
    titulo_consulta = forms.CharField()  # PK
    consulta = forms.CharField() 

class BuscaProyectoFormulario(forms.Form):
    autor_proyecto = forms.CharField(max_length=51)  # Podrías agregar opciones para seleccionar
    nombre_proyecto = forms.CharField(max_length=51)

