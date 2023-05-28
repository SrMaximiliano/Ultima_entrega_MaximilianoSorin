from django.urls import path
from App1 import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required



urlpatterns = [
   
    path('Inicio', views.Inicio, name="inicio"), #este era nuestro primer view
    path('login',views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='App1/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"), 
    path('About', login_required(views.About_Me), name="About"),
    path('Loggeate!', views.not_logged_in, name="not_logged_in"),    
    path('login_error!', views.login_error, name="login_error"),

    path('crear_blog/', views.BlogCreacion.as_view(), name='crear_blog'),
    path('Leer_Blogs/', views.BlogList.as_view(), name='Leer_Blogs'),
    path('EliminarBlog/<int:pk>/', views.BlogDeleteView.as_view(), name='EliminarBlog'),
    path('EditarBlog/<int:pk>/', views.BlogUpdate.as_view(), name='EditarBlog'),
    path('DetalleBlog/<int:pk>/', views.BlogDetalle.as_view(), name='DetalleBlog'),
    
    path('Anuncio/list/', views.AnuncioList.as_view(), name='List'), 
    path('<int:pk>/', views.AnuncioDetalle.as_view(), name='Detail'), 
    path('nuevo/', views.AnuncioCreacion.as_view(), name='New'),  
    path('editar/<int:pk>/', views.AnuncioUpdate.as_view(), name='Edit'), 
    path('borrar/<int:pk>/', views.AnuncioDelete.as_view(), name='Delete'),

]