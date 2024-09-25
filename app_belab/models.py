from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=51, null=False)
    apellido = models.CharField(max_length=51, null=False)
    edad = models.IntegerField(null=False)  
    NickName = models.CharField(max_length=18, null=False)
    password = models.CharField(max_length=128, null=False) 
    email = models.EmailField(max_length=200, null=False) 
    profesion_trabajo = models.CharField(max_length=51, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Proyectos(models.Model):
    proyecto_id = models.CharField(max_length=18, null=False)
    breve_descripcion = models.CharField(max_length=1250, null=False) 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # FK con Usuario

    def __str__(self):
        return self.breve_descripcion

class Consulta(models.Model):
    usuario_id = models.CharField(max_length=18, null=False)
    consulta = models.CharField(max_length=2000, null=False)

    def __str__(self):
        return self.consulta