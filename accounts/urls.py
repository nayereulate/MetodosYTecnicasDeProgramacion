"""
accounts/urls.py
"""

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('registro/',           views.registro_view,          name='registro'),
    path('login/',              views.login_view,              name='login'),
    path('logout/',             views.logout_view,             name='logout'),
    path('perfil/',             views.perfil_view,             name='perfil'),
    path('cambiar-contrasena/', views.cambiar_contrasena_view, name='cambiar_contrasena'),
]
