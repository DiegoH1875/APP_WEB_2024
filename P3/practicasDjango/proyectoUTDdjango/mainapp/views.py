from django.shortcuts import render, redirect # type: ignore
# from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import register_form_p
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title':'Inicio',
        'content':'.::Bienvenido::.'
    })

@login_required(login_url='inicio')
def about(request):
    return render(request, 'mainapp/about.html', {
        'title':'Acerca de',
        'content':'.::Institucion con el mas alto prestigio::.'
    })

@login_required(login_url='inicio')
def mision(request):    
    return render(request, 'mainapp/mision.html', {
        'title':'Mision',
        'content':'.::Ser la mejor universidad de Durango::.'
    })

@login_required(login_url='inicio')
def vision(request):
    return render(request, 'mainapp/vision.html', {
        'title':'Vision'
    })


def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.warning(request, "Credenciales no válidas")

        return render (request, 'users/login.html')

def registro(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        register_form = register_form_p()
        if request.method == "POST":
            register_form = register_form_p(request.POST)

            if register_form.is_valid():
                user = register_form.save()  # Se guarda el usuario
                messages.success(request, "Registro exitoso")
                return redirect('iniciar')
            else:
                messages.error(request, "Error en el registro. Verifique los campos.")

        return render(request, 'users/register.html', {
            'title': 'Registrarse',
            'register_form': register_form
        })


def logout_view(request):
    logout(request)
    messages.success(request, "Sesión cerrada")
    return redirect('index')

# def error404(request, exception):
#     return redirect(request, 'inicio')

def prueba(request):
    return render(request, 'mainapp/404.html')

def error404_2(request, exception):
    return render(request, 'mainapp/404.html')