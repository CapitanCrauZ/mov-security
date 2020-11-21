from djongo import models

# Create your models here.

class Productos(models.Model):
    nombre= models.CharField(max_length=45, blank=False)
    descripcion = models.CharField(max_length=45, blank=False)
    cantidad = models.IntegerField(blank=False)