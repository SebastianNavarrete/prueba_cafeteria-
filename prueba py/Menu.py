import os
import globales 
import generar_valor_producto
import estadisticas

os.system("cls")

def menu_estadisticas():
    while True:
        os.system("cls")
        print("1. producto con valor mas alto")
        print("2. producto iva mas bajo")
        print("3. promedio valor productos")
        print("4. media geometrica")
        print("5. volver")

        opcion = globales.seleccionar_opcion(5)
        if opcion == 1:
            estadisticas.producto_mayor_valor()
        elif opcion == 2:
            estadisticas.producto_iva_mas_bajo()
        elif opcion == 3:
            estadisticas.promedio()
        elif opcion == 4:
            estadisticas.promedio_geometrico()
        elif opcion == 5:
            return
        input()

def menu_principal():
    while True:
        os.system("cls")
        print("1. asignar montos aleatoreos")
        print("2. ver estadisticas")
        print("3. salir")

        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            generar_valor_producto.generar_ventas()
        elif opcion == 2:
            menu_estadisticas()
        elif opcion == 3:
            return
        input()

__name__ = "__menu__"
menu_principal()