def ordenacao_bolha(lista): 
    n = len(lista) 
    for i in range(n): 
        for j in range(0, n - i - 1): 
            if lista[j] > lista[j + 1]: 
                lista[j], lista[j + 1] = lista[j + 1], lista[j] 
    return lista

lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
lista_ordenada = ordenacao_bolha(lista)
print("Lista ordenada:", lista_ordenada)