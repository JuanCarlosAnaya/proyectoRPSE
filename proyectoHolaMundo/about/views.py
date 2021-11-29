#from django.http.response import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.

def about(request):
    
    resultado = mifuncion(request)
    template_name='about/about.html'
    # dict = {"nombreusuario":resultado, 'edad': 24}
    return render(request, template_name, )

    
    
def mifuncion(*args):
    return 'juan'
    
"""
    textHtml =
    
    <h1>Hola mundo </h1>
    
    <ul>
    
        <li>Donde
        <li>la fiesta
        
    </ul>    
    return HttpResponse(textHtml)
"""