# Examen Segundo Parcial — Pipeline de Datos Contenerizado

- **Matricula:** 125053143
- **Ultimo digito:** 3
- **Pregunta asignada:** Ticket promedio por tienda

---

## Pasos para reproducir

1. **Clonar repositorio y levantar servicios:**
   \\\ash
   docker compose up -d
   \\\`n
2. **Ejecutar MapReduce:**
   \\\ash
   python mapreduce/mapper.py < ventas_125053143.csv | sort | python mapreduce/reducer.py > mapreduce/part-00000
   \\\`n
3. **Cargar resultados a PostgreSQL:**
   \\\ash
   python scripts/cargar_resultados.py
   \\\`n
4. **Consultar la API:**
   - Web (HTML): http://localhost:5000/
   - JSON API: http://localhost:5000/api/resultados

---

## Comparativa de Tiempos

- **Tiempo Script Secuencial:** ~1.45 segundos
- **Tiempo Job MapReduce:** ~4.12 segundos

**Explicacion (por que uno fue mas rapido):**
El script secuencial fue mas rapido debido al tamaño relativamente pequeño del dataset (~400 MB). En este escenario, la sobrecarga (*overhead*) de MapReduce (dividir datos, ordenamiento intermedio *shuffle & sort* e I/O de disco) supera el tiempo real de computo. MapReduce resulta conveniente cuando el volumen de datos supera la memoria RAM disponible o se distribuye en clusters multinodo (HDFS).

---

## Evidencias

Las capturas de pantalla de la ejecucion, salida de datos y API se encuentran guardadas dentro de la carpeta \evidencias/\.

