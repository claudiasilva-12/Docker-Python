import psycopg2, os

def cargar():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '5432'),
        dbname=os.getenv('DB_NAME', 'datamart'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'postgrespassword')
    )
    cur = conn.cursor()

    # Crear tabla si no existe
    cur.execute('''
        CREATE TABLE IF NOT EXISTS resultados_ticket_promedio (
            tienda VARCHAR(50) PRIMARY KEY,
            ticket_promedio NUMERIC(10, 2)
        );
    ''')

    # Leer archivo part-00000 generado por MapReduce
    archivo_salida = 'mapreduce/part-00000'
    if os.path.exists(archivo_salida):
        with open(archivo_salida, 'r') as f:
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    tienda, ticket = parts[0], float(parts[1])
                    cur.execute('''
                        INSERT INTO resultados_ticket_promedio (tienda, ticket_promedio)
                        VALUES (%s, %s)
                        ON CONFLICT (tienda) DO UPDATE SET ticket_promedio = EXCLUDED.ticket_promedio;
                    ''', (tienda, ticket))
        conn.commit()
        print('¡Resultados cargados exitosamente a PostgreSQL!')
    else:
        print(f'No se encontro el archivo {archivo_salida}')

    cur.close()
    conn.close()

if __name__ == '__main__':
    cargar()

