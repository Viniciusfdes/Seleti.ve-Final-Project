from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.messages import constants
from django.contrib import messages
# from rembg import remove
# from PIL import Image

def nova_empresa(request):
    if request.method == "GET":
        nichos = Nichos.objects.all()
        techs = Tecnologias.objects.all()
        return render(request, 'nova_empresa.html', {'techs': techs, 'nichos': nichos})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cidade = request.POST.get('cidade')
        endereco = request.POST.get('endereco')
        nicho = request.POST.get('nicho')
        caracteristicas = request.POST.get('caracteristicas')
        tecnologias = request.POST.getlist('tecnologias')
        logo = request.FILES.get('logo')
        
        if (len(nome.strip()) == 0 or len(email.strip()) == 0 or len(cidade.strip()) == 0 or len(endereco.strip()) == 0 or len(caracteristicas.strip()) == 0 or (not logo)): 
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/home/nova_empresa')

        if logo.size > 100_000_000:
            messages.add_message(request, constants.ERROR, 'A logo da empresa deve ter menos de 10MB')
            return redirect('/home/nova_empresa')

        # if nicho not in [i[0] for i in Nichos.nicho]:
        #     messages.add_message(request, constants.ERROR, 'Nicho de mercado inválido')
        #     return redirect('/home/nova_empresa')]
        
        empresa = Empresa(logo=logo, nome=nome, email=email, cidade=cidade, endereco=endereco, caracteristica_empresa=caracteristicas)
        empresa.nicho_mercado = Nichos(id=nicho)
        empresa.save()

        print(logo)

        # img = Image.open('C:/Users/vinic/OneDrive/Área de Trabalho/DJANGO/seleti.ve/media/logo_empresa/' + str(logo))
        # img_bg = remove(img)
        # img_bg.save('C:/Users/vinic/OneDrive/Área de Trabalho/DJANGO/seleti.ve/media/logo_empresa/' + str(logo))
        # empresa.logo=img_bg

        empresa.tecnologias.add(*tecnologias)
        empresa.save()
        messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso')
        return redirect('/home/empresas')

def empresas(request):
    technologias_filtrar = request.POST.get('tecnologias')
    nome_filtrar = request.POST.get('nome')
    empresas = Empresa.objects.all()

    if technologias_filtrar:
        empresas = empresas.filter(tecnologias = technologias_filtrar)
    
    if nome_filtrar:
        empresas = empresas.filter(nome__icontains = nome_filtrar)

    tecnologias = Tecnologias.objects.all()
    return render(request, 'empresas.html', {'empresas': empresas, 'tecnologias': tecnologias})

def excluir_empresa(request, id):
    empresa = Empresa.objects.get(id=id)
    vagas = Vagas.objects.get(empresa_id=id)
    empresa.delete()
    vagas.delete()
    messages.add_message(request, constants.SUCCESS, 'Empresa excluída com sucesso')
    return redirect('/home/empresas')

def empresa_specific(request, id):
    empresa_unica = get_object_or_404(Empresa, id=id)
    empresas = Empresa.objects.all()
    tecnologias = Tecnologias.objects.all()
    vagas = Vagas.objects.filter(empresa_id=id)
    return render(request, 'empresa_specific.html', {'empresa': empresa_unica,'tecnologias': tecnologias, 'empresas': empresas,'vagas': vagas})