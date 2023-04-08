from django.db import models

# Create your models here.

class Autos(models.Model):
    modelo= models.CharField(max_length=20)
    año= models.IntegerField()
    kilometros= models.IntegerField()
    descripcion= models.CharField(max_length=250)
    precio= models.IntegerField()

    def __str__(self):
        return self.modelo

class Alquiler(models.Model):
    modelo= models.CharField(max_length=20)
    año= models.IntegerField()
    descripcion= models.CharField(max_length=250)
    precio= models.IntegerField()

    def __str__(self):
        return self.modelo

class Asesoramiento(models.Model):
    nombre= models.CharField(max_length=20)
    telefono= models.IntegerField()
    dataAsesoramiento= models.CharField(max_length=250)
    modeloAuto= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

