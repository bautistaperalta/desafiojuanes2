from django.db import models

class Datos_personales(models.Model):
    usuario = models.CharField(max_length=40)
    contraseña = models.IntegerField()

class Datos_registro(models.Model):
    nombre_completo = models.CharField(max_length=40)
    email = models.EmailField()
    fechaDeNacimiento = models.DateField()
    contraseña = models.IntegerField()


    