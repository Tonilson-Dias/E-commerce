from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
from . import models

from pprint import pprint

class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 3
    

class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'
    
    


class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        # TODO: Remover linhas abaixo
        #if self.request.session.get('carrinho'):
        #    del self.request.session['carrinho']
        #    self.request.session.save()

        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
            
            )
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            messages.error(
                self.request,
                'Produto nao existe'
            )
            return redirect(http_referer)
        
        variacao = get_object_or_404(models.Variacao, id= variacao_id)
        variacao_estoque = variacao.estoque
        produto = variacao.produto

        produto_id = produto.id
        produto_nome = produto.nome
        variacao_nome = variacao.nome or ''
        preco_unitario = variacao.preco
        preco_unitario_promocional = variacao.preco_promocional
        quantidade = 1
        slug = produto.slug
        imagem = produto.imagem

        if imagem:
            imagem = imagem.name
        else:
            imagem = ''

        if variacao.estoque < 1:
            messages.error(
                self.request,
                'Estoque insuficiente'
            )
            return redirect(http_referer)
        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()

        carrinho = self.request.session['carrinho']

        if variacao_id in carrinho:
           quantidade_carrinho = carrinho[variacao_id]['quantidade']
           quantidade_carrinho += 1

           if variacao_estoque < quantidade_carrinho:
               messages.warning(
                   self.request,
                   f'Estoque insuficiente para {quantidade_carrinho}x no '
                   f'produto "{produto.nome}." Adicionamos {variacao_estoque}x '
                   f'no seu carrinho'
               )
               quantidade_carrinho = variacao_estoque

           carrinho[variacao_id]['quantidade']= quantidade_carrinho
           carrinho[variacao_id]['preco_quantitativo']= preco_unitario * \
            quantidade_carrinho
           carrinho[variacao_id]['preco_quantitativo_promocinal']= preco_unitario_promocional * \
            quantidade_carrinho
           
        else:
           carrinho[variacao_id] = {
                'produto_id': produto_id,
                'produto_nome': produto_nome,  
                'variacao_nome': variacao_nome,
                'variacao_id': variacao_id,
                'preco_unitario': preco_unitario,
                'preco_unitario_promocional': preco_unitario_promocional, 
                'preco_quantitativo': preco_unitario,
                'preco_quantitativo_promocinal': preco_unitario_promocional,
                'quantidade': 1,
                'slug': slug,
                'imagem': imagem,
           }

        self.request.session.save()
        
        messages.success(
            self.request,
            f'Produto {produto.nome} {variacao.nome} adicionado ao seu  '
            f'carrinho {carrinho[variacao_id]["quantidade"]}x.'
        )

        return redirect(http_referer)


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
            
            )
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            return redirect(http_referer)
        
        if not self.request.session.get('carrinho'):
            return redirect(http_referer)
        
        if variacao_id not in self.request.session['carrinho']:
             return redirect(http_referer)

        Carrinho = self.request.session['carrinho'][variacao_id]

        messages.success(
            self.request,
          f'Produto {Carrinho['produto_nome']} {Carrinho["variacao_nome"]} '
          f'removido do seu carrinho.'
        )

        del self.request.session['carrinho'][variacao_id]
        self.request.session.save()
        return redirect(http_referer)
      

class Carrinho(View):
    def get(self, *args, **kwargs):
        contexto = {
            'carrinho': self.request.session.get('carrinho', {})
            
            }
        return render(self.request, 'produto/carrinho.html', contexto)

class ResumoDaCompra(View):
  def get(self, *args, **kwargs):
        return HttpResponse('ResumoDaCompra')