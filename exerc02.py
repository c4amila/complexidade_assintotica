def somar_lista(lista): 
    total = 0 
    for elemento in lista:
        total += elemento 
    return total 

lista = [5, 10, 15, 20, 25, 30]
print(somar_lista(lista))