"""PrimeiroSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
#from core.views import olamundo
#from core.views import Disciplina
from core.views import olamundo, Disciplina, home
from core.views import minha_idade, meu_nome,minha_nota,cadastro,pag1,pag2,teste

urlpatterns = [
    path('teste/', teste),
    path('pagina2/',pag2),
    path('pagina1/',pag1),
    path('nota/<str:nota>', minha_nota),
    path('cadastro/<str:nome>/<int:idade>', cadastro),
    path('nome/<str:nome>/', meu_nome),
    path('', home),
    path('idade/<int:idade>' , minha_idade),
    path('ola/',olamundo),
    path('Disciplina/', Disciplina),
    path('admin/', admin.site.urls),
]
