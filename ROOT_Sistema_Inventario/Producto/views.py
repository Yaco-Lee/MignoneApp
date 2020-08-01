from django.shortcuts import render
from .forms import ProductoForm
# Create your views here.


def crear_formulario(request):
    context = {'form': ProductoForm()}
    return render(request, 'producto_crear_form.html', context)
