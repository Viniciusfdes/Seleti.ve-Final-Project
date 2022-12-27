from django.urls import path
from .views import *

urlpatterns = [
    path('nova_vaga/<int:id>', nova_vaga, name="nova_vaga"),
    path("home", vagas, name="dashboard_vagas"),
    path("vaga/<int:id>", vaga_specific, name="vaga_specific"),
    
]