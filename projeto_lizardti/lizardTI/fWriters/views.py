# Create your views here.
from django.shortcuts import render, redirect
from .forms import PostagemForms


def index(request):
    return render(request, 'index.html')


def cadastro_postagem(request):

    if request.method == 'POST':
        form = PostagemForms(request.POST)
        form.save()
        return redirect('index')


def cadastro_inscricao(request):
    return render(request, 'inscrever.html')
