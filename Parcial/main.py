from funciones import *
from funciones2 import *
from funciones3 import *
from ordenar_especies import *

avistamientos = [0] * 8
cargado = False  
opcion_seleccionada = ""

while opcion_seleccionada != "0":
    print("1 - Cargar avistamientos (Manual - 8 zonas)")
    print("2 - Reporte general")
    print("3 - Zonas menor al 8% de impacto bioambiental")
    print("4 - Zonas menor al 12% de impacto bioambiental")
    print("5 - Zonas menor al 18% de impacto bioambiental")
    print("6 - Zonas de alta densidad")
    print("7 - Zonas de densidad crítica")
    print("8 - Zonas por encima del promedio ecológico general")
    print("9 - Zonas con menor registro")
    print("10 - Hardcodear vector de prueba")
    print("11 - Ordenar especies por nombre")
    print("0 - Salir del menú")

    opcion_seleccionada = input("Elija una opción: ")

    if opcion_seleccionada == "1":
        cargar_avistamientos(avistamientos)
        cargado = True  
    
    elif opcion_seleccionada in ["2", "3", "4", "5", "6", "7", "8", "9"]:
        if not cargado:
            print("\n error, debe cargar datos antes de realizar análisis, elija del 1 al 10.")
        else:
            if opcion_seleccionada == "2":
                reporte(avistamientos)
            elif opcion_seleccionada == "3":
                zonas_menor_8(avistamientos)
            elif opcion_seleccionada == "4":
                zonas_menor_12(avistamientos)
            elif opcion_seleccionada == "5":
                zonas_menor_18(avistamientos)
            elif opcion_seleccionada == "6":
                zonas_altas_intensidad(avistamientos)
            elif opcion_seleccionada == "7":
                zonas_densidad_critica(avistamientos)
            elif opcion_seleccionada == "8":
                zonas_encima_promedio(avistamientos)
            elif opcion_seleccionada == "9":
                zonas_menor_registro(avistamientos)
                
    elif opcion_seleccionada == "10":
        avistamientos = harcodear_vetor()
        cargado = True  
        
    elif opcion_seleccionada == "11":
        ordenar_especies()  
        
    elif opcion_seleccionada == "0":
        print("\nFin del sistema. ¡Muchas gracias por utilizar el monitor de biodiversidad!")
    else:
        print("\nError: Opción inválida. Ingrese un número correspondiente al menú.")