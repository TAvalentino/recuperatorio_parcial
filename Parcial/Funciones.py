def cargar_avistamientos(avistamientos):
    print("\n carga de avistamientos ")

    for i in range(len(avistamientos)):
        while True:
            entrada_usuario = input(f"Ingrese avistamientos Zona {i + 1}: ")
            try:
                valor_ingresado = int(entrada_usuario)
                if valor_ingresado <= 0:
                    print("Error: No se permiten números negativos ni ceros. Intente de nuevo.")
                else:
                    avistamientos[i] = valor_ingresado
                    break
            except ValueError:
                print("Error: Ingreso inválido (debe ser un número entero). Intente de nuevo.")

def reporte(avistamientos):
    total_avistamientos = 0

    for i in range(len(avistamientos)):
        total_avistamientos += avistamientos[i]
        
    print("\n reporte general ")
    for i in range(len(avistamientos)):
        porcentaje_zona = (avistamientos[i] / total_avistamientos) * 100
        print(f"Zona {i + 1} | Avistamientos: {avistamientos[i]} | Porcentaje: {porcentaje_zona:.2f}%")
    
    print(f"Cantidad de zonas activas: {len(avistamientos)}")
    print(f"Total acumulado de avistamientos: {total_avistamientos}")


def zonas_menor_8(avistamientos):
    total_avistamientos = 0

    for indice in range(len(avistamientos)):
        total_avistamientos += avistamientos[indice]

    print("\n Zonas con menos del 8 porciento de impacto bioambiental ")
    
    zonas_encontradas = []
    lista_porcentajes = []
    porcentaje_acumulado = 0

    for i in range(len(avistamientos)):
        porcentaje_zona = (avistamientos[i] / total_avistamientos) * 100
        if porcentaje_zona < 8:
            zonas_encontradas.append(i)
            lista_porcentajes.append(porcentaje_zona)
            porcentaje_acumulado += porcentaje_zona

    if len(zonas_encontradas) == 0:
        print("Error: No hay ninguna zona con menos del 8% de impacto.")

        return
    
    for i in range(len(zonas_encontradas)):
        i_zona = zonas_encontradas[i]
        print(f"Zona {i_zona + 1} | Avistamientos: {avistamientos[i_zona]} | Porcentaje: {lista_porcentajes[i]:.2f}%")
    
    print(f"Porcentaje acumulado total: {porcentaje_acumulado:.2f}%")

def zonas_menor_12(avistamientos):
    total_avistamientos = 0

    for i in range(len(avistamientos)):
        total_avistamientos += avistamientos[i]
    print("\n Zonas con menos del 12 porciento de impacto bioambiental ")
    
    zonas_encontradas = []
    lista_porcentajes = []
    porcentaje_acumulado = 0

    for i in range(len(avistamientos)):
        porcentaje_zona = (avistamientos[i] / total_avistamientos) * 100
        if porcentaje_zona < 12:
            zonas_encontradas.append(i)
            lista_porcentajes.append(porcentaje_zona)
            porcentaje_acumulado += porcentaje_zona

    if len(zonas_encontradas) == 0:
        print("Error: No hay ninguna zona con menos del 12% de impacto.")
        return
    
    for i in range(len(zonas_encontradas)):
        i_zona = zonas_encontradas[i]
        print(f"Zona {i_zona + 1} | Avistamientos: {avistamientos[i_zona]} | Porcentaje: {lista_porcentajes[i]:.2f}%")
    
    print(f"Porcentaje acumulado total: {porcentaje_acumulado:.2f}%")

