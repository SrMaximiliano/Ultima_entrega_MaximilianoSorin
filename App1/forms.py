from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import DateInput


#class CursoFormulario(forms.Form):
#    id= forms.IntegerField()
#    nombre = forms.CharField()
#    curso = forms.IntegerField()



class AnuncioFormularios(forms.ModelForm):
    fecha = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Anuncio
        fields = ['titulo', 'fecha', 'tipo_de_anuncio', 'contenido']

class BlogFormularios(forms.ModelForm):
    fecha = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Blog
        fields = ['titulo', 'fecha', 'subtitulo', 'contenido', 'autor', 'imagen']



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class UserEditForm(UserCreationForm):
    username= forms.CharField(max_length=30)
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2', 'first_name', 'last_name']
        
class AvatarFormulario(forms.Form):
    #Especificar los campos
    imagen = forms.ImageField(required=True)
