from django.db import models

# Create your models here.
class Promocoes(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.CharField(max_length=50, blank=True, null=True)
    desconto = models.CharField(max_length=50, blank=True, null=True)
