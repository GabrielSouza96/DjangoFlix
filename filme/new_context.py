from .models import Filme

#Gerenciador de contexto
def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:5]
    return {"lista_filmes_recentes": lista_filmes}

def lista_filmes_alta(request):
    lista_alta = Filme.objects.all().order_by('-visualizacoes')[0:5]
    return {"lista_filmes_alta": lista_alta}

def filme_destaque(request):
    destaque = Filme.objects.order_by('-visualizacoes')[0]
    return {"filme_destaque": destaque}