from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def mision_vision(request):
    return render(request, 'mision_vision.html')

def noticias(request):
    return render(request, 'noticias.html')

def contacto(request):
    return render(request, 'contacto.html')

