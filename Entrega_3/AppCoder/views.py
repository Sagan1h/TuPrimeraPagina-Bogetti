from django.shortcuts import render, redirect
from .models import Curso, Estudiante, Profesor, Entregable
from .forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario, EntregableFormulario

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def cursos_formulario(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_curso = Curso(curso=informacion["curso"], camada=informacion["camada"])
            nuevo_curso.save()
            return redirect("inicio")
    else:
        mi_formulario = CursoFormulario()
        return render(request, "cursos_formulario.html", {"mi_formulario" : mi_formulario})

def estudiantes_formulario(request):
    if request.method == "POST":
        mi_formulario2 = EstudianteFormulario(request.POST)
        
        if mi_formulario2.is_valid():
            informacion2 = mi_formulario2.cleaned_data
            nuevo_estudiante = Estudiante(nombre=informacion2["nombre"], apellido=informacion2["apellido"], mail=informacion2["mail"])
            nuevo_estudiante.save()
            return redirect("inicio")
    else:
        mi_formulario2 = EstudianteFormulario()
        return render(request, "estudiantes_formulario.html", {"mi_formulario2" : mi_formulario2})

def profesores_formulario(request):
    if request.method == "POST":
        mi_formulario3 = ProfesorFormulario(request.POST)
        
        if mi_formulario3.is_valid():
            informacion3 = mi_formulario3.cleaned_data
            nuevo_profesor = Profesor(nombre=informacion3["nombre"], apellido=informacion3["apellido"], mail=informacion3["mail"], profesion=informacion3["profesion"])
            nuevo_profesor.save()
            return redirect("inicio")
    else:
        mi_formulario3 = ProfesorFormulario()
        return render(request, "profesores_formulario.html", {"mi_formulario3" : mi_formulario3})

def entregables_formulario(request):
    if request.method == "POST":
        mi_formulario4 = EntregableFormulario(request.POST)
        
        if mi_formulario4.is_valid():
            informacion4 = mi_formulario4.cleaned_data
            nuevo_entregable = Entregable(nombre=informacion4["nombre"], fecha_entrega=informacion4["fecha_entrega"], entregado=informacion4["entregado"])
            nuevo_entregable.save()
            return("inicio")
    else:
        mi_formulario4 = EntregableFormulario()
        return render(request, "entregables_formulario.html", {"mi_formulario4" : mi_formulario4})

def buscar(request):
    camada = request.GET.get("camada")
    if camada:
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "resultadosBusqueda.html", {"cursos" : cursos, "camada" : camada})
    else:
        return render(request, "datosInvalidos.html")