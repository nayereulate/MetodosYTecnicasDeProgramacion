from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('',                        views.inicio_view,          name='inicio'),
    path('tareas/',                 views.tareas_lista_view,    name='tareas_lista'),
    path('tareas/nueva/',           views.tarea_crear_view,     name='tarea_crear'),
    path('tareas/<int:pk>/editar/', views.tarea_editar_view,    name='tarea_editar'),
    path('tareas/<int:pk>/eliminar/', views.tarea_eliminar_view, name='tarea_eliminar'),
    path('tareas/<int:pk>/completar/', views.tarea_completar_view, name='tarea_completar'),
]
