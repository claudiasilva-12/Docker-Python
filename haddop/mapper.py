#!/usr/bin/env python3
import sys
import csv

def main():
    reader = csv.reader(sys.stdin)
    # Omitir el encabezado
    header = next(reader, None)
    
    for row in reader:
        if not row or len(row) < 8:
            continue
        
        # Columnas: id, fecha_hora, tienda, categoria, producto, cantidad, precio_unitario, metodo_pago
        tienda = row[2]
        try:
            cantidad = float(row[5])
            precio = float(row[6])
            ingreso = cantidad * precio
            # Imprimimos: tienda \t ingreso,1
            print(f"{tienda}\t{ingreso:.2f},1")
        except ValueError:
            continue

if __name__ == '__main__':
    main()