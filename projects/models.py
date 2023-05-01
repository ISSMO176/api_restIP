from django.db import models

# Create your models here.
class Project(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.CharField(max_length=3)
    dni = models.CharField(max_length=8)