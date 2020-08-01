from django.db import models

# Create your models here.


class Producto(models.Model):
    Id = models.IntegerField(primary_key=True, auto_created=True)
    cod_de_barra = models.CharField(max_length=200, unique=True, blank=False)
    descripcion = models.CharField(max_length=3000)
    marca = models.CharField(max_length=500)
    categoria = models.CharField(max_length=500)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField()
    ubicacion = models.CharField(max_length=500)
    proveedor = models.CharField(max_length=300)
    observaciones = models.CharField(max_length=3000)
