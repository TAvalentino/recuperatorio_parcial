avistamientos = []
cargado = False

def cargar_avistamientos():
    
    '''
    '''

    for i in range(len(avistamientos)):
        while True:
            entrada = input(f" zona {i + 1}:")
            try:
                valor = int(entrada)
                if valor <= 0:
                    print("error, debe ingresar un valor mayor a cero")
                else:
                    avistamientos[i] = valor
                    break
            except ValueError:
                print("ingreso invalido intente nuevamente")

def reporte():

    '''
    '''

    total = 0
    for i in range(len(avistamientos)):
        total += avistamientos[i]
    print("\n-- reporte general --")

    for i in range(len(avistamientos)):
        porcentaje = (avistamientos[i] / total) * 100
        print("zona", i + 1, "avistamientos: ", avistamientos[i], "porcentaje:", "%.2f" % porcentaje, "%") 
        print("zonas activas:", len(avistamientos))
        print("total acumulado:", total)

def zonas_menor_8():

    '''
    '''

    total = 0
    for i in range(len(avistamientos)):
        total += avistamientos[i]
    print("\n-zonas con menos del 8 porciento de impacto-")

    encontradas = []
    porcentaje = []
    porcentaje_acumulado = 0

    for i in range(len(avistamientos)):
        porcentaje = (avistamientos[i] / total) * 100
        if porcentaje < 8:
            encontradas.append(i + 1)
            porcentaje.append(porcentaje)
            porcentaje_acumulado += porcentaje

    if len(encontradas) == 0:
        print("no hay zonas con menos del 8%")
        return
    
    for i in range(len(encontradas)):
        print("zona", encontradas[i], "avistamientos:", avistamientos[encontradas[i] + 1])
        print("porcentaje:", "%.2f" % porcentaje[i], "%")
        print("porcentaje acumulado:", "%.2f" % porcentaje_acumulado, "%")

def zonas_menor_12():

    '''
    '''

    total = 0
    for i in range(len(avistamientos)):
        total += avistamientos[i]        
    print("\n-zonas con menos del 12 porciento de impacto-")

    encontradas = []
    porcentaje = []
    porcentaje_acumulado = 0

    for i in range(len(avistamientos)):
        porcentaje = (avistamientos[i] / total) * 100
        if porcentaje < 12:
            encontradas.append(i + 1)
            porcentaje.append(porcentaje)
            porcentaje_acumulado += porcentaje

    if len(encontradas) == 0:
        print("no hay zonas con menos del 12%")
        return
    
    for i in range(len(encontradas)):
        print("zona", encontradas[i], "avistamientos:", avistamientos[encontradas[i] + 1])
        print("porcentaje:", "%.2f" % porcentaje[i], "%")
        print("porcentaje acumulado:", "%.2f" % porcentaje_acumulado, "%")

def zonas_menor_18():

    '''
    '''

    total = 0
    for i in range(len(avistamientos)):
        total += avistamientos[i]        
    print("\n-zonas con menos del 18 porciento de impacto-")

    encontradas = []
    porcentaje = []
    porcentaje_acumulado = 0

    for i in range(len(avistamientos)):
        porcentaje = (avistamientos[i] / total) * 100
        if porcentaje < 18:
            encontradas.append(i + 1)
            porcentaje.append(porcentaje)
            porcentaje_acumulado += porcentaje

    if len(encontradas) == 0:
        print("no hay zonas con menos del 18%")
        return
    
    for i in range(len(encontradas)):
        print("zona", encontradas[i], "avistamientos:", avistamientos[encontradas[i] + 1])
        print("porcentaje:", "%.2f" % porcentaje[i], "%")
        print("porcentaje acumulado:", "%.2f" % porcentaje_acumulado, "%")

def zonas_altas_intensidad():

    '''
    '''

    total = 0
    for i in range(len(avistamientos)):
        total += avistamientos[i]
        
    encontradas = []
    suma = 0

    for i in range(len(avistamientos)):
        if avistamientos[i] > 400:
            encontradas.append(i)
            suma += avistamientos[i]
    if len(encontradas) == 0:
        print("no hay zonas con mas de 400 avistamientos")
        return
    
    print("zonas de alta densidad")
    for i in range(len(encontradas)):
        zona = encontradas[i]
        porcentaje = (avistamientos[zona] * 100) / total

        print("zona:", zona + 1)
        print("avistamientos:", avistamientos[zona])
        print("porcentaje:", "%.2f" % porcentaje, "%")
        print()
    cantidad = len(encontradas)
    promedio = suma / cantidad

    print("suma total: ", suma)
    print("cantidad de zonas: ", cantidad)
    print(f"promedio: {promedio}")

def zonas_densidad_critica():

    '''
    '''

    total = 0
    for i in range(len(avistamientos)):
        total += avistamientos[i]
        
    encontradas = []
    suma = 0

    for i in range(len(avistamientos)):
        if avistamientos[i] > 900:
            encontradas.append(i)
            suma += avistamientos[i]
    if len(encontradas) == 0:
        print("no hay zonas con mas de 900 avistamientos")
        return
    
    print("zonas de densidad critica")
    for i in range(len(encontradas)):
        zona = encontradas[i]
        porcentaje = (avistamientos[zona] * 100) / total

        print("zona:", zona + 1)
        print("avistamientos:", avistamientos[zona])
        print("porcentaje:", "%.2f" % porcentaje, "%")
        print()
    cantidad = len(encontradas)
    promedio = suma / cantidad

    print("suma total: ", suma)
    print("cantidad de zonas: ", cantidad)
    print(f"promedio: {promedio}")

def zonas_encima_promedio():
    '''
    '''

    total = 0
    for i in range(len(avistamientos)):
        total += avistamientos[i]

    promedio_general = total / len(avistamientos)

    print("zonas por encima del promedio")
    print(f"promedio general: {promedio_general}") 

    encontradas = []
    suma = 0

    for i in range(len(avistamientos)):
        if avistamientos[i] > promedio_general:
            encontradas.append(i)
            suma += avistamientos[i]
    if len(encontradas) == 0:
        print("no hay zonas por encima del promedio")
    
    for i in range(len(encontradas)):
        zona = encontradas[i]

        print("zona: ", zona + 1)
        print("avistamientos: ", avistamientos[zona])
        print()

    porcentaje_acumulado = (suma * 100) / total
    print(f"porcentaje acumulado: {porcentaje_acumulado}")

def zonas_menor_registro():

    '''

    '''

    total = 0
    for i in range(len(avistamientos)):
        total += avistamientos[i]

    menor = avistamientos[0]

    for i in range(len(avistamientos)):
        if avistamientos[i] < menor:
            menor = avistamientos[i]

    encontradas = []

    for i in range(len(avistamientos)):
        if avistamientos[i] == menor:
            encontradas.append(i)

    print("zonas con menor registro")

    for i in range(len(encontradas)):
        zona = encontradas[i]
        porcentaje = (avistamientos[zona] * 100) / total

        print("zona: ", zona + 1)
        print("avistamientos: ", avistamientos[zona])
        print(f"porcentaje: {porcentaje}")
        print()

#harcodeo de vector
def harcodear_vetor():
    avistamientos_zonas = [850, 310, 150, 1420, 620, 500, 1100, 95,
                            2300, 70]
    
    return avistamientos_zonas.copy()

print("se harcodeo correctamente")