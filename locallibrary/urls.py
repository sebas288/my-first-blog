""" locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
""" La lista `urlpatterns` enruta las URL a las vistas. Para más información, consulte:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Ejemplos:
Vistas de funciones
    1. Agregue una importación: desde vistas de importación my_app
    2. Agregue una URL a urlpatterns: ruta ('', views.home, name = 'home')
Vistas basadas en clase
    1. Agregue una importación: from other_app.views import Inicio
    2. Agregue una URL a urlpatterns: ruta ('', Home.as_view (), name = 'home')
Incluyendo otra URLconf
    1. Importe la función include (): desde django.urls import include, ruta
    2. Agregue una URL a urlpatterns: ruta ('blog /', include ('blog.urls'))
"" " """

from django.contrib import admin
from django.urls import path, include
from locallibrary.views import saludo, despedida, dameFecha, calcularEdad



urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('chao/' , despedida), #'chao/' es el nombre de la url , despedida es el nombre de la función
    path('fecha/' , dameFecha),
    path('' , include('blog.urls')),
    
]

