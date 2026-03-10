# Análise de Complexidade Assintótica (Big O)

Atividade proposta pelo professor Alexandre Montanha, com objetivo de analisar diferentes trechos de código, identificar qual é a complexidade e justificar a resposta.

## Resolução

### Exercício 1
```python
def verificar_primeiro(lista):
    if len(lista) == 0: 
        return None 
    return lista[0]
```
**Complexidade:** O(1) <br>
**Justificativa:** É um código que não está usando nenhum loop, está acessando apenas o primeiro elemento de uma lista de forma imediata.

### Exercício 2
```python
def somar_lista(lista): 
    total = 0 
    for elemento in lista:
        total += elemento 
    return total 
```
**Complexidade:** O(n) <br>
**Justificativa:** por ser um loop único e que executa a soma para cada elemento da lista. Se dobrar os dados, o tempo irá dobrar.

## Principais Notações Utilizadas

| Complexidade | Descrição | Exemplo |
|:-------------:|:-----------:|:---------|
| O(1) | Tempo constante | Acesso a um elemento de um array |
| O(log n) | Tempo logarítmico | Busca binária |
| O(n) | Tempo linear | Percorrer um Array |
| O(n log n) | Tempo linearítmico | Merge Sort |
| O(n²) | Tempo quadrático | Bubble Sort |
| O(2ⁿ) | Tempo exponencial | Fibonacci recursivo |
| O(n!) | Tempo fatorial | Permutações de um conjunto |