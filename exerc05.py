def imprimir_pares_e_soma(lista): 
    # Bloco 1: imprime cada elemento 
    for i in range(len(lista)):
        print(lista[i])
    # Bloco 2: imprime todos os pares 
    for i in range(len(lista)): 
        for j in range(len(lista)): 
            print(lista[i], lista[j])

# maior numeros de combinações possiveis
lista = [1, 2, 3, 4, 5]
imprimir_pares_e_soma(lista)