import os

os.environ.setdefault(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:postgres@localhost:5432/fastapi_estudiantes",
)

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_inicio():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["mensaje"] == "API funcionando"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
