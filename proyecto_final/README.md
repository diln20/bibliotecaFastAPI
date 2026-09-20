# API de Estudiantes · FastAPI + PostgreSQL

Proyecto final de la biblioteca educativa. Usa FastAPI, SQLAlchemy 2.x, PostgreSQL, psycopg 3 y Alembic.

## 1. Crear la base

En `psql` o pgAdmin:

```sql
CREATE DATABASE fastapi_estudiantes;
```

## 2. Preparar Python

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## 3. Variables de entorno

Copia `.env.example` como `.env` y coloca tu contraseña real de PostgreSQL.

```env
DATABASE_URL=postgresql+psycopg://postgres:TU_PASSWORD@localhost:5432/fastapi_estudiantes
```

## 4. Crear las tablas con migraciones

```powershell
alembic revision --autogenerate -m "crear programas y estudiantes"
alembic upgrade head
```

## 5. Ejecutar

```powershell
fastapi dev app/main.py
```

Abre:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`
- `http://127.0.0.1:8000/health`

## Endpoints principales

| Método | Ruta | Acción |
|---|---|---|
| POST | `/programas` | Crear programa |
| GET | `/programas` | Listar programas |
| GET | `/programas/{id}` | Consultar programa |
| DELETE | `/programas/{id}` | Eliminar programa si no tiene estudiantes |
| POST | `/estudiantes` | Crear estudiante |
| GET | `/estudiantes` | Listar, filtrar y paginar |
| GET | `/estudiantes/{id}` | Consultar estudiante y programa |
| PATCH | `/estudiantes/{id}` | Actualizar parcialmente |
| DELETE | `/estudiantes/{id}` | Eliminar estudiante |

## Filtros de estudiantes

Ejemplo:

```text
GET /estudiantes?activo=true&programa_id=1&buscar=ana&edad_minima=18&limit=20
```

## Pruebas básicas

```powershell
pytest -q
```

Las pruebas incluidas verifican las rutas que no requieren consultar la base. Para CRUD conviene crear una base separada de testing o sustituir la dependencia `get_db`.
