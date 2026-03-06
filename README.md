# 🚀 Métodos y Técnicas de Programación: Python & Django

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-4.x-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Regex](https://img.shields.io/badge/regex-supported-orange.svg)](#-expresiones-regulares-regex)

> Documentación técnica de desarrollo web moderno: fundamentos de Python, framework Django y Expresiones Regulares.

---

## 📑 Tabla de Contenidos
1. [Introducción a Python](#-introducción-a-python)
2. [Entorno de Desarrollo](#-entorno-de-desarrollo)
3. [Framework Django](#-framework-django)
4. [Expresiones Regulares (Regex)](#-expresiones-regulares-regex)
5. [Instalación](#-instalación)

---

## 🐍 Introducción a Python

Python es un lenguaje de programación creado en los años 90 por **Guido van Rossum**. Su nombre está inspirado en el grupo cómico británico *Monty Python*. Hoy es uno de los lenguajes más populares del mundo por su claridad y versatilidad.

### Conceptos Clave

| Concepto | Descripción |
|---|---|
| **Funciones** | Se definen con la palabra reservada `def` |
| **Control de Flujo** | Sentencias `if-elif-else`, ciclos `while` y `for` |
| **Entrada / Salida** | Captura con `input()`, visualización con `print()` |
```python
# Ejemplo básico de función en Python
def saludar(nombre):
    print(f"Hola, {nombre}! Bienvenido a Python.")

nombre = input("Ingresa tu nombre: ")
saludar(nombre)
```

---

## 💻 Entorno de Desarrollo

Para un desarrollo limpio y reproducible se utilizan **entornos virtuales (`venv`)**: espacios aislados que permiten instalar distintas versiones de paquetes sin interferir con el sistema global.

> 💡 **¿Por qué usarlo?** Evita conflictos de versiones entre proyectos. Cada proyecto tiene su propio entorno limpio y aislado.
```bash
# 1. Crear el entorno virtual
python -m venv nombre_entorno

# 2. Activar el entorno (Windows)
nombre_entorno\Scripts\activate

# 3. Desactivar cuando termines
deactivate
```

---

## 🎸 Framework Django

Django es un framework web de alto nivel escrito en Python que permite el desarrollo **rápido, seguro y mantenible** de aplicaciones web. Sigue el principio **DRY** *(Don't Repeat Yourself)* y una arquitectura **MVT**.

### Arquitectura MVT
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    MODEL    │ ──► │    VIEW     │ ──► │  TEMPLATE   │
│  Datos/ORM  │     │ Lógica HTTP │     │ HTML Visual │
└─────────────┘     └─────────────┘     └─────────────┘
```

| Capa | Responsabilidad |
|---|---|
| **Models** | Definen la estructura de datos y gestionan la BD vía ORM |
| **Views** | Gestionan peticiones HTTP y devuelven respuestas |
| **Templates** | Ficheros HTML que definen la estructura visual |

### Estructura del Proyecto

Al ejecutar `django-admin startproject mysite`:
```
mysite/
├── manage.py         # Utilidad CLI del proyecto
└── mysite/
    ├── settings.py   # Configuración global
    ├── urls.py       # Mapeador de rutas URL
    ├── wsgi.py       # Punto de entrada WSGI
    └── asgi.py       # Punto de entrada ASGI (async)
```

---

## 🔍 Expresiones Regulares (Regex)

Las expresiones regulares definen un **patrón de búsqueda** para cadenas de caracteres. Son fundamentales para validar, buscar y transformar texto.

### Símbolos Comunes

| Símbolo | Descripción | Ejemplo |
|---|---|---|
| `.` | Cualquier carácter | `a.c` → "abc", "axc" |
| `^` | Inicio de cadena | `^Hola` → "Hola mundo" |
| `$` | Final de cadena | `mundo$` → "Hola mundo" |
| `\d` | Dígito `[0-9]` | `\d+` → "42", "2026" |
| `\w` | Alfanumérico o `_` | `\w+` → "python_3" |
| `+` | 1 o más repeticiones | `a+` → "a", "aaa" |
| `*` | 0 o más repeticiones | `ab*` → "a", "ab" |
| `?` | 0 o 1 (opcional) | `colou?r` → "color" |
| `[ ]` | Clase de caracteres | `[aeiou]` → vocales |
```python
import re

# Buscar un patrón en un texto
texto = "Mi email es nayer@dev.com"
patron = r"[\w.-]+@[\w.-]+\.\w+"

resultado = re.search(patron, texto)
if resultado:
    print(f"Email encontrado: {resultado.group()}")
```

---

## 🛠️ Instalación

Sigue estos pasos para configurar tu entorno de trabajo desde cero.

**1. Instalar Python**
Descarga desde [python.org](https://www.python.org/) y verifica:
```bash
python --version
```

**2. Verificar PIP**
```bash
pip --version
```

**3. Crear y activar entorno virtual**
```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # macOS/Linux
```

**4. Instalar Django**
```bash
pip install django
django-admin --version
```

**5. Crear y correr el proyecto**
```bash
django-admin startproject mysite .
python manage.py runserver
```

---

## 👤 Autor

**Nayer | Dev** — MIT License © 2025
