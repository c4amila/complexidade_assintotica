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

### Exercício 3
```python
def busca_binaria(lista, alvo): 
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita: 
        meio = (esquerda + direita) // 2 

        if lista[meio] == alvo: 
            return meio 
        elif lista[meio] < alvo: 
            esquerda = meio + 1 
        else: 
            direita = meio - 1 

    return -1
```
**Complexidade:** O(log n) <br>
**Justificativa:** existe um while que está dividindo o vetor pela metade a cada iteração que faz.

### Exercício 4
```python
def pares_com_soma(lista, alvo): 
    for i in range(len(lista)): 
        for j in range(i + 1, len(lista)): 
            if lista[i] + lista[j] == alvo: 
                print(lista[i], lista[j])
```
**Complexidade:** O(n²) <br>
**Justificativa:** este código faz 2 verificações usando loops aninhados para encontrar todos os pares que somem e resultem o valor que o alvo escolheu, para cada elemento do vetor ele compara com todos os outros na frente.

### Exercício 5
```python
def imprimir_pares_e_soma(lista): 
    # Bloco 1: imprime cada elemento 
    for i in range(len(lista)):
        print(lista[i])
    # Bloco 2: imprime todos os pares 
    for i in range(len(lista)): 
        for j in range(len(lista)): 
            print(lista[i], lista[j])
```
**Complexidade:** O(n²) <br>
**Justificativa:** apesar de ter um loop percorrendo uma única vez para apenas mostrar todos os valores do vetor - O(n) -, logo depois há loops aninhados para fazer dupla verificação com objetivo de encontrar o máximo de pares possíveis para cada elemento.

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