from django.contrib import admin
from .models import *

class TecnologiasAdmin(admin.ModelAdmin):
    list_display = ('id', 'tecnologia')

class NichosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nicho')

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cidade', 'nicho_mercado', 'cnpj')

class VagasAdmin(admin.ModelAdmin):
    list_display = ('id', 'empresa', 'titulo', 'nivel_experiencia', 'data_final', 'status')

admin.site.register(Tecnologias, TecnologiasAdmin)
admin.site.register(Nichos, NichosAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Vagas, VagasAdmin)
