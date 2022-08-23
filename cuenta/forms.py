from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PerfilUsuario

class FormCreacionUsuario(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(FormCreacionUsuario,self).__init__(*args, **kwargs)
        for campo in self.visible_fields():
            campo.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'username',            
            'password1',
            'password2',
            'email',
        )

        # Una manera de ponerle form-control a los input
        #widgets = {
        #    "first_name": forms.TextInput(
        #        attrs={
        #            "class":"form-control"
        #        }
        #    )
        #}
class FormCreacionPerfil(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormCreacionPerfil,self).__init__(*args, **kwargs)
        for campo in self.visible_fields():
            campo.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = PerfilUsuario
        fields = ('tipoUsuario', )


