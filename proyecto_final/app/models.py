from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Programa(Base):
    __tablename__ = "programas"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)

    estudiantes: Mapped[list["Estudiante"]] = relationship(back_populates="programa")


class Estudiante(Base):
    __tablename__ = "estudiantes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(180), unique=True, index=True, nullable=False)
    edad: Mapped[int | None] = mapped_column(nullable=True)
    activo: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    programa_id: Mapped[int] = mapped_column(
        ForeignKey("programas.id", ondelete="RESTRICT"), index=True, nullable=False
    )

    programa: Mapped[Programa] = relationship(back_populates="estudiantes")
