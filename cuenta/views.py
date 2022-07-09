from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import FormCreacionUsuario, FormCreacionPerfil
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import TipoUsuario, PerfilUsuario
from django.contrib.auth.models import User

# Create your views here.
def registro(request):
    #GET
    formulario = FormCreacionUsuario()
    formulario2 = FormCreacionPerfil()
    if request.method == 'POST':
        formulario = FormCreacionUsuario(request.POST)
        formulario2 = FormCreacionPerfil(request.POST)
        if formulario.is_valid() and formulario2.is_valid(): 
            usuario = formulario.save()
            perfil = formulario2.save(commit=False)
            perfil.usuario = usuario
            perfil.save()
            messages.add_message(request, messages.INFO, 'Registrado Correctamente....')
            return redirect('/cuenta/registro/')
    context = {
        'formulario':formulario,
        'formulario2': formulario2
    }
    return render(
        request,
        'usuario/registro.html',
        context
    )
    #POST
def iniciarSesion(request):
    #GET
    formulario = AuthenticationForm()
    if request.method == 'POST':
        formulario = AuthenticationForm(data = request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']

            usuarioLogueado = authenticate(username = username, password = password) 
            if usuarioLogueado is not None:
                login(request, usuarioLogueado)
                return redirect('perfil/')

    context = {
        'formulario':formulario
    }
    return render(
        request,
        'usuario/login.html',
        context
    )
    #POST
def salir(request):
    logout(request)
    return redirect('/cuenta/')


def perfil(request):
    if request.user.is_authenticated:
        return render(
            request,
            'usuario/perfil.html'
        )
    #return redirect('cuenta/')

def camaras(request):
    return render(
        request,
        'usuario/camaras.html'
    )

def grabaciones(request):
    return render(
        request,
        'usuario/grabaciones.html'
    )

def interfazrec(request):
    return render(
        request,
        'usuario/interfazrec.html'
    )

def modificar(request):
    return render(
        request,
        'usuario/modificarusuario.html'
    )


def listar(request):
    usuarios = User.objects.all()
    context = {
        'titulo':'Listar Usuarios',
        'usuarios':usuarios
    }
    
    return render(
        request,
        'usuario/listarUsuarios.html',
        context
    )

def listarmov(request):
    return render(
        request,
        'usuario/listarMovimiento.html'
    )



