from Funciones import *

avistamientos = [0,0,0,0,0,0,0,0]
opcion = ""

while opcion != "0":
    print("\n-menu principal-")
    print("1 - cargar avistamientos")
    print("2 - reporte general")
    print("3 - zonas menor al 8 porciento de impacto bioambiental ")
    print("4 - zonas menor al 12 porciento de impacto bioambiental")
    print("5 - zonas menor al 18 porciento de impacto bioambiental")
    print("6 - zonas de alta densidad")
    print("7 - zonas de densidad critica")
    print("8 - zonas por encima del promedio ecologico general")
    print("9 - zonas con menor registro")
    print("10 - harcodear vector")
    print("0 - salir del menu")

    opcion = input("elija una opcion: ")

    if opcion == "1":
        cargar_avistamientos(avistamientos)
    elif opcion == "2":
        reporte(avistamientos)
    elif opcion == "3":
        zonas_menor_8(avistamientos)
    elif opcion == "4":
        zonas_menor_12(avistamientos)
    elif opcion == "5":
        zonas_menor_18(avistamientos)
    elif opcion == "6":
        zonas_altas_intensidad(avistamientos)
    elif opcion == "7":
        zonas_densidad_critica(avistamientos)
    elif opcion == "8":
        zonas_encima_promedio(avistamientos)
    elif opcion == "9":
        zonas_menor_registro(avistamientos)
    elif opcion == "10":
        harcodear_vetor()
    elif opcion == "0":
        print("fin del sistema")
    else:
        print("error, ingrese una opcion valida")