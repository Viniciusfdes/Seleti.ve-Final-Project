from django.shortcuts import render, redirect, get_object_or_404
from register.models import Vagas
from django.http import Http404, HttpResponse
from register.models import *
from django.contrib.messages import constants
from django.contrib import messages


def vaga_specific(request, id):
  vaga_unica = get_object_or_404(Vagas, id=id)
  empresa = get_object_or_404(Empresa, id=vaga_unica.empresa.id)
  vagas_empresa = Vagas.objects.filter(empresa=empresa.id)

  return render(request, 'vaga_specific.html', {'vaga': vaga_unica, 'vagas_empresa': vagas_empresa})

def vagas(request):
  vagas = Vagas.objects.all()

  tecnologias_filtrar = request.POST.get('tecnologias')
  nome_filtrar = request.POST.get('nome')
  empresas = Empresa.objects.all()

  if tecnologias_filtrar:
    empresas = empresas.filter(tecnologias = tecnologias_filtrar)
    
  if nome_filtrar:
    empresas = empresas.filter(nome__icontains = nome_filtrar)

  tecnologias = Tecnologias.objects.all()
  return render(request, 'vagas.html', {'empresas': empresas, 'tecnologias': tecnologias, 'vagas': vagas })

def nova_vaga(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        email = request.POST.get('email')
        tecnologias_domina = request.POST.getlist('tecnologias_domina')
        tecnologias_nao_domina = request.POST.getlist('tecnologias_nao_domina')
        experiencia = request.POST.get('experiencia')
        data_final = request.POST.get('data_final')
        empresa = request.POST.get('empresa')
        status = request.POST.get('status')

        # TODO: validations

        vaga = Vagas(titulo=titulo, email=email, nivel_experiencia=experiencia, data_final=data_final, empresa_id=empresa, status=status)
        vaga.save()

        vaga.tecnologias_estudar.add(*tecnologias_nao_domina)
        vaga.tecnologias_dominadas.add(*tecnologias_domina)

        vaga.save()        
        
        messages.add_message(request, constants.SUCCESS, 'Vaga criada com sucesso.')
        return redirect(f'/home/empresas/{id}')
    elif request.method == "GET":
        return render('vagas.html')