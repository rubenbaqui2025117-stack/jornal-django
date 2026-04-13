"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from noticias import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_artigos, name='lista_artigos'),
    path('artigo/<int:pk>/', views.detalhe_artigo, name='detalhe_artigo'),
    path('artigo/<int:pk>/comentarios/', views.comentarios_artigo, name='comentarios_artigo'),
]