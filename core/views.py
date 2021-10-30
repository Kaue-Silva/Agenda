from django.shortcuts import redirect, render
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.

# def index(request):
#     return redirect('/agenda')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        
        if usuario is not None: 
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou Senha inválido.")
    return redirect('/')


@login_required(login_url='/login/')
def lista_eventos(request):
    user = request.user
    eventos = Evento.objects.filter(usuario=user)
    dados = {'eventos':eventos}
    return render(request, 'agenda.html', dados)
