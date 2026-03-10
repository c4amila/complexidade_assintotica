def pares_com_soma(lista, alvo): 
    for i in range(len(lista)): 
        for j in range(i + 1, len(lista)): 
            if lista[i] + lista[j] == alvo: 
                print(lista[i], lista[j])

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alvo = 10
pares_com_soma(lista, alvo)