from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TipoUsuario(models.Model):
    detalleUsuario = models.CharField(max_length=45, blank=False)
    
    def __str__(self):
        return self.detalleUsuario

class PerfilUsuario(models.Model):
    tipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    