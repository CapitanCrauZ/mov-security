from django.shortcuts import render,redirect
from .forms import FormProducto
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import Productos
from django.http import HttpResponse

# Create your views here.


def agregarProducto(request):
    formProd = FormProducto()
    if request.method == 'POST':
        formProd = FormProducto(request.POST)
        if formProd.is_valid():
            formProd.save()
            messages.add_message(request, messages.INFO, 'Producto Agregado Correctamente....')
            return redirect('/productos/agregarProducto/')
    context = {
        'formProd': formProd,
    }
    return render(
        request,
        'productoMongo/agregarProducto.html',
        context
    )

def modificarProducto(request,id):
    productoEncontrado = Productos.objects.get(pk = id)
    formProd = FormProducto(instance=productoEncontrado)
    if request.method == 'POST':
        formProd = FormProducto(request.POST, instance=productoEncontrado)
        if formProd.is_valid():
            formProd.save()
            messages.add_message(request, messages.INFO, 'Producto Modificado Correctamente....')
            return redirect ('/productos/listarProducto/')
    context = {
        'formProd':formProd
    }
    return render(
        request,
        'productoMongo/modificarProducto.html',
        context
    )

def eliminarProducto(request,id):
    productoEncontrado = Productos.objects.get(pk = id)
    productoEncontrado.delete()
    messages.add_message(request, messages.INFO, 'Producto Eliminado Correctamente....')
    return redirect('/productos/listarProducto/') 



def listarProducto(request):
    productos = Productos.objects.all()
    context = {
        'productos':productos
    }
    return render(
        request,
        'productoMongo/listarProducto.html',
        context   
    )





