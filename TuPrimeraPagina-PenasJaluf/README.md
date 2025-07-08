# TuPrimeraPagina - Penas Jaluf

Este es un blog básico en Django creado como parte de la consigna de práctica del patrón MVT.

## 🔧 Requisitos del proyecto

- 3 modelos: Autor, Categoría, Artículo.
- Formularios para crear cada modelo.
- Formulario de búsqueda de artículos por título.
- Herencia de plantillas.
- Patrón MVT.

## 📋 Funcionalidades

1. **Inicio**: `/`
2. **Crear Autor**: `/crear_autor/`
3. **Crear Categoría**: `/crear_categoria/`
4. **Crear Artículo**: `/crear_articulo/`
5. **Buscar Artículo**: `/buscar_articulo/`

## 🧪 Orden sugerido de pruebas

1. Crear al menos un autor.
2. Crear una categoría.
3. Crear un artículo seleccionando el autor y categoría.
4. Buscar el artículo creado usando parte del título.

## ⚙️ Cómo correr el proyecto

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
