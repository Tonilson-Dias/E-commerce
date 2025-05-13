from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

class ListaProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Listar Produto')

class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhar Produto')

class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adiciobnar Ao Carrinho')

class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover do Carinho')

class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')

class Finalizar(View):
  def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')