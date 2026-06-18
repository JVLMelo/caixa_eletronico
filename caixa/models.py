from django.db import models

class Usuario(models.Model):

    nome = models.CharField(max_length=255)
    email = models.EmailField()
    nome_mae = models.CharField(max_length=255)
    nome_pai = models.CharField(max_length=255)
    senha = models.PositiveIntegerField()
    valor = models.IntegerField()
