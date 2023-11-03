from django import forms

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    mail = forms.EmailField()
    profesion = forms.CharField()

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    mail = forms.EmailField()

class EntregableFormulario(forms.Form):
    nombre = forms.CharField()
    fecha_entrega = forms.DateField()
    entregado = forms.BooleanField()