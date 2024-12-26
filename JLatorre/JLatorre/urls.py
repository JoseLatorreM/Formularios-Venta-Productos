"""
URL configuration for JLatorre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from AplicacionRecu import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/', views.VistaCompras, name='Listado'),
    path('autor/', views.Autor, name='autor'),
    path('F', views.Formulario, name='Formulario'),
    path('guardar_datos/', views.guardar_datos, name='guardar_datos'),
    path('borrar/<int:id>/', views.borrar, name="borrar"),
    path('buscar/', views.buscar_por_pk, name='buscar_por_pk'),
    path('modificar_objeto/<str:rut>/', views.ModificarDato, name='modificarDato'),
    path('', include('AplicacionRecu.urls')),
]

