from django.urls import path
from . import views

app_name = 'filme'

urlpatterns = [
path('', views.Filmes.as_view(), name="filmes"),
path('<int:pk>/', views.Filme_detalhe.as_view(), name='filme_detalhe'),
path('episodio/<int:pk>/', views.PaginaEpsodio.as_view(), name='epsodio'),
path( 'comentarios/criar/<int:episodio_id>/',  views.CriarComentarioView.as_view(), name='criar_comentario')




]