from django.shortcuts import render
from .forms import ProductoForm
from .models import Producto


def crear_formulario(request):
    form = ProductoForm()
    if request.method == 'POST':
        form = ProductoForm(request.POST or None)
        if form.is_valid():
            Producto.objects.create(**form.cleaned_data)
            form = ProductoForm()
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, 'producto_crear_form.html', context)

def listar_productos(request):
    productos = Producto.objects.all().order_by('categoria')
    context = {'productos': productos}
    return render(request, 'producto_listado.html', context)
