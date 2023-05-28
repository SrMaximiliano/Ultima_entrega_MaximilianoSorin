from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


"""
¿Como le hago para usar subclases? ¿Y cuentan para la cantidad de clases que pide la entrega, o al ser subclases no se las cuenta como una clase hecha?
"""

class Blog(models.Model):
    titulo= models.CharField(max_length=100, default='')
    fecha= models.DateField()
    subtitulo=models.CharField(max_length=50, default='')
    contenido= models.TextField(default='')
    autor=models.CharField(max_length=100,default='')
    imagen=models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.titulo} {self.fecha} <br> Autor: {self.autor}<br> {self.subtitulo}<br> {self.contenido}<br></br> "


class Anuncio(models.Model):
    titulo=models.CharField(max_length=50, default='')
    fecha= models.DateField()
    contenido= models.TextField(default='')
    TIPO_CHOICES = [
        ('Urgente', 'Urgente'),
        ('Aviso', 'Aviso'),
    ]
    tipo_de_anuncio = models.CharField(max_length=7, choices=TIPO_CHOICES, default='')
    def __str__(self):
        return f"{self.titulo} {self.fecha} {self.tipo_de_anuncio} "
    def get_absolute_url(self):
        return reverse('Detail', args=[str(self.id)])
    


