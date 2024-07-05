import globales
import random

def generar_ventas ():
    productos = globales.leer_archivo_json("productos.json")
    venta =[]
    for producto in productos :
        valor = random.randint(2000,10000)
        iva = valor * 0.19
        nueva_venta ={
            "nombre":producto["nombre"],
            "valor" : int(valor),
            "iva" : int(iva)
        }
        venta.append(nueva_venta)
    globales.guardar_archivo_json("ventas.json", venta)

generar_ventas()