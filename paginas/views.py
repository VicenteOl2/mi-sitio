from django.shortcuts import render,redirect
from .models import Cliente,Proyecto,Tecnologia
from .forms import ProyectoForm

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

def crear_proyecto_view(request):
    if request.method == 'POST':
        formulario = ProyectoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('home')
    else:
        formulario = ProyectoForm()
    
    contexto = {'form':formulario}
    return render(request,'crear_proyecto.html',contexto)
