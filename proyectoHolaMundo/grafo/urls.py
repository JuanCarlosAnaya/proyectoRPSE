from django.urls import path
from .views import grafos, procesamiento

app_name = 'grafo'

urlpatterns = [
    path("grafo/", grafos, name="grafo"),
    path("procesamiento/", procesamiento, name="procesamiento"),
]