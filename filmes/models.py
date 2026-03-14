from django.db import models
from django.utils import timezone
from contas.models import Usuario

LISTA_CATEGORIAS = (
    ('ACAO', 'Ação'),
    ('TERROR', 'Terror'),
)



class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    capa = models.ImageField(upload_to='capas_filmes')
    categorias = models.CharField(max_length=15, choices= LISTA_CATEGORIAS)
    visulizacao = models.IntegerField(default=0)
    data = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.titulo

class Episodio(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, related_name='episodios')
    titulo = models.CharField(max_length=100)
    video = models.URLField()
    numero = models.PositiveIntegerField()
    material = models.FileField(upload_to='materiais/', blank=True, null=True)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    episodio = models.ForeignKey(Episodio,on_delete=models.CASCADE,related_name='comentarios' )
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    texto = models.TextField()

    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='respostas'
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['criado_em']

    def __str__(self):
        return self.texto[:30]




