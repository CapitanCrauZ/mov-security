from django.urls import path
from .views import agregarProducto,listarProducto,eliminarProducto,modificarProducto

urlpatterns = [
    path('agregarProducto/',agregarProducto, name='agregarProducto'),
    path('eliminarProducto/<int:id>',eliminarProducto, name='eliminarProducto'),
    path('modificarProducto/<int:id>',modificarProducto,name='modificarProducto'),
    path('listarProducto/',listarProducto,name='listarProducto'),

]