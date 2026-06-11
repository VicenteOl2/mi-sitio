from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    correo_contacto = models.EmailField(blank=True,null=True)
    
    
    def __str__(self):
        return self.nombre_empresa

class Tecnologia(models.Model):
    nombre_Tecnologia = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_Tecnologia

class Proyecto(models.Model):
    titulo_proyecto = models.CharField(max_length=50)
    descripcion = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tecnologias = models.ManyToManyField(Tecnologia)

    def __str__(self):
        return self.titulo_proyecto
   




