from . models import Filme

def filmes_recentes(request):
    lista_filmes = Filme.objects.order_by('-data')[:8]

    if lista_filmes:
        filme_principal = lista_filmes[0]
    else:
        filme_principal = None

    return {
        'filmes_recentes': lista_filmes,
        'filme_principal': filme_principal
    }


def filmes_destaque(request):
    lista_filmes = Filme.objects.order_by('-visulizacao')[0:8]
    return {'filmes_destaque':lista_filmes}


