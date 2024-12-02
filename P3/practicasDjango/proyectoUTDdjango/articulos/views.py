from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article, Category

# Create your views here.

@login_required(login_url='inicio')
def articulos(request):
    articulos = Article.objects.all()
    return render(request, 'articulos/articulos.html', {
        'title':'Artículos',
        'articulos': articulos,
    })

@login_required(login_url='inicio')
def categorias(request):
    categorias = Category.objects.all()
    return render(request, 'categorias/categorias.html', {
        'title':'Categorías',
        'categorias': categorias,
    })