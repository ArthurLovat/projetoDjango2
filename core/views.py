from pyexpat.errors import messages

from django.shortcuts import render
from django.contrib import messages
from core.forms import ContatoForm


def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None) #pode ser vasil ou none
    #esse é um modelo simples de formulario onde não é salvo na banco de dados

    if str(request.method) ==  'POST':    #se for post e pq foi preenchido
        if form.is_valid(): #se não tiver erro retorna true, no geral validação de dados
            form.send_mail()

            '''nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviado!')
            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')
            '''

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()

        else:
            messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'form' : form
    }
    return render(request, 'contato.html', context)


def produto(request):
    return render(request, 'produto.html')
