from django.urls import path
from .views import registro, iniciarSesion, salir, perfil, camaras, grabaciones, interfazrec, menu, modificar, listar, listarmov
#
urlpatterns = [
    path('registro/', registro, name='registro'),
    path('', iniciarSesion, name='iniciarSesion'),
    path('salir/', salir, name='salir'),
    path('perfil/', perfil, name='perfil'),
    path('camaras/', camaras, name='camaras'),
    path('grabaciones/', grabaciones, name='grabaciones'),
    path('interfazrec/', interfazrec, name='interfazrec'),
    path('menu/', menu, name='menu'),
    path('modificar/', modificar, name='modificar'),
    path('listar/', listar, name='listar'),
    path('listarMovimiento/', listarmov, name='listarMovimiento'),

]
