from django.db import models

# Create your models here.

class Productos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=45, blank=False)
    descripcion = models.TextField(max_length=500, blank=False)
    cantidad = models.IntegerField(blank=False)