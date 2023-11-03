from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name= "inicio"),
    path('profesor/', views.profesores_formulario, name= "profesores_formulario"),
    path('estudiante/', views.estudiantes_formulario, name= "estudiantes_formulario"),
    path('entregables/', views.entregables_formulario, name= "entregables_formulario"),
    path('cursos/', views.cursos_formulario, name= "cursos_formulario"),
    path('buscar/', views.buscar, name= "buscar"),
]