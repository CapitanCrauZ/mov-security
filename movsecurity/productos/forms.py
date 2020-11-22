from django import forms
from .models import Productos

class FormProducto(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FormProducto,self).__init__(*args, **kwargs)
        for campo in self.visible_fields():
            campo.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Productos
        fields = (
            'nombre',
            'descripcion',
            'cantidad',
        )

