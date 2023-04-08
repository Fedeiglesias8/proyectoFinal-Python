from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def inicio(self):

    return render(self, 'inicio.html')

def venta(request):

    if request.method == 'POST':  
      miFormulario = AutosFormularios(request.POST)

      if miFormulario.is_valid():
          data = miFormulario.cleaned_data

          auto = Autos(modelo=data['modelo'], año=data['año'], kilometros=data['kilometros'], descripcion=data['descripcion'], precio=data['precio'])
          auto.save()
    
          return render(request, "inicio.html")
    
      else:
          return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    
    else:
      miFormulario = AutosFormularios()
      return render(request, "venta.html", {"miFormulario": miFormulario})

def alquiler(request):
    
    if request.method == 'POST':
        miFormulario = AlquilerFormulario(request.POST)

        if miFormulario.is_valid(): 
            data = miFormulario.cleaned_data

            alquiler = Alquiler(modelo=data['modelo'], año=data['año'], descripcion=data['descripcion'], precio=data['precio'])
            alquiler.save()
        
            return render(request, "inicio.html")
        
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
        
    else:
        miFormulario = AlquilerFormulario()
        return render(request, "alquiler.html", {"miFormulario": miFormulario})

def asesoramiento(request):
    if request.method == 'POST':
            miFormulario = AsesoramientoFormulario(request.POST)

            if miFormulario.is_valid():
                data = miFormulario.cleaned_data

                asesoramiento = Asesoramiento(nombre=data['nombre'], telefono=data['telefono'], dataAsesoramiento=data['dataAsesoramiento'], modeloAuto=data['modeloAuto'])
                asesoramiento.save()

                return render(request, "inicio.html")

            else:
                return render(request, "inicio.html", {"mensaje": "Formulario invalido"})

    else:
        miFormulario = AsesoramientoFormulario()
        return render(request, "asesoramiento.html", {"miFormulario": miFormulario})

def servicios(self):

    return render(self, 'servicios.html')

def sobreNosotros(self):

    return render(self, 'sobreNosotros.html')

def compra(request):

    return render(request, 'compra.html')

def buscarCompra(request):

    if request.GET['modelo']:

        modelo= request.GET['modelo']
        autos= Autos.objects.filter(modelo=modelo)

        return render(request, 'resultadoDeBusqueda.html',{'autos': autos, 'modelo': modelo})
