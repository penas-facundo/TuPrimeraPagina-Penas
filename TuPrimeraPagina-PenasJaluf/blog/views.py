from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, ArticuloForm, BuscarArticuloForm
from .models import Articulo

def home(request):
    return render(request, 'blog/home.html')

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    return render(request, 'blog/crear_autor.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'blog/crear_categoria.html', {'form': form})

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArticuloForm()
    return render(request, 'blog/crear_articulo.html', {'form': form})

def buscar_articulo(request):
    if request.method == 'POST':
        form = BuscarArticuloForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultados = Articulo.objects.filter(titulo__icontains=titulo)
            return render(request, 'blog/resultados_busqueda.html', {'resultados': resultados})
    else:
        form = BuscarArticuloForm()
    return render(request, 'blog/buscar_articulo.html', {'form': form})