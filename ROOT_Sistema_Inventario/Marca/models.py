from django.db import models


class Marca(models.Model):
    nombre = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
