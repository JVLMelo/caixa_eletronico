from django.shortcuts import render, redirect
from .models import Usuario
from django.http import HttpResponse

def inicio(request):
    return render(request, 'inicio.html')


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        nome_mae = request.POST.get('nome_mae')
        nome_pai = request.POST.get('nome_pai')
        senha = request.POST.get('senha')

        usuario = Usuario(
            nome=nome,
            email=email,
            nome_mae=nome_mae,
            nome_pai=nome_pai,
            senha=senha,
            valor=0
        )

        if Usuario.objects.filter(email=email).exists():
            return HttpResponse('Existe')
        else:
            usuario.save()
            return render(request, 'login.html')
        

        

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if Usuario.objects.filter(email=email).exists() & Usuario.objects.filter(senha=senha).exists():
            return render(request, 'opcoes.html')
        else:
            return render(request, 'login.html')
        
def opcoes(request):
    return render(request, 'opcoes.html')

def deposito(request):
    if request.method == 'GET':
        return render(request, 'deposito.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        valor = request.POST.get('valor')
        item = Usuario.objects.get(email=email)
        valor_atual = item.valor
        novo_valor = valor_atual + int(valor)

        item.valor = novo_valor
        item.save()

        return HttpResponse(item.valor)
        