from django.urls import path
from .views import *

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name='login'),
    path('sair/', sair, name="sair")
]