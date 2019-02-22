"""samportfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from core import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', views.index, name='home'),
    path ('post/', views.post, name='post'),
    path ('elements/', views.elements, name='elements'),
    path ('portfolio/', views.portfolio, name='portfolio'),
    path ('works/', views.works, name='works'),

    path ('itunes/', views.itunes, name='itunes'),
    path ('oakhouse/', views.oakhouse, name='oakhouse'),
    path ('chant/', views.chant, name='chant'),
    path ('quizzer/', views.quizzer, name='quizzer'),
    path ('wayfinder/', views.wayfinder, name='wayfinder'),
    path ('design/', views.design, name='design'),
    
]
