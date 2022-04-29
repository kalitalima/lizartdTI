from django.db import models


# Create your models here.
class Postagem(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=280)
    criterio = models.BooleanField(default=False)
