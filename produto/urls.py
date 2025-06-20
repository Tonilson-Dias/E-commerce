from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('lista/', views.ListaProdutos.as_view(), name='lista'),
    path('lista/<slug>/', views.DetalheProduto.as_view(), name='detalhe'),
    path('adicionaraocarrinho/', views.AdicionarAoCarrinho.as_view(), 
         name='adicionaraocarrinho'),
    path('removerdocarrinho/', views.RemoverDoCarrinho.as_view(), 
         name='removerdocarrinho'),
    path('carrinho/', views.Carrinho.as_view(), name='carrinho'),
    path('resumodacompra/', views.ResumoDaCompra.as_view(), name='resumodacompra'),
   
]
