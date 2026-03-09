from django.db import models

from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    filme_vistos = models.ManyToManyField('filmes.Filme', related_name='usuarios', blank=True)
    foto_perfil = models.ImageField(upload_to='perfil', blank=True, null=True)






