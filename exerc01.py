def verificar_primeiro(lista): 
    if len(lista) == 0: 
        return None 
    return lista[0]

lista = [5, 10, 15, 20, 25, 30, 35]

print(verificar_primeiro(lista))