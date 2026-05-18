from django.shortcuts import render


def home(request):
    return render(request, 'livros/home.html')


def lista_livros(request):
    return render(request, 'livros/lista.html')


def detalhe_livro(request):
    return render(request, 'livros/detalhe.html')