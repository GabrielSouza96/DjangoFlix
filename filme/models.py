from django.db import models
from django.utils import timezone

LISTA_CATEGORIAS = (
    ("ACAO", "Ação"),
    ("SUSPENSE", "Suspense"),
    ("TERROR", "Terror"),
    ("OUTROS", "Outros"),
)

# Create your models here.
class Filme(models.Model):
    titulo = models.CharField(max_length=30)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=5000)
    categoria = models.CharField(max_length=25, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)


def __str__(self):
    return Filme.titulo
