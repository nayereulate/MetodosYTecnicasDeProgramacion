"""
accounts/admin.py
─────────────────
Configuración del panel de administración para CustomUser.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display  = ['email', 'username', 'get_full_name', 'is_verified', 'is_active', 'created_at']
    list_filter   = ['is_active', 'is_verified', 'is_staff', 'created_at']
    search_fields = ['email', 'username', 'first_name', 'last_name']
    ordering      = ['-created_at']

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Información personal'), {'fields': ('first_name', 'last_name', 'bio', 'avatar', 'fecha_nacimiento')}),
        (_('Permisos'), {'fields': ('is_active', 'is_verified', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Fechas'), {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    readonly_fields = ['created_at', 'updated_at', 'last_login']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
