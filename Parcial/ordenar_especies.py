def ordenar_especies():
    lista_especies = ["Yaguareté", 
                      "Cóndor", 
                      "Aguará Guazú", 
                      "Puma", 
                      "Coatí", 
                      "Carayá", 
                      "Tapir", 
                      "Tucán"]
    
    limite_externo = len(lista_especies) - 1
    for i_externo in range(limite_externo):
        limite_interno = len(lista_especies) - 1 - i_externo
        for i_interno in range(limite_interno):
            if lista_especies[i_interno] > lista_especies[i_interno + 1]:
                variable = lista_especies[i_interno]
                lista_especies[i_interno] = lista_especies[i_interno + 1]
                lista_especies[i_interno + 1] = variable

    print("\n Especies Ordenadas Alfabéticamente ")
    for i_especie in range(len(lista_especies)):
        print(f" {lista_especies[i_especie]}")

ordenar_especies()