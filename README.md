# 🚀 Métodos y Técnicas de Programación: Python & Django

<div align="center">

[![Python Version](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-F7DF1E?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Regex](https://img.shields.io/badge/Regex-Supported-E34F26?style=for-the-badge)](https://docs.python.org/3/library/re.html)
[![Status](https://img.shields.io/badge/Status-Active-00C851?style=for-the-badge)]()

<br/>

> **Documentación técnica completa** sobre desarrollo con Python, el framework Django y el uso de Expresiones Regulares.  
> Materiales de la asignatura *Métodos y Técnicas de Programación*.

<br/>

[📖 Ver Documentación](#-tabla-de-contenidos) · [🐛 Reportar Error](https://github.com/) · [💡 Sugerir Mejora](https://github.com/)

</div>

---

## 📑 Tabla de Contenidos

- [📌 Acerca del Proyecto](#-acerca-del-proyecto)
- [🐍 Introducción a Python](#-introducción-a-python)
  - [Historia y Filosofía](#historia-y-filosofía)
  - [Tipos de Datos](#tipos-de-datos)
  - [Control de Flujo](#control-de-flujo)
  - [Funciones](#funciones)
  - [Listas y Colecciones](#listas-y-colecciones)
- [💻 Entorno de Desarrollo](#-entorno-de-desarrollo)
  - [Requisitos Previos](#requisitos-previos)
  - [Entornos Virtuales (venv)](#entornos-virtuales-venv)
- [🎸 Framework Django](#-framework-django)
  - [Arquitectura MVT](#arquitectura-mvt)
  - [Estructura del Proyecto](#estructura-del-proyecto)
  - [Modelos y ORM](#modelos-y-orm)
  - [Vistas y URLs](#vistas-y-urls)
  - [Templates](#templates)
- [🔍 Expresiones Regulares](#-expresiones-regulares-regex)
  - [Sintaxis Básica](#sintaxis-básica)
  - [Módulo re en Python](#módulo-re-en-python)
- [🛠️ Instalación](#️-instalación)
- [👤 Autor](#-autor)

---

## 📌 Acerca del Proyecto

Este repositorio centraliza los fundamentos teóricos y prácticos de la asignatura. Cubre tres ejes principales:

| Módulo | Descripción | Nivel |
|---|---|---|
| 🐍 **Python** | Sintaxis, estructuras de datos, funciones y POO | Básico → Intermedio |
| 🎸 **Django** | Framework web MVT, ORM, rutas y templates | Intermedio |
| 🔍 **Regex** | Patrones de búsqueda y procesamiento de texto | Básico → Avanzado |

---

## 🐍 Introducción a Python

### Historia y Filosofía

Python fue creado a finales de los 80 y publicado en 1991 por **Guido van Rossum**. Su nombre está inspirado en el grupo cómico británico *Monty Python's Flying Circus*. Es reconocido mundialmente por su sintaxis limpia y legible.

> *"Readability counts."* — The Zen of Python (`import this`)

**Características principales:**
- ✅ Sintaxis simple y legible
- ✅ Tipado dinámico
- ✅ Multiplataforma
- ✅ Gran ecosistema de librerías (PyPI)
- ✅ Comunidad masiva y activa

---

### Tipos de Datos

```python
# Tipos primitivos
entero     = 42           # int
decimal    = 3.14         # float
texto      = "Python"     # str
booleano   = True         # bool
nulo       = None         # NoneType

# Colecciones
lista      = [1, 2, 3]            # list  — mutable, ordenada
tupla      = (1, 2, 3)            # tuple — inmutable, ordenada
conjunto   = {1, 2, 3}            # set   — mutable, sin duplicados
diccion    = {"clave": "valor"}   # dict  — clave:valor

# Verificar tipo
print(type(entero))   # <class 'int'>
```

---

### Control de Flujo

```python
# ── if / elif / else ──────────────────────────────────────
nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")


# ── Ciclo for ─────────────────────────────────────────────
lenguajes = ["Python", "JavaScript", "Go"]

for lang in lenguajes:
    print(f"  → {lang}")


# ── Ciclo while ───────────────────────────────────────────
contador = 0

while contador < 3:
    print(f"Iteración {contador}")
    contador += 1


# ── Comprensión de listas (Pythonic) ─────────────────────
cuadrados = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]
```

---

### Funciones

```python
# ── Función básica ────────────────────────────────────────
def saludar(nombre):
    return f"Hola, {nombre}!"


# ── Parámetros por defecto ────────────────────────────────
def potencia(base, exponente=2):
    return base ** exponente

print(potencia(3))     # 9
print(potencia(3, 3))  # 27


# ── *args y **kwargs ──────────────────────────────────────
def sumar(*numeros):
    return sum(numeros)

print(sumar(1, 2, 3, 4))  # 10


# ── Lambda (función anónima) ──────────────────────────────
doble = lambda x: x * 2
print(doble(5))  # 10


# ── Entrada del usuario ───────────────────────────────────
nombre = input("Ingresa tu nombre: ")
print(saludar(nombre))
```

---

### Listas y Colecciones

```python
frutas = ["manzana", "banana", "cereza"]

# Operaciones comunes
frutas.append("durazno")       # Agregar al final
frutas.insert(1, "mango")      # Insertar en posición
frutas.remove("banana")        # Eliminar por valor
frutas.sort()                  # Ordenar
print(frutas[0])               # Acceso por índice
print(frutas[-1])              # Último elemento
print(frutas[1:3])             # Slicing

# Diccionario
estudiante = {
    "nombre": "Nayer",
    "carrera": "Ingeniería",
    "promedio": 9.2
}

for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")
```

---

## 💻 Entorno de Desarrollo

### Requisitos Previos

| Herramienta | Versión mínima | Descarga |
|---|---|---|
| Python | 3.8+ | [python.org](https://www.python.org/downloads/) |
| pip | Incluido con Python | — |
| Git | Cualquiera | [git-scm.com](https://git-scm.com/) |
| VS Code *(recomendado)* | Cualquiera | [code.visualstudio.com](https://code.visualstudio.com/) |

---

### Entornos Virtuales (venv)

Un **entorno virtual** es un directorio aislado que contiene una instalación de Python independiente con sus propios paquetes. Permite trabajar en múltiples proyectos con diferentes dependencias sin conflictos.

```
Sistema Global
│
├── Python 3.x
│
├── proyecto_a/
│   └── venv/  ← Django 3.2, requests 2.26
│
└── proyecto_b/
    └── venv/  ← Django 4.2, requests 2.31
```

**Comandos — Windows:**

```bash
# Crear entorno virtual
python -m venv venv

# Activar
venv\Scripts\activate

# Verificar activación (verás el prefijo)
(venv) C:\mi_proyecto>

# Instalar paquetes
pip install nombre_paquete

# Guardar dependencias
pip freeze > requirements.txt

# Instalar desde requirements
pip install -r requirements.txt

# Desactivar
deactivate
```

**Comandos — macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
deactivate
```

---

## 🎸 Framework Django

Django es un framework web de alto nivel escrito en Python que permite el desarrollo **rápido, seguro y mantenible** de aplicaciones web. Sigue el principio **DRY** *(Don't Repeat Yourself)*.

---

### Arquitectura MVT

Django implementa el patrón **MVT** (Model – View – Template), una variación del clásico MVC:

```
  Cliente (Browser)
        │
        │  HTTP Request
        ▼
  ┌─────────────┐
  │   urls.py   │  ← Enrutador: decide qué View ejecutar
  └──────┬──────┘
         │
         ▼
  ┌─────────────┐       ┌─────────────┐
  │    VIEW     │ ◄───► │    MODEL    │  ← ORM / Base de Datos
  │  views.py   │       │  models.py  │
  └──────┬──────┘       └─────────────┘
         │
         ▼
  ┌─────────────┐
  │  TEMPLATE   │  ← HTML renderizado
  │  .html      │
  └──────┬──────┘
         │
         │  HTTP Response
         ▼
  Cliente (Browser)
```

| Capa | Archivo | Responsabilidad |
|---|---|---|
| **Model** | `models.py` | Estructura de datos, lógica de negocio, ORM |
| **View** | `views.py` | Procesa requests, llama modelos, retorna respuestas |
| **Template** | `*.html` | Presentación visual — HTML dinámico |
| **URL Dispatcher** | `urls.py` | Mapea URLs a sus respectivas vistas |

---

### Estructura del Proyecto

```bash
django-admin startproject mysite
cd mysite
python manage.py startapp blog
```

```
mysite/                          ← Directorio raíz
│
├── manage.py                    # CLI: runserver, migrate, createsuperuser...
│
├── mysite/                      # Paquete de configuración
│   ├── __init__.py
│   ├── settings.py              # Configuración global (BD, apps, static...)
│   ├── urls.py                  # Enrutador principal
│   ├── wsgi.py                  # Servidor WSGI (producción)
│   └── asgi.py                  # Servidor ASGI (async/websockets)
│
└── blog/                        # App creada con startapp
    ├── migrations/              # Historial de cambios en BD
    │   └── __init__.py
    ├── __init__.py
    ├── admin.py                 # Panel de administración
    ├── apps.py                  # Configuración de la app
    ├── models.py                # Modelos / tablas de BD
    ├── tests.py                 # Tests unitarios
    ├── urls.py                  # Rutas de la app
    └── views.py                 # Lógica de las vistas
```

---

### Modelos y ORM

```python
# blog/models.py
from django.db import models
from django.utils import timezone

class Articulo(models.Model):
    titulo     = models.CharField(max_length=200)
    contenido  = models.TextField()
    autor      = models.CharField(max_length=100)
    publicado  = models.DateTimeField(default=timezone.now)
    activo     = models.BooleanField(default=True)

    class Meta:
        ordering = ["-publicado"]  # Más reciente primero

    def __str__(self):
        return self.titulo


# ── Migraciones ───────────────────────────────────────────
# python manage.py makemigrations
# python manage.py migrate


# ── Queries con el ORM ────────────────────────────────────
todos       = Articulo.objects.all()
activos     = Articulo.objects.filter(activo=True)
primero     = Articulo.objects.get(id=1)
ordenados   = Articulo.objects.order_by("titulo")
nuevo       = Articulo.objects.create(titulo="Hola", contenido="...", autor="Nayer")
```

---

### Vistas y URLs

```python
# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Articulo

def lista_articulos(request):
    articulos = Articulo.objects.filter(activo=True)
    return render(request, "blog/lista.html", {"articulos": articulos})

def detalle_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    return render(request, "blog/detalle.html", {"articulo": articulo})
```

```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("",          views.lista_articulos,   name="lista"),
    path("<int:pk>/", views.detalle_articulo,  name="detalle"),
]
```

```python
# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/",  include("blog.urls")),
]
```

---

### Templates

```html
<!-- blog/templates/blog/lista.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <title>Blog</title>
</head>
<body>
    <h1>Artículos</h1>

    {% for articulo in articulos %}
        <article>
            <h2>{{ articulo.titulo }}</h2>
            <p>{{ articulo.contenido|truncatewords:30 }}</p>
            <a href="{% url 'detalle' articulo.pk %}">Leer más →</a>
        </article>
    {% empty %}
        <p>No hay artículos disponibles.</p>
    {% endfor %}
</body>
</html>
```

**Tags y filtros más usados:**

| Sintaxis | Tipo | Uso |
|---|---|---|
| `{{ variable }}` | Variable | Muestra el valor de una variable |
| `{% tag %}` | Tag | Lógica: `for`, `if`, `block`, `url` |
| `{{ var\|filtro }}` | Filtro | Transforma: `upper`, `truncatewords`, `date` |
| `{% extends "base.html" %}` | Herencia | Extiende un template base |
| `{% block nombre %}` | Bloque | Define sección sobreescribible |

---

## 🔍 Expresiones Regulares (Regex)

Las expresiones regulares definen un **patrón de búsqueda** sobre cadenas de texto. Son una herramienta fundamental para validar, buscar y transformar datos.

---

### Sintaxis Básica

**Metacaracteres:**

| Símbolo | Descripción | Ejemplo | Coincide con |
|---|---|---|---|
| `.` | Cualquier carácter (excepto `\n`) | `a.c` | "abc", "axc" |
| `^` | Inicio de cadena | `^Hola` | "Hola mundo" |
| `$` | Final de cadena | `mundo$` | "Hola mundo" |
| `*` | 0 o más repeticiones | `ab*` | "a", "ab", "abb" |
| `+` | 1 o más repeticiones | `ab+` | "ab", "abb" |
| `?` | 0 o 1 (opcional) | `colou?r` | "color", "colour" |
| `{n}` | Exactamente n veces | `\d{4}` | "2026" |
| `{n,m}` | Entre n y m veces | `\d{2,4}` | "42", "2026" |
| `\|` | Alternativa (OR) | `gato\|perro` | "gato", "perro" |

**Clases de caracteres:**

| Símbolo | Descripción | Equivalente |
|---|---|---|
| `\d` | Dígito | `[0-9]` |
| `\D` | No dígito | `[^0-9]` |
| `\w` | Alfanumérico o `_` | `[a-zA-Z0-9_]` |
| `\W` | No alfanumérico | `[^a-zA-Z0-9_]` |
| `\s` | Espacio en blanco | `[ \t\n\r]` |
| `\S` | No espacio | `[^ \t\n\r]` |
| `[abc]` | a, b o c | — |
| `[^abc]` | Nada de a, b, c | — |
| `[a-z]` | Rango de a a z | — |

---

### Módulo re en Python

```python
import re

texto = "Contacto: nayer@dev.com — Tel: 591-77889900"

# ── re.search() — Primera coincidencia ───────────────────
match = re.search(r"\d+", texto)
if match:
    print(match.group())    # "591"
    print(match.start())    # posición inicial
    print(match.end())      # posición final


# ── re.findall() — Todas las coincidencias ────────────────
numeros = re.findall(r"\d+", texto)
print(numeros)              # ['591', '77889900']


# ── re.match() — Solo al inicio de la cadena ─────────────
result = re.match(r"Contacto", texto)
print(bool(result))         # True


# ── re.sub() — Reemplazar coincidencias ──────────────────
limpio = re.sub(r"\d", "*", texto)
print(limpio)               # "Contacto: nayer@dev.com — Tel: ***-********"


# ── re.split() — Dividir por patrón ──────────────────────
partes = re.split(r"[—\-]", texto)
print(partes)


# ── Grupos de captura ─────────────────────────────────────
patron_email = r"([\w.-]+)@([\w.-]+)\.(\w+)"
m = re.search(patron_email, texto)
if m:
    print(m.group(0))   # email completo: nayer@dev.com
    print(m.group(1))   # usuario:        nayer
    print(m.group(2))   # dominio:        dev
    print(m.group(3))   # extensión:      com


# ── Flags útiles ──────────────────────────────────────────
# re.IGNORECASE  →  ignora mayúsculas/minúsculas
# re.MULTILINE   →  ^ y $ aplican a cada línea
# re.DOTALL      →  . también coincide con \n

resultado = re.findall(r"[a-z]+", texto, re.IGNORECASE)
```

---

## 🛠️ Instalación

### Setup Completo Paso a Paso

**Paso 1 — Instalar Python**

Descarga desde [python.org](https://www.python.org/downloads/) y marca ✅ *"Add Python to PATH"* durante la instalación.

```bash
python --version
# Python 3.x.x
```

**Paso 2 — Verificar pip**

```bash
pip --version
# pip xx.x.x from ...
```

**Paso 3 — Clonar o crear el proyecto**

```bash
# Opción A: clonar repositorio existente
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo

# Opción B: crear proyecto nuevo
mkdir mi_proyecto
cd mi_proyecto
```

**Paso 4 — Crear y activar entorno virtual**

```bash
# Crear
python -m venv venv

# Activar (Windows)
venv\Scripts\activate

# Activar (macOS/Linux)
source venv/bin/activate
```

**Paso 5 — Instalar dependencias**

```bash
pip install django
pip install -r requirements.txt   # si existe el archivo
```

**Paso 6 — Crear proyecto Django**

```bash
django-admin startproject mysite .
python manage.py startapp mi_app
```

**Paso 7 — Migraciones iniciales y servidor**

```bash
python manage.py migrate
python manage.py createsuperuser   # opcional: panel admin
python manage.py runserver
```

Abre tu navegador en: **http://127.0.0.1:8000** 🎉

---

### Comandos de Referencia Rápida

```bash
# Django
python manage.py runserver          # Inicia servidor de desarrollo
python manage.py makemigrations     # Genera migraciones
python manage.py migrate            # Aplica migraciones
python manage.py createsuperuser    # Crea usuario administrador
python manage.py shell              # Abre consola interactiva Django
python manage.py collectstatic      # Recolecta archivos estáticos
python manage.py startapp nombre    # Crea nueva aplicación

# pip
pip install paquete                 # Instalar paquete
pip uninstall paquete               # Desinstalar paquete
pip list                            # Listar paquetes instalados
pip freeze > requirements.txt       # Exportar dependencias
pip install -r requirements.txt     # Instalar desde archivo
```

---

## 👤 Autor

<div align="center">

**Nayer | Dev**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![TikTok](https://img.shields.io/badge/TikTok-000000?style=for-the-badge&logo=tiktok&logoColor=white)](https://tiktok.com/)

*MIT License © 2026 — Métodos y Técnicas de Programación*

</div>
```
