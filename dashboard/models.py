"""
dashboard/models.py
────────────────────
Modelo de Tareas del usuario — ejemplo de CRUD completo con Django ORM.
"""

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Tarea(models.Model):
    """Tarea personal del usuario autenticado."""

    PRIORIDAD_CHOICES = [
        ('baja',   '🟢 Baja'),
        ('media',  '🟡 Media'),
        ('alta',   '🔴 Alta'),
    ]

    ESTADO_CHOICES = [
        ('pendiente',   'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('completada',  'Completada'),
    ]

    usuario     = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tareas',
        verbose_name=_('usuario'),
    )
    titulo      = models.CharField(_('título'), max_length=200)
    descripcion = models.TextField(_('descripción'), blank=True)
    prioridad   = models.CharField(_('prioridad'), max_length=10, choices=PRIORIDAD_CHOICES, default='media')
    estado      = models.CharField(_('estado'), max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_limite = models.DateField(_('fecha límite'), blank=True, null=True)
    created_at  = models.DateTimeField(_('creado'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('actualizado'), auto_now=True)

    class Meta:
        verbose_name        = _('tarea')
        verbose_name_plural = _('tareas')
        ordering            = ['-created_at']

    def __str__(self):
        return f"[{self.prioridad.upper()}] {self.titulo}"

    @property
    def esta_completada(self):
        return self.estado == 'completada'

    @property
    def color_prioridad(self):
        colores = {'baja': 'green', 'media': 'yellow', 'alta': 'red'}
        return colores.get(self.prioridad, 'gray')
