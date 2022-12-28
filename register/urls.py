from django.urls import path
from .views import * 

urlpatterns = [
    path('nova_empresa/', nova_empresa, name="nova_empresa"),
    path('empresas/', empresas, name="empresas"),
    path('excluir_empresa/<int:id>', excluir_empresa, name="excluir_empresa"),
    # path('editar_empresa/<int:id>', editar_empresa, name="editar_empresa"),
    path('empresas/<int:id>', empresa_specific, name="empresa_specific"),
    path('', home, name='home')
]