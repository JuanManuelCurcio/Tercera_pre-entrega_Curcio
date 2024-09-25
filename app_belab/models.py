from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=51)
    apellido = models.CharField(max_length=51)
    edad = models.IntegerField()
    NickName = models.CharField(max_length=18)  # Asegúrate de que esté aquí
    password = models.CharField(max_length=18)
    email = models.EmailField(max_length=200)
    profesion_trabajo = models.CharField(max_length=51, default="Ninguna")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Proyectos(models.Model):
    NickName= models.CharField(max_length=18, null=False) # aca deberia ser fk con usuario pero todavia no dimos como mantener el usuario logueado en la web
    nombre_proyecto = models.CharField(max_length= 500, null=False)
    breve_descripcion = models.CharField(max_length=1250, null=False) 

    def __str__(self):
        return self.breve_descripcion

class Consulta(models.Model):
    NickName= models.CharField(max_length=18) # aca deberia ser fk con usuario pero todavia no dimos como mantener el usuario logueado en la web
    titulo_consulta = models.CharField(max_length=500, null=False)
    consulta = models.CharField(max_length=2000, null=False)

    def __str__(self):
        return self.consulta