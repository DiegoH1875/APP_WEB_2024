from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='acercade'),
    path('mision/', views.mision, name='mision'),
    path('vision/', views.vision, name='vision'),
    path('login/', views.login_user, name='iniciar'),
    path('registrar/', views.registro, name='registrar'),
    path('cerrar/', views.logout_view, name='cerrar'),
    path('prueba/', views.prueba, name='prueba'),
]