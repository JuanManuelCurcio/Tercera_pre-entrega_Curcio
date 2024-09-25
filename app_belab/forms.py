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
    breve_descripcion = forms.CharField(widget=forms.Textarea)

class NuevaConsultaFormulario(forms.Form):
    NickName= forms.CharField()
    titulo_consulta = forms.CharField()
    consulta = forms.CharField(widget=forms.Textarea) 

class BuscaProyectoFormulario(forms.Form):
    NickName = forms.CharField(max_length=51)  # Podrías agregar opciones para seleccionar
    nombre_proyecto = forms.CharField(max_length=51)

