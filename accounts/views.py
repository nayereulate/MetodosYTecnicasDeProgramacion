"""
accounts/views.py
─────────────────
Vistas para: registro, login, logout, perfil y cambio de contraseña.
Usa login_required, mensajes de Django y redirecciones.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from .forms import RegistroForm, LoginForm, PerfilForm, CambiarContrasenaForm


# ── Registro ──────────────────────────────────────────────────────────────────

def registro_view(request):
    """Crea un nuevo usuario y lo autentica automáticamente."""
    if request.user.is_authenticated:
        return redirect('dashboard:inicio')

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.nombre_completo}! Tu cuenta fue creada.')
            return redirect('dashboard:inicio')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = RegistroForm()

    return render(request, 'accounts/registro.html', {'form': form})


# ── Login ─────────────────────────────────────────────────────────────────────

def login_view(request):
    """Autentica al usuario con email y contraseña."""
    if request.user.is_authenticated:
        return redirect('dashboard:inicio')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # "Recordarme": sesión permanente si está marcado
            if not form.cleaned_data.get('recordarme'):
                request.session.set_expiry(0)   # Cierra al cerrar navegador
            else:
                request.session.set_expiry(1209600)  # 2 semanas

            messages.success(request, f'¡Hola de nuevo, {user.nombre_completo}!')
            next_url = request.GET.get('next', 'dashboard:inicio')
            return redirect(next_url)
        else:
            messages.error(request, 'Correo o contraseña incorrectos.')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


# ── Logout ────────────────────────────────────────────────────────────────────

@login_required
def logout_view(request):
    """Cierra sesión y redirige al login."""
    nombre = request.user.nombre_completo
    logout(request)
    messages.info(request, f'Hasta luego, {nombre}. ¡Sesión cerrada correctamente!')
    return redirect('accounts:login')


# ── Perfil ────────────────────────────────────────────────────────────────────

@login_required
def perfil_view(request):
    """Muestra y actualiza el perfil del usuario autenticado."""
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('accounts:perfil')
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = PerfilForm(instance=request.user)

    return render(request, 'accounts/perfil.html', {'form': form})


# ── Cambiar Contraseña ────────────────────────────────────────────────────────

@login_required
def cambiar_contrasena_view(request):
    """Permite al usuario cambiar su contraseña manteniendo la sesión activa."""
    if request.method == 'POST':
        form = CambiarContrasenaForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Actualiza el hash de sesión para no cerrar sesión
            update_session_auth_hash(request, user)
            messages.success(request, '¡Contraseña cambiada correctamente!')
            return redirect('accounts:perfil')
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = CambiarContrasenaForm(request.user)

    return render(request, 'accounts/cambiar_contrasena.html', {'form': form})
