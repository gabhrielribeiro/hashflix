from django.urls import path, reverse_lazy
from filmes.urls import app_name
from . import views
from django.contrib.auth import views as auth_views

app_name = 'contas'


urlpatterns = [
    path('', views.HomeFilmes.as_view(), name='homefilmes'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('criarconta/', views.CriarConta.as_view(), name='criarconta'),
    path('editarperfil/<int:pk>/', views.EditarPerfil.as_view(), name='editarperfil'),
    path('mudarsenha/', auth_views.PasswordChangeView.as_view(template_name='editarperfil.html', success_url=reverse_lazy('filme:filmes')),  name='mudarsenha'),
    path('pesquisar/', views.PaginaBusca.as_view(), name='pesquisar')


]