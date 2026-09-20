from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ProgramaCreate(BaseModel):
    nombre: str = Field(min_length=2, max_length=100)


class ProgramaOut(ProgramaCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)


class EstudianteCreate(BaseModel):
    nombre: str = Field(min_length=2, max_length=120)
    email: EmailStr
    edad: int | None = Field(default=None, ge=0, le=120)
    programa_id: int
    activo: bool = True


class EstudianteUpdate(BaseModel):
    nombre: str | None = Field(default=None, min_length=2, max_length=120)
    email: EmailStr | None = None
    edad: int | None = Field(default=None, ge=0, le=120)
    programa_id: int | None = None
    activo: bool | None = None


class EstudianteOut(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    edad: int | None
    programa_id: int
    activo: bool
    model_config = ConfigDict(from_attributes=True)


class EstudianteDetalle(EstudianteOut):
    programa: ProgramaOut
