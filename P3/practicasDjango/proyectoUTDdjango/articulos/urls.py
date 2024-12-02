from django.urls import path
from . import views

urlpatterns = [
    path('articulos/', views.articulos, name='articulos'),
    path('categorias/', views.categorias, name='categorias'),
]
