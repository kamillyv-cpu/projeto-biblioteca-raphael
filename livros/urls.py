from django.urls import path
from . import views

app_name = 'livros'

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.lista_livros, name='lista'),
    path('detalhe/', views.detalhe_livro, name='detalhe'),
]