from django import forms

class AutosFormularios(forms.Form):
    marca= forms.CharField(max_length=20)
    modelo= forms.CharField(max_length=20)
    año= forms.IntegerField()
    kilometros= forms.IntegerField()
    descripcion= forms.CharField(max_length=250)
    precio= forms.IntegerField()

class AlquilerFormulario(forms.Form):
    marca= forms.CharField(max_length=20)
    año= forms.IntegerField()
    descripcion= forms.CharField(max_length=250)
    precio= forms.IntegerField()


class AsesoramientoFormulario(forms.Form):
    nombre= forms.CharField(max_length=20)
    telefono= forms.IntegerField()
    dataAsesoramiento= forms.CharField(max_length=250)
    modeloAuto= forms.CharField(max_length=50)