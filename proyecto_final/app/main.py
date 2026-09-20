from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import estudiantes, programas


app = FastAPI(
    title="API de Estudiantes",
    version="1.0.0",
    description="API educativa construida con FastAPI, SQLAlchemy y PostgreSQL.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(programas.router)
app.include_router(estudiantes.router)


@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}


@app.get("/health")
def health():
    return {"status": "ok"}
