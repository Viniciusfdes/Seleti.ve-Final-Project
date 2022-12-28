from django.urls import path
from .views import *

urlpatterns = [
    path('nova_vaga/<int:id>', nova_vaga, name="nova_vaga"),
    path("oportunidades/", vagas, name="vagas-user"),
    path("oportunidades/<int:id>", vaga_specific, name="vaga_specific"),
    path('vagas/tables/<int:id>', vagas_detais, name='vagas-details')
    
]