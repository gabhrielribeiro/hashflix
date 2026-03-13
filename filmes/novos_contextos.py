from .models import Filme


def filmes_recentes(request):
    lista_filmes = Filme.objects.order_by('-data')[:8]

    filme_principal = lista_filmes.first()

    return {
        'filmes_recentes': lista_filmes,
        'filme_principal': filme_principal
    }


def filmes_destaque(request):
    lista_filmes = Filme.objects.order_by('-visulizacao')[:8]

    return {
        'filmes_destaque': lista_filmes
    }