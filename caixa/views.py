from django.shortcuts import render, redirect
from .models import Usuario
from django.http import HttpResponse

def inicio(request):
    return render(request, 'inicio.html')


def cadastro(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        return render(request, 'cadastro.html', {'status':status})
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
            return redirect('/cadastro/?status=1')
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

        if Usuario.objects.filter(email=email).exists() & Usuario.objects.filter(senha=senha).exists():
            item.valor = novo_valor
            item.save()
            return render(request, 'opcoes.html')
        else:
            return render(request, 'deposito.html')
        
def saque(request):
    if request.method == 'GET':
        return render(request, 'saque.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        valor = request.POST.get('valor')
        item = Usuario.objects.get(email=email)
        valor_atual = item.valor

        if Usuario.objects.filter(email=email).exists() & Usuario.objects.filter(senha=senha).exists():
            if int(valor) > valor_atual:
                return render(request, 'saque.html')
            else:
                novo_valor = valor_atual - int(valor)
                item.valor = novo_valor
                item.save()
                return render(request, 'opcoes.html')
        else:
            return render(request, 'saque.html')

def transferencia(request):
    if request.method == 'GET':
        return render(request, 'transferencia.html')
    else:
        email_paga = request.POST.get('email_paga')
        senha = request.POST.get('senha')
        email_bene = request.POST.get('email_bene')
        valor = request.POST.get('valor')
        item1 = Usuario.objects.get(email=email_paga)
        item2 = Usuario.objects.get(email=email_bene)
        valor_atual_paga = item1.valor
        valor_atual_bene = item2.valor

        if Usuario.objects.filter(email=email_paga).exists() & Usuario.objects.filter(senha=senha).exists() & Usuario.objects.filter(email=email_bene).exists():
            if int(valor) > valor_atual_paga:
                return render(request, 'saque.html')
            else:
                novo_valor_paga = valor_atual_paga - int(valor)
                novo_valor_bene = valor_atual_bene + int(valor)
                item1.valor = novo_valor_paga
                item2.valor = novo_valor_bene
                item1.save()
                item2.save()

                return render(request, 'opcoes.html')
        else:
            return render(request, 'transferencia.html')