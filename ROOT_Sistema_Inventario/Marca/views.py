from django.shortcuts import render
from .forms import MarcaForm
from .models import Marca


def crear_marca(request):
    form = MarcaForm()
    if request.method == 'POST':
        form = MarcaForm(request.POST or None)
        if form.is_valid():
            Marca.objects.create(**form.cleaned_data)
            form = MarcaForm()

    context = {'form': form}
    return render(request, 'crear_marca.html', context)

