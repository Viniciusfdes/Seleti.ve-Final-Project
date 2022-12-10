from django.urls import path
from .views import *

urlpatterns = [
    path('nova_vaga/<int:id>', nova_vaga, name="nova_vaga")
]