from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PerfilUsuario

class FormCreacionUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',            
            'password1',
            'password2',
            'email',
        )

class FormCreacionPerfil(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ('tipoUsuario', )


