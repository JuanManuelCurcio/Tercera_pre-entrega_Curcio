from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=51, null=False)
    apellido = models.CharField(max_length=51, null=False)
    edad = models.IntegerField(null=False)  
    usuario_id = models.CharField(max_length=18, null=False, required=True)  # PK
    password = models.CharField(max_length=128, null=False) 
    email = models.EmailField(max_length=200, null=False, required=True) 
    profesion_trabajo = models.CharField(max_length=51, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Proyectos(models.Model):
    proyecto_id = models.CharField(max_length=18, null=False, required=True)  # PK
    breve_descripcion = models.CharField(max_length=1250, null=False)
    test = models.CharField(max_length=1250, null=True) # no se si iria la idea es que vaya a al test para contestar
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # FK con Usuario

    def __str__(self):
        return self.breve_descripcion
