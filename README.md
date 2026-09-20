# FastAPI Academy · PostgreSQL + API REST

Biblioteca educativa inspirada en la lógica de aprendizaje progresivo de `bibliotecaDjango`.

## Contenido

- `index.html`: biblioteca interactiva lista para GitHub Pages.
- `proyecto_final/`: API ejecutable de ejemplo con FastAPI + PostgreSQL + SQLAlchemy + Alembic.

## Ruta pedagógica

1. API, HTTP y JSON.
2. Python mínimo y entorno virtual.
3. PostgreSQL y conceptos de base de datos.
4. SQL: DDL, CRUD, claves, relaciones y JOIN.
5. FastAPI: rutas, path/query params y Pydantic.
6. Estructura del proyecto.
7. PostgreSQL desde SQLAlchemy 2.x y psycopg 3.
8. Migraciones con Alembic.
9. CRUD de Programas y Estudiantes.
10. Filtros, paginación, errores HTTP, Swagger, CORS y testing.
11. Proyecto final desde cero.

## Publicar como GitHub Pages

Puedes subir `index.html` a la raíz de un repositorio y configurar Pages para servir la rama principal desde `/ (root)`.

## Ejecutar el proyecto final

Lee `proyecto_final/README.md`.

## Publicación en GitHub Pages

Este repositorio incluye `.github/workflows/pages.yml` para desplegar automáticamente la biblioteca estática desde la rama `main` usando GitHub Actions.

Repositorio previsto: `diln20/bibliotecaFastAPI`
Sitio previsto: `https://diln20.github.io/bibliotecaFastAPI/`

Si GitHub Pages todavía no está habilitado en el repositorio, el workflow omitirá el despliegue sin fallar. Entra a **Settings > Pages** y selecciona **GitHub Actions** como origen de publicación para activar el sitio; a partir de ese momento, el workflow desplegará nuevamente en cada push a `main`.