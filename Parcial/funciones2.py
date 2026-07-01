def zonas_menor_18(avistamientos):
    total_avistamientos = 0

    for i in range(len(avistamientos)):
        total_avistamientos += avistamientos[i]

    print("\n Zonas con menos del 18 porciento de impacto bioambiental ")
    
    zonas_encontradas = []
    lista_porcentajes = []
    porcentaje_acumulado = 0

    for i in range(len(avistamientos)):
        porcentaje_zona = (avistamientos[i] / total_avistamientos) * 100
        if porcentaje_zona < 18:
            zonas_encontradas.append(i)
            lista_porcentajes.append(porcentaje_zona)
            porcentaje_acumulado += porcentaje_zona

    if len(zonas_encontradas) == 0:
        print("Error: No hay ninguna zona con menos del 18% de impacto.")
        return
    
    for i in range(len(zonas_encontradas)):
        i_zona = zonas_encontradas[i]
        print(f"Zona {i_zona + 1} | Avistamientos: {avistamientos[i_zona]} | Porcentaje: {lista_porcentajes[i]:.2f}%")
    
    print(f"Porcentaje acumulado total: {porcentaje_acumulado:.2f}%")

def zonas_altas_intensidad(avistamientos):
    total_avistamientos = 0

    for i in range(len(avistamientos)):
        total_avistamientos += avistamientos[i]
        
    zonas_encontradas = []
    suma = 0

    for i in range(len(avistamientos)):
        if avistamientos[i] > 400:
            zonas_encontradas.append(i)
            suma += avistamientos[i]

    if len(zonas_encontradas) == 0:
        print("\nError, no hay zonas con más de 400 avistamientos.")

        return
    
    print("\n Zonas de Alta Densidad ")
    for i in range(len(zonas_encontradas)):
        i_zona = zonas_encontradas[i]
        porcentaje_zona = (avistamientos[i_zona] * 100) / total_avistamientos
        print(f"Zona {i_zona + 1} | Avistamientos: {avistamientos[i_zona]} | Porcentaje: {porcentaje_zona:.2f}%")
        
    promedio = suma / len(zonas_encontradas)
    print(f"Suma total: {suma}")
    print(f"Cantidad de zonas con alta densidad {len(zonas_encontradas)}")
    print(f"Promedio: {promedio:.2f}")

def zonas_densidad_critica(avistamientos):
    total_avistamientos = 0

    for i in range(len(avistamientos)):
        total_avistamientos += avistamientos[i]
        
    zonas_encontradas = []
    suma = 0

    for i in range(len(avistamientos)):
        if avistamientos[i] > 900:
            zonas_encontradas.append(i)
            suma += avistamientos[i]

    if len(zonas_encontradas) == 0:
        print("\nError, No hay zonas con más de 900 avistamientos.")
        
        return
    
    print("\n Zonas de Densidad Crítica ")
    for i in range(len(zonas_encontradas)):
        i_zona = zonas_encontradas[i]
        porcentaje_zona = (avistamientos[i_zona] * 100) / total_avistamientos
        print(f"Zona {i_zona + 1} | Avistamientos: {avistamientos[i_zona]} | Porcentaje: {porcentaje_zona:.2f}%")
        
    promedio = suma / len(zonas_encontradas)
    print(f"Suma total: {suma}")
    print(f"Cantidad de zonas con densidad critica: {len(zonas_encontradas)}")
    print(f"Promedio: {promedio:.2f}")