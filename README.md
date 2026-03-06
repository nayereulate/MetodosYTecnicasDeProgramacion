# 🚀 Mi App Django — Guía de Instalación

## Estructura del Proyecto

```
mi_app_django/
│
├── django_project/          # Configuración principal
│   ├── settings.py          # Ajustes globales
│   ├── urls.py              # Rutas raíz
│   └── wsgi.py
│
├── accounts/                # App de autenticación
│   ├── models.py            # CustomUser (extiende AbstractUser)
│   ├── forms.py             # Registro, Login, Perfil, Contraseña
│   ├── views.py             # registro, login, logout, perfil
│   ├── urls.py
│   ├── admin.py
│   └── templates/accounts/
│       ├── login.html
│       ├── registro.html
│       ├── perfil.html
│       └── cambiar_contrasena.html
│
├── dashboard/               # App del panel principal
│   ├── models.py            # Modelo Tarea
│   ├── forms.py             # TareaForm
│   ├── views.py             # CRUD completo de tareas
│   ├── urls.py
│   ├── admin.py
│   └── templates/dashboard/
│       ├── inicio.html
│       ├── tareas_lista.html
│       ├── tarea_form.html
│       └── tarea_confirmar_eliminar.html
│
├── core/                    # App base / redirección home
│   ├── views.py
│   └── urls.py
│
├── templates/               # Templates globales
│   ├── base.html
│   └── base_dashboard.html
│
├── static/
│   └── css/
│       └── main.css
│
├── manage.py
└── requirements.txt
```

## ⚡ Instalación Rápida

```bash
# 1. Clonar / descomprimir el proyecto
cd mi_app_django

# 2. Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# 5. Crear superusuario (admin)
python manage.py createsuperuser

# 6. Correr el servidor
python manage.py runserver
```

Abre: **http://127.0.0.1:8000**

## 🔑 Funcionalidades

| Feature | Ruta |
|---|---|
| Login (email + contraseña) | `/accounts/login/` |
| Registro con validación fuerte | `/accounts/registro/` |
| Perfil editable | `/accounts/perfil/` |
| Cambiar contraseña | `/accounts/cambiar-contrasena/` |
| Dashboard con estadísticas | `/dashboard/` |
| CRUD de tareas con filtros | `/dashboard/tareas/` |
| Panel de admin | `/admin/` |

## 🛡️ Validaciones implementadas

- Contraseña: mínimo 8 caracteres, mayúscula, número y símbolo especial
- Email único por usuario
- Username: solo alfanumérico y `_` (3-20 caracteres)
- Tareas: solo el dueño puede editar/eliminar (get_object_or_404 con usuario)
- CSRF token en todos los formularios POST
- @login_required en todas las vistas protegidas
