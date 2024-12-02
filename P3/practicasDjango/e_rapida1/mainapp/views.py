from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html', {
        'title':'Inicio | Página principal',
        'content':'Bienvenido a mi ágina principal'
    })

def about(request):
    return render(request, 'mainapp/about.html', {
        'title':'Inicio | Acerca de',
        'content':'Somos un equipo de desarrollo con Django'        
    })

def mision(request):
    return render(request, 'mainapp/mision.html', {
        'title':'Misión',
        'content':'Somos un equipo de desarrollo con Django'        
    })

def vision(request):
    return render(request, 'mainapp/vision.html', {
        'title':'Visión',
        'content':'Somos un equipo de desarrollo con Django'        
    })