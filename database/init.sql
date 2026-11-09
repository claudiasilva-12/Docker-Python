CREATE TABLE IF NOT EXISTS resultados_ticket_promedio (
    id SERIAL PRIMARY KEY,
    tienda VARCHAR(50) NOT NULL,
    ticket_promedio NUMERIC(12, 2) NOT NULL,
    fecha_procesamiento TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
