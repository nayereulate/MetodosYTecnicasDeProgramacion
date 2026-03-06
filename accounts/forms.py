"""
accounts/forms.py
─────────────────
Formularios para registro, login, perfil y cambio de contraseña.
Usa las validaciones nativas de Django y validaciones personalizadas.
"""

import re
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
    SetPasswordForm,
)
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


# ── Validadores personalizados ────────────────────────────────────────────────

def validar_contrasena_fuerte(value):
    """
    Valida que la contraseña tenga:
      - Al menos 8 caracteres
      - Al menos una mayúscula
      - Al menos un número
      - Al menos un carácter especial
    """
    if len(value) < 8:
        raise ValidationError(_('La contraseña debe tener al menos 8 caracteres.'))
    if not re.search(r'[A-Z]', value):
        raise ValidationError(_('La contraseña debe contener al menos una letra mayúscula.'))
    if not re.search(r'\d', value):
        raise ValidationError(_('La contraseña debe contener al menos un número.'))
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
        raise ValidationError(_('La contraseña debe contener al menos un carácter especial.'))


def validar_username(value):
    """Solo letras, números y guiones bajos. 3-20 caracteres."""
    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', value):
        raise ValidationError(
            _('El usuario solo puede contener letras, números y _ (3-20 caracteres).')
        )


# ── Formulario de Registro ────────────────────────────────────────────────────

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(
        label=_('Nombre'),
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Tu nombre',
            'autofocus': True,
        })
    )
    last_name = forms.CharField(
        label=_('Apellido'),
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Tu apellido',
        })
    )
    username = forms.CharField(
        label=_('Usuario'),
        max_length=20,
        validators=[validar_username],
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'nombre_usuario',
        })
    )
    email = forms.EmailField(
        label=_('Correo electrónico'),
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'correo@ejemplo.com',
        })
    )
    password1 = forms.CharField(
        label=_('Contraseña'),
        validators=[validar_contrasena_fuerte],
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': '••••••••',
            'id': 'password1',
        })
    )
    password2 = forms.CharField(
        label=_('Confirmar contraseña'),
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': '••••••••',
            'id': 'password2',
        })
    )
    terminos = forms.BooleanField(
        label=_('Acepto los términos y condiciones'),
        required=True,
        error_messages={'required': _('Debes aceptar los términos y condiciones.')},
    )

    class Meta:
        model  = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email', '').lower()
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError(_('Este correo ya está registrado.'))
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username', '').lower()
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError(_('Este nombre de usuario ya está en uso.'))
        return username

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password1')
        p2 = cleaned.get('password2')
        if p1 and p2 and p1 != p2:
            self.add_error('password2', _('Las contraseñas no coinciden.'))
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email      = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name  = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


# ── Formulario de Login ───────────────────────────────────────────────────────

class LoginForm(forms.Form):
    email = forms.EmailField(
        label=_('Correo electrónico'),
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'correo@ejemplo.com',
            'autofocus': True,
        })
    )
    password = forms.CharField(
        label=_('Contraseña'),
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': '••••••••',
        })
    )
    recordarme = forms.BooleanField(
        label=_('Recordarme'),
        required=False,
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user    = None
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned  = super().clean()
        email    = cleaned.get('email', '').lower()
        password = cleaned.get('password')

        if email and password:
            self.user = authenticate(
                self.request,
                username=email,
                password=password,
            )
            if self.user is None:
                raise ValidationError(_('Correo o contraseña incorrectos.'))
            if not self.user.is_active:
                raise ValidationError(_('Esta cuenta está desactivada.'))
        return cleaned

    def get_user(self):
        return self.user


# ── Formulario de Perfil ──────────────────────────────────────────────────────

class PerfilForm(forms.ModelForm):
    class Meta:
        model  = CustomUser
        fields = ['first_name', 'last_name', 'username', 'bio', 'avatar', 'fecha_nacimiento']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-input', 'placeholder': 'Nombre',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-input', 'placeholder': 'Apellido',
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-input',
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-input', 'rows': 3,
                'placeholder': 'Cuéntanos algo sobre ti...',
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-input-file', 'accept': 'image/*',
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-input', 'type': 'date',
            }),
        }


# ── Formulario de Cambio de Contraseña ────────────────────────────────────────

class CambiarContrasenaForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_('Contraseña actual'),
        widget=forms.PasswordInput(attrs={
            'class': 'form-input', 'placeholder': '••••••••',
        })
    )
    new_password1 = forms.CharField(
        label=_('Nueva contraseña'),
        validators=[validar_contrasena_fuerte],
        widget=forms.PasswordInput(attrs={
            'class': 'form-input', 'placeholder': '••••••••',
        })
    )
    new_password2 = forms.CharField(
        label=_('Confirmar nueva contraseña'),
        widget=forms.PasswordInput(attrs={
            'class': 'form-input', 'placeholder': '••••••••',
        })
    )
