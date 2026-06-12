from django.urls import path
from .views import home_view,crear_proyecto_view


urlpatterns = [
    #cuando la url este vacia (la raiz del sitio), ejecuta la funcion home
    path('',home_view,name='home'),
    path('crear/',crear_proyecto_view, name='crear_proyecto')

]
