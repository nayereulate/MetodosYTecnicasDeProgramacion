"""
accounts/models.py
──────────────────
Modelo de usuario personalizado que extiende AbstractUser de Django.
Agrega campos adicionales: bio, avatar y fecha de nacimiento.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """
    Usuario personalizado.
    Extiende AbstractUser para agregar campos extra.
    """
    email = models.EmailField(_('email'), unique=True)
    bio   = models.TextField(_('biografía'), blank=True, max_length=500)
    avatar = models.ImageField(
        _('avatar'),
        upload_to='avatars/',
        blank=True,
        null=True,
        default=None,
    )
    fecha_nacimiento = models.DateField(
        _('fecha de nacimiento'),
        blank=True,
        null=True,
    )
    is_verified = models.BooleanField(_('verificado'), default=False)
    created_at  = models.DateTimeField(_('creado'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('actualizado'), auto_now=True)

    # Usamos email en lugar de username para login
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name        = _('usuario')
        verbose_name_plural = _('usuarios')
        ordering            = ['-created_at']

    def __str__(self):
        return f"{self.get_full_name()} <{self.email}>"

    @property
    def nombre_completo(self):
        return self.get_full_name() or self.username

    @property
    def iniciales(self):
        """Devuelve las iniciales del nombre para el avatar por defecto."""
        partes = self.nombre_completo.split()
        if len(partes) >= 2:
            return f"{partes[0][0]}{partes[1][0]}".upper()
        return self.username[:2].upper()
