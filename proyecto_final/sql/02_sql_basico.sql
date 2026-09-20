-- Ejecutar después de conectarte a fastapi_estudiantes.
-- Estas sentencias son para practicar SQL antes de usar el ORM.

CREATE TABLE programas_demo (
    id BIGSERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE estudiantes_demo (
    id BIGSERIAL PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    email VARCHAR(180) NOT NULL UNIQUE,
    edad INTEGER CHECK (edad IS NULL OR edad >= 0),
    activo BOOLEAN NOT NULL DEFAULT TRUE,
    programa_id BIGINT NOT NULL REFERENCES programas_demo(id) ON DELETE RESTRICT
);

INSERT INTO programas_demo (nombre) VALUES ('Ingeniería de Sistemas');
INSERT INTO estudiantes_demo (nombre, email, edad, programa_id)
VALUES ('Ana Torres', 'ana@example.com', 20, 1);

SELECT e.id, e.nombre, e.email, p.nombre AS programa
FROM estudiantes_demo e
INNER JOIN programas_demo p ON p.id = e.programa_id;
