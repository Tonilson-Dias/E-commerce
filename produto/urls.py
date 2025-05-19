from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('lista/', views.ListaProdutos.as_view(), name='lista'),
    path('adicionaraocarrinho/', views.AdicionarAoCarrinho.as_view(), 
         name='adicionaraocarrinho'),
    path('removerdocarinho/', views.RemoverDoCarrinho.as_view(), 
         name='removerdocarinho'),
    path('carrinho/', views.Carrinho.as_view(), name='carrinho'),
    path('finalizar/', views.Finalizar.as_view(), name='finalizar'),
    path('lista/<slug>/', views.DetalheProduto.as_view(), name='detalhe'),
]
