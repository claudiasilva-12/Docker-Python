#!/usr/bin/env python3
import sys

def main():
    current_tienda = None
    sum_ingreso = 0.0
    count = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            tienda, val_str = line.split('\t')
            ingreso_str, cnt_str = val_str.split(',')
            ingreso = float(ingreso_str)
            cnt = int(cnt_str)
        except ValueError:
            continue

        if current_tienda == tienda:
            sum_ingreso += ingreso
            count += cnt
        else:
            if current_tienda:
                ticket_promedio = sum_ingreso / count
                print(f"{current_tienda}\t{ticket_promedio:.2f}")
            current_tienda = tienda
            sum_ingreso = ingreso
            count = cnt

    if current_tienda == tienda and count > 0:
        ticket_promedio = sum_ingreso / count
        print(f"{current_tienda}\t{ticket_promedio:.2f}")

if __name__ == '__main__':
    main()