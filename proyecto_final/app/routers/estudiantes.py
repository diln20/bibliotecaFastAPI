from fastapi import APIRouter, HTTPException, Query, Response, status
from sqlalchemy import select

from app import models, schemas
from app.dependencies import DbSession


router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])


def _validar_programa(db: DbSession, programa_id: int) -> None:
    if not db.get(models.Programa, programa_id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Programa no encontrado")


def _email_en_uso(db: DbSession, email: str, ignorar_id: int | None = None) -> bool:
    stmt = select(models.Estudiante).where(models.Estudiante.email == email)
    if ignorar_id is not None:
        stmt = stmt.where(models.Estudiante.id != ignorar_id)
    return db.scalar(stmt) is not None


@router.post("", response_model=schemas.EstudianteOut, status_code=status.HTTP_201_CREATED)
def crear_estudiante(datos: schemas.EstudianteCreate, db: DbSession):
    _validar_programa(db, datos.programa_id)
    if _email_en_uso(db, str(datos.email)):
        raise HTTPException(status.HTTP_409_CONFLICT, "El email ya está registrado")

    estudiante = models.Estudiante(**datos.model_dump())
    db.add(estudiante)
    db.commit()
    db.refresh(estudiante)
    return estudiante


@router.get("", response_model=list[schemas.EstudianteOut])
def listar_estudiantes(
    db: DbSession,
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    activo: bool | None = None,
    programa_id: int | None = None,
    buscar: str | None = None,
    edad_minima: int | None = Query(default=None, ge=0, le=120),
):
    stmt = select(models.Estudiante)

    if activo is not None:
        stmt = stmt.where(models.Estudiante.activo == activo)
    if programa_id is not None:
        stmt = stmt.where(models.Estudiante.programa_id == programa_id)
    if buscar:
        stmt = stmt.where(models.Estudiante.nombre.ilike(f"%{buscar}%"))
    if edad_minima is not None:
        stmt = stmt.where(models.Estudiante.edad >= edad_minima)

    stmt = stmt.order_by(models.Estudiante.id).offset(skip).limit(limit)
    return list(db.scalars(stmt).all())


@router.get("/{estudiante_id}", response_model=schemas.EstudianteDetalle)
def obtener_estudiante(estudiante_id: int, db: DbSession):
    estudiante = db.get(models.Estudiante, estudiante_id)
    if not estudiante:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Estudiante no encontrado")
    return estudiante


@router.patch("/{estudiante_id}", response_model=schemas.EstudianteOut)
def actualizar_estudiante(
    estudiante_id: int,
    datos: schemas.EstudianteUpdate,
    db: DbSession,
):
    estudiante = db.get(models.Estudiante, estudiante_id)
    if not estudiante:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Estudiante no encontrado")

    cambios = datos.model_dump(exclude_unset=True)

    if "programa_id" in cambios:
        _validar_programa(db, cambios["programa_id"])
    if "email" in cambios and _email_en_uso(db, str(cambios["email"]), estudiante_id):
        raise HTTPException(status.HTTP_409_CONFLICT, "El email ya está registrado")

    for campo, valor in cambios.items():
        setattr(estudiante, campo, valor)

    db.commit()
    db.refresh(estudiante)
    return estudiante


@router.delete("/{estudiante_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_estudiante(estudiante_id: int, db: DbSession):
    estudiante = db.get(models.Estudiante, estudiante_id)
    if not estudiante:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Estudiante no encontrado")

    db.delete(estudiante)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
