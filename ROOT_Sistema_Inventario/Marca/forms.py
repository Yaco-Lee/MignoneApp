from django import forms


class MarcaForm(forms.Form):
    nombre = forms.CharField(max_length=200, required=True)
    empresa = forms.CharField(max_length=200, required=True)
