from django.contrib import admin
from paginas.models import Cliente,Proyecto,Tecnologia

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Tecnologia)
admin.site.register(Proyecto)
