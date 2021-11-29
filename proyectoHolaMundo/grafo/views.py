# import numpy as np
from django.shortcuts import render
# from home.models import tessue

# Create your views here.
def grafos(request):
    template_name="grafo/grafo.html"
 
    return render(request, template_name,)

def procesamiento():
    print("hola")