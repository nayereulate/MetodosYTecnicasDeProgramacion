from django.contrib import admin
from .models import Tarea


@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display  = ['titulo', 'usuario', 'prioridad', 'estado', 'fecha_limite', 'created_at']
    list_filter   = ['estado', 'prioridad', 'created_at']
    search_fields = ['titulo', 'descripcion', 'usuario__email']
    ordering      = ['-created_at']
    date_hierarchy = 'created_at'
