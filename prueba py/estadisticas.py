import globales
import math

def producto_mayor_valor():
    ventas = globales.leer_archivo_json("ventas.json")
    ordenar_ventas = sorted(ventas, key= lambda x:x ["valor"], reverse=True)
    print("|producto\t|\tvalor\t|\tiva\t|")
    for valor in ordenar_ventas [:1]:
        print(f"|{valor['nombre']}\t|\t{valor['valor']}\t|\t{valor['iva']}\t|")
        

def producto_iva_mas_bajo():
    ventas = globales.leer_archivo_json("ventas.json")
    ordenar_ventas = sorted(ventas, key= lambda x:x ["iva"], reverse= False)
    print("|producto\t|\tvalor\t|\tiva\t|")
    for valor in ordenar_ventas [:1]:
        print(f"|{valor['nombre']}\t|\t{valor['valor']}\t|\t{valor['iva']}\t|")

def promedio():
    ventas = globales.leer_archivo_json("ventas.json")
    tot_ventas=0
    cant_ventas=0
    for venta in ventas:
        tot_ventas += venta["valor"]
        cant_ventas += 1
    promedio = tot_ventas / cant_ventas
    print(f"El promedio del valor los productros es ${int(promedio)}")

def promedio_geometrico():
    ventas = globales.leer_archivo_json("ventas.json")
    tot_ventas=0
    cant_ventas=0
    for venta in ventas:
        tot_ventas += math.log (venta["valor"])
        cant_ventas += 1
    promedio = math.exp(tot_ventas / cant_ventas)
    print(f"El promedio del valor los productros es ${promedio}")

