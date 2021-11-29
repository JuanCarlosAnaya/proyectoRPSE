from django.urls import path

# from proyectoHolaMundo.grafo import views
from .views import principal

app_name = 'sintactico'

urlpatterns = [
    path("sintactico-estructural-patrones/", principal, name="patrones"), 
]