# core/urls.py
from django.urls import path
from . import views  # Importe le module views depuis core/

urlpatterns = [
    path('', views.index, name='landing_page'),  # Route racine vers la vue index
]