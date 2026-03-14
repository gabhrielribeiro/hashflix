from django.shortcuts import render, get_object_or_404, redirect
from . models import Filme, Episodio, Comentario
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CometarioEpsodio


# Create your views here.


class Filmes(LoginRequiredMixin, ListView):
    template_name = 'filmes.html'
    model = Filme




class Filme_detalhe(LoginRequiredMixin, DetailView):
    template_name = 'filmes_detalhe.html'
    model = Filme
    context_object_name = 'filme'

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visulizacao +=1
        filme.save()

        usuario = request.user
        usuario.filme_vistos.add(filme)



        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filme = self.get_object()
        filmes_relacionados = Filme.objects.filter(categorias = filme.categorias).exclude(id=filme.id)[:5]
        context['filmes_relacionados'] = filmes_relacionados

        return context




class PaginaEpsodio(DetailView):
    template_name='epsodio.html'
    model = Episodio

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CometarioEpsodio()

        context['comentarios'] = (
            Comentario.objects
            .filter(episodio=self.object, parent__isnull=True)
            .select_related('usuario')
            .prefetch_related('respostas__usuario')
            .order_by('-criado_em')
        )

        return context


class CriarComentarioView(LoginRequiredMixin, FormView):
    form_class = CometarioEpsodio

    def form_valid(self, form):
        episodio = get_object_or_404(Episodio, pk=self.kwargs['episodio_id'])

        comentario = form.save(commit=False)
        comentario.usuario = self.request.user
        comentario.episodio = episodio

        parent_id = self.request.POST.get('parent_id')
        if parent_id:
            comentario.parent_id = parent_id

        comentario.save()

        return redirect(self.get_success_url())

    def get_success_url(self):
        referer = self.request.META.get('HTTP_REFERER', '/')
        return f"{referer}#secaoComentarios"








