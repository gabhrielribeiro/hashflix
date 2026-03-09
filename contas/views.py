from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, FormView, UpdateView, ListView
from . forms import  CriarContaForm, Homeform
from . models import Usuario
from filmes.models import Filme







class HomeFilmes(FormView):
    template_name = 'index.html'
    form_class = Homeform

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuario = Usuario.objects.filter(email=email)

        if usuario:

            return reverse('contas:login')

        else:
            return reverse('contas:criarconta')



    def get(self, request, *args, **kwargs):

            if request.user.is_authenticated:

                return redirect('filme:filmes')
            else:

                return super().get(request, *args, **kwargs)


class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:filmes')


class EditarPerfil(UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email', 'foto_perfil']

    def get_object(self):
        # garante que o usuário só edite o próprio perfil
        return self.request.user

    def get_success_url(self):
        return reverse('filme:filmes')


class PaginaBusca(ListView):
    template_name = 'busca.html'
    model = Filme

    def get_queryset(self):
        parametro = self.request.GET.get('query')

        if parametro:

            return Filme.objects.filter(titulo__icontains=parametro)

        else:
            return Filme.objects.all()













