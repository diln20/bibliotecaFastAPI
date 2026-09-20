from fastapi import APIRouter, HTTPException, Response, status
from sqlalchemy import func, select

from app import models, schemas
from app.dependencies import DbSession


router = APIRouter(prefix="/programas", tags=["Programas"])


@router.post("", response_model=schemas.ProgramaOut, status_code=status.HTTP_201_CREATED)
def crear_programa(datos: schemas.ProgramaCreate, db: DbSession):
    existe = db.scalar(select(models.Programa).where(models.Programa.nombre == datos.nombre))
    if existe:
        raise HTTPException(status.HTTP_409_CONFLICT, "Ya existe un programa con ese nombre")

    programa = models.Programa(**datos.model_dump())
    db.add(programa)
    db.commit()
    db.refresh(programa)
    return programa


@router.get("", response_model=list[schemas.ProgramaOut])
def listar_programas(db: DbSession):
    stmt = select(models.Programa).order_by(models.Programa.id)
    return list(db.scalars(stmt).all())


@router.get("/{programa_id}", response_model=schemas.ProgramaOut)
def obtener_programa(programa_id: int, db: DbSession):
    programa = db.get(models.Programa, programa_id)
    if not programa:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Programa no encontrado")
    return programa


@router.delete("/{programa_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_programa(programa_id: int, db: DbSession):
    programa = db.get(models.Programa, programa_id)
    if not programa:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Programa no encontrado")

    total = db.scalar(
        select(func.count()).select_from(models.Estudiante).where(
            models.Estudiante.programa_id == programa_id
        )
    )
    if total:
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            "No se puede eliminar: el programa tiene estudiantes asociados",
        )

    db.delete(programa)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
