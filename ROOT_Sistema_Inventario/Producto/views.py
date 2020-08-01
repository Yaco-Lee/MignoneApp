from django.shortcuts import render
from .forms import ProductoForm
from .models import Producto
# Create your views here.


def crear_formulario(request):
    form = ProductoForm()
    if request.method == 'POST':
        form = ProductoForm(request.POST or None)
        if form.is_valid():
            Producto.objects.create(**form.cleaned_data)
            form = ProductoForm()
        else:
            print(form.errors)
    context = {'form': ProductoForm()}
    return render(request, 'producto_crear_form.html', context)

