def zonas_encima_promedio(avistamientos):
    total_avistamientos = 0
    for i in range(len(avistamientos)):
        total_avistamientos += avistamientos[i]

    promedio_general = total_avistamientos / len(avistamientos)
    print("\n zonas por encima del promedio ecológico general ")
    print(f"Promedio general absoluto: {promedio_general:.2f} avistamientos") 

    suma = 0
    encima_promedio = False

    for i in range(len(avistamientos)):
        if avistamientos[i] > promedio_general:
            print(f"Zona {i + 1} | Avistamientos: {avistamientos[i]}")
            suma += avistamientos[i]
            encima_promedio = True

    if not encima_promedio:
        print("No hay zonas que superen el promedio general.")
        return

    porcentaje_acumulado = (suma * 100) / total_avistamientos
    print(f"Porcentaje acumulado frente al total absoluto: {porcentaje_acumulado:.2f}%")

def zonas_menor_registro(avistamientos):
    total_avistamientos = 0
    for i in range(len(avistamientos)):
        total_avistamientos += avistamientos[i]

    menor_valor = avistamientos[0]
    for i in range(len(avistamientos)):
        if avistamientos[i] < menor_valor:
            menor_valor = avistamientos[i]

    print("\n Zonas con Menor Registro ")
    for i in range(len(avistamientos)):
        if avistamientos[i] == menor_valor:
            porcentaje_zona = (avistamientos[i] * 100) / total_avistamientos
            print(f"Zona {i + 1} | Avistamientos: {avistamientos[i]} | Porcentaje: {porcentaje_zona:.2f}%")

def harcodear_vetor():
    avistamientos_zonas = [850, 310, 150, 1420, 620, 500, 1100, 95, 2300, 70]
    print("\nEl vector ha sido reemplazado con los datos de prueba")

    return avistamientos_zonas.copy()