from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('lista/', views.ListaProdutos.as_view(), name='lista'),
    path('adicionaraocarrinho/', views.AdicionarAoCarrinho.as_view(), 
         name='adicionaraocarrinho'),
    path('removerdocarinho/', views.RemoverDoCarrinho.as_view(), 
         name='removerdocarinho'),
    path('carinho/', views.Carrinho.as_view(), name='carinho'),
    path('finalizar/', views.Finalizar.as_view(), name='finalizar'),
    
]
