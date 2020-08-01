from django import forms


class ProductoForm(forms.Form):
    cod_de_barra = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=3000)
    marca = forms.CharField(max_length=500)
    categoria = forms.CharField(max_length=500)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = forms.DateField()
    ubicacion = forms.CharField(max_length=500)
    proveedor = forms.CharField(max_length=300)
    observaciones = forms.CharField(max_length=3000)