from django.shortcuts import render
from .models import Cliente,Proyecto,Tecnologia

# Create your views here.

def home_view(request):
    # el context es un diccionario de python
    #Son los datos dinamicos que se le mandaran al html
    lista_proyecto = Proyecto.objects.all()
    contexto = {
       'proyectos': lista_proyecto
    }

    #render() toma la peticion, y envia los datos en este caso contexto para que se puedan ver.
    return render(request,'home.html',contexto)

def crear_cliente(request):
    return render (request,'clientes')