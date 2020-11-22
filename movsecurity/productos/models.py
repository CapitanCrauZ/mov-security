from djongo import models

# Create your models here.

class Productos(models.Model):
    id = models.ObjectIdField()
    nombre= models.CharField(max_length=45, blank=False)
    descripcion = models.TextField(max_length=500, blank=False)
    cantidad = models.IntegerField(blank=False)