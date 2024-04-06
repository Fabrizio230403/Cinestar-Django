"""
URL configuration for djangocine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
# from tasks import apiRest
 

# Rutas URL de mi aplicacion Web

urlpatterns = [
     path('', views.index, name='index'),
     path('cines/', views.cines, name='cines'),
     path('cine/<int:id>/', views.cine, name='cine'),
     path('peliculas/<str:id>/', views.peliculas, name='peliculas'),
     path('pelicula/<int:id>/', views.pelicula, name='pelicula'),
]

# Rutas URL de mi ApiRest

# si desea ver el ApiRest, solo debe quitar el comentario del 2do urlpatterns y el from tasks import apiRest y comentar el primer urlpatterns, osea que se turnen 
# pero lo dejo asi para que vea la funcionalidad del appWeb que es lo que mas importa.

# Comando para ejecutar el proyecto es -> python manage.py runserver 

#urlpatterns = [
    #path('', apiRest.index, name='index'),
    #path('cines/', apiRest.cines, name='cines'),
    #path('cine/<int:id>/', apiRest.cine, name='cine'),
    #path('peliculas/<str:id>/', apiRest.peliculas, name='peliculas'),
    #path('pelicula/<int:id>/', apiRest.pelicula, name='pelicula'),
#]


 