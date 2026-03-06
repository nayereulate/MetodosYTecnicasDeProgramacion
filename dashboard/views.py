"""
dashboard/views.py
──────────────────
Vistas protegidas del dashboard: resumen, CRUD de tareas.
Todas requieren autenticación con @login_required.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Q

from .models import Tarea
from .forms import TareaForm


# ── Inicio / Resumen ──────────────────────────────────────────────────────────

@login_required
def inicio_view(request):
    """
    Panel principal: muestra estadísticas y las últimas tareas del usuario.
    Demuestra el uso de aggregate, filter y Q objects del ORM.
    """
    usuario = request.user

    # ORM: queries con aggregate y filter
    tareas = Tarea.objects.filter(usuario=usuario)

    stats = {
        'total':       tareas.count(),
        'pendientes':  tareas.filter(estado='pendiente').count(),
        'en_progreso': tareas.filter(estado='en_progreso').count(),
        'completadas': tareas.filter(estado='completada').count(),
        'alta_prioridad': tareas.filter(prioridad='alta', estado__in=['pendiente', 'en_progreso']).count(),
    }

    # Últimas 5 tareas
    ultimas_tareas = tareas.order_by('-created_at')[:5]

    # Búsqueda con Q objects
    query = request.GET.get('q', '')
    if query:
        ultimas_tareas = tareas.filter(
            Q(titulo__icontains=query) | Q(descripcion__icontains=query)
        )

    context = {
        'stats':         stats,
        'ultimas_tareas': ultimas_tareas,
        'query':         query,
    }
    return render(request, 'dashboard/inicio.html', context)


# ── Lista de Tareas ───────────────────────────────────────────────────────────

@login_required
def tareas_lista_view(request):
    """Lista todas las tareas con filtros por estado y prioridad."""
    tareas = Tarea.objects.filter(usuario=request.user)

    # Filtros por GET
    estado    = request.GET.get('estado', '')
    prioridad = request.GET.get('prioridad', '')
    query     = request.GET.get('q', '')

    if estado:
        tareas = tareas.filter(estado=estado)
    if prioridad:
        tareas = tareas.filter(prioridad=prioridad)
    if query:
        tareas = tareas.filter(
            Q(titulo__icontains=query) | Q(descripcion__icontains=query)
        )

    context = {
        'tareas':    tareas,
        'estado':    estado,
        'prioridad': prioridad,
        'query':     query,
    }
    return render(request, 'dashboard/tareas_lista.html', context)


# ── Crear Tarea ───────────────────────────────────────────────────────────────

@login_required
def tarea_crear_view(request):
    """Crea una nueva tarea asignada al usuario autenticado."""
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user   # Asigna el usuario actual
            tarea.save()
            messages.success(request, f'Tarea "{tarea.titulo}" creada correctamente.')
            return redirect('dashboard:tareas_lista')
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = TareaForm()

    return render(request, 'dashboard/tarea_form.html', {
        'form': form, 'titulo_pagina': 'Nueva Tarea', 'accion': 'Crear',
    })


# ── Editar Tarea ──────────────────────────────────────────────────────────────

@login_required
def tarea_editar_view(request, pk):
    """Edita una tarea existente. Solo permite editar las propias."""
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)

    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            messages.success(request, f'Tarea "{tarea.titulo}" actualizada.')
            return redirect('dashboard:tareas_lista')
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = TareaForm(instance=tarea)

    return render(request, 'dashboard/tarea_form.html', {
        'form': form, 'tarea': tarea,
        'titulo_pagina': 'Editar Tarea', 'accion': 'Guardar cambios',
    })


# ── Eliminar Tarea ────────────────────────────────────────────────────────────

@login_required
def tarea_eliminar_view(request, pk):
    """Elimina una tarea tras confirmación por POST."""
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)

    if request.method == 'POST':
        titulo = tarea.titulo
        tarea.delete()
        messages.success(request, f'Tarea "{titulo}" eliminada.')
        return redirect('dashboard:tareas_lista')

    return render(request, 'dashboard/tarea_confirmar_eliminar.html', {'tarea': tarea})


# ── Completar Tarea (AJAX-friendly) ──────────────────────────────────────────

@login_required
def tarea_completar_view(request, pk):
    """Marca/desmarca una tarea como completada via POST rápido."""
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
    if request.method == 'POST':
        tarea.estado = 'completada' if tarea.estado != 'completada' else 'pendiente'
        tarea.save(update_fields=['estado'])
        estado_txt = 'completada' if tarea.esta_completada else 'pendiente'
        messages.success(request, f'Tarea marcada como {estado_txt}.')
    return redirect('dashboard:tareas_lista')
