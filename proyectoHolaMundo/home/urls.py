from django.urls.conf import path
from .views import micasa
from . import views

urlpatterns = [
    path('', micasa, name='home'),
    path("procesamiento/", views.procesamiento, name="procesamiento"),
]
