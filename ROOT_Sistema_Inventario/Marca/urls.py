from django.urls import path
from .views import crear_marca


urlpatterns = [
    path('', crear_marca)
]
