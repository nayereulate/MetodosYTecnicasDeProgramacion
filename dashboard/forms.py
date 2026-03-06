"""
dashboard/forms.py
──────────────────
Formulario para crear y editar tareas.
"""

from django import forms
from .models import Tarea


class TareaForm(forms.ModelForm):
    class Meta:
        model  = Tarea
        fields = ['titulo', 'descripcion', 'prioridad', 'estado', 'fecha_limite']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Título de la tarea',
                'autofocus': True,
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 3,
                'placeholder': 'Descripción opcional...',
            }),
            'prioridad': forms.Select(attrs={
                'class': 'form-input',
            }),
            'estado': forms.Select(attrs={
                'class': 'form-input',
            }),
            'fecha_limite': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
        }
