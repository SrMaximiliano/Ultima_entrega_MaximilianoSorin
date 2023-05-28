from django.shortcuts import render
from django.http import HttpResponse
from App1.models import *
from App1.forms import *
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login,logout,authenticate
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView




def Inicio(request):

    return render(request, 'App1/inicio.html')
@login_required
def About_Me(request):
    return render(request, 'App1/About.html')
@login_required
def Blogs(request):
    return render(request,'App1/Blogs.html' )

def not_logged_in(request):
    return render(request,'App1/not_logged.html' )

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return redirect('inicio') 
            else:
                return redirect('login_error')  
    else:
        form = AuthenticationForm()
    return render(request, 'App1/login.html', {'form': form})


def login_error(request):
    return render(request, 'App1/login_error.html')

def register(request):
      if request.method == 'POST':
            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"App1/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     
      return render(request,"App1/registro.html" ,  {"form":form})




@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.username= informacion["username"]
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            return render(request, "App1/inicio.html")
    else:

        miFormulario = UserEditForm(initial={'username': usuario.username})
    return render(request, "App1/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})






class AnuncioList(ListView):
    model =Anuncio 
    template_name='App1/Anuncio_list.html'
class AnuncioDetalle(DetailView):
    model= Anuncio
    template_name= "App1/Anuncio_detalle.html"
class AnuncioCreacion(CreateView):
    model=Anuncio
    template_name = "App1/Anuncio_form.html"
    success_url = reverse_lazy("List")
    fields= ['titulo','fecha','tipo_de_anuncio','contenido']
class AnuncioUpdate(UpdateView):
    model=Anuncio
    success_url = reverse_lazy("List")
    fields=['titulo','fecha','tipo_de_anuncio','contenido']
class AnuncioDelete(DeleteView):
    model=Anuncio
    template_name = "App1/Anuncio_confirm_delete.html"
    success_url = reverse_lazy("List")


class BlogList(ListView):
    model = Blog
    template_name = 'App1/blog_list.html'

class BlogDetalle(DetailView):
    model= Blog
    template_name= "App1/blog_detalle.html"    

class BlogCreacion(CreateView):
    model = Blog
    template_name = 'App1/blog_form.html'
    fields = ['titulo','fecha', 'subtitulo','contenido','autor','imagen']
    success_url = reverse_lazy("Leer_Blogs") 

class BlogUpdate(UpdateView):
    model = Blog
    fields = ['titulo','fecha', 'subtitulo','contenido','autor','imagen']
    success_url = reverse_lazy("Leer_Blogs")  
    template_name = 'App1/blog_form.html'


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'App1/blog_confirm_delete.html'
    success_url = reverse_lazy("Leer_Blogs")  
    
