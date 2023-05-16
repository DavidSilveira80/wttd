from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def existe(request):
    return render(request, 'existe.html')
