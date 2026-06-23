def ordenar_especies():
    lista_especies = [
        "Yaguareté", 
        "Cóndor", 
        "Aguará Guazú", 
        "Puma",
        "Coatí", 
        "Carayá", 
        "Tapir", 
        "Tucán"
    ]
    for i in range(len(lista_especies) - 1):
        for j in range(len(lista_especies) - 1 - i):
            if lista_especies[j] > lista_especies[j + 1]:

                variable = lista_especies[j]
                lista_especies[j] = lista_especies[j + 1]
                lista_especies[j + 1] = variable
    print("\n-especies ordenadas-")

    for i in range(len(lista_especies)):
        print(lista_especies[i])