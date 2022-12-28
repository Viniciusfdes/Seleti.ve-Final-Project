from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse

# Create your views here.    
def cadastro(request):
    if request.method == "GET":
        return render(request, 'page-register.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        if not password == confirm_password:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/auth/cadastro')
        
        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0 or len(confirm_password.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/auth/cadastro')
        
        user_username = User.objects.filter(username=username)
        if user_username.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usário com esse username')
            return redirect('/auth/cadastro')

        user_email = User.objects.filter(email=email)
        if user_email.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usário com esse email')
            return redirect('/auth/cadastro')

        try:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=name)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso')
            return redirect('/auth/login')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/auth/cadastro')

    
def login(request):
    if request.method == "GET":
        return render(request, 'page-login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_staff: 
                login_django(request, user)
                return redirect('/home/empresas')
            else:
                messages.add_message(request, constants.ERROR, 'Usuário sem acesso administrativo')
                return redirect('/auth/login')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect('/auth/login')

        # if user.is_authenticated:
        # return redirect('/')

def sair(request):
    logout(request)
    return redirect('/auth/login')


