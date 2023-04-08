from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('servicios/', servicios, name='servicios'),
    path('sobreNosotros/', sobreNosotros, name='sobreNosotros'),
    path('compra/', compra, name='compra'),
    path('alquiler/', alquiler, name='alquiler'),
    path('asesoramiento/', asesoramiento, name='asesoramiento'),
    path('venta/', venta, name='venta'),
    path('buscarCompra/', buscarCompra, name='buscarCompra'),
]
