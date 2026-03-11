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

### Exercício 6
```python
def potencias_de_dois(n): 
    i = 1 

    while i < n: 
        print(i) 
        i *= 2
```
**Complexidade:** O(log n) <br>
**Justificativa:** Fiquei em dúvida entre O(2ⁿ) e O(log n), mas estarei apostando que esse código tem complexidade O(log n) pois está multiplicando o valor de n por 2 até chegar no valor definido pelo usuário, os valores crescem muito devagar.

### Exercício 7
```python
def fibonacci_recursivo(n): 
    if n <= 1: 
        return n 
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
```
**Complexidade:** O(2ⁿ) <br>
**Justificativa:** este código tem complexidade O(2ⁿ) pois o crescimento deste já é muito maior que o logarítmico, cada chamada está gerado 2 novas chamadas: (n-1) e (n-2).

### Exercício 8
```python
def ordenacao_bolha(lista): 
    n = len(lista) 
    for i in range(n): 
        for j in range(0, n - i - 1): 
            if lista[j] > lista[j + 1]: 
                lista[j], lista[j + 1] = lista[j + 1], lista[j] 
    return lista
```
**Complexidade:** O(n²) <br>
**Justificativa:** este código contém loops aninhados fazendo duas comparações: o i verifica quantas passagens serão feitas e o j compara os valores próximos, caso o elemento atual seja maior que o próximo, ele troca os valores, jogando o maior para o final da lista.

### Exercício 9
```python
def produto_de_matrizes(A, B, n): 
    C = [[0] * n for _ in range(n)] 
    for i in range(n): 
        for j in range(n): 
            for k in range(n): 
                C[i][j] += A[i][k] * B[k][j] 
    return C
```
**Complexidade:** O(n³) <br>
**Justificativa:** Contém 3 loops aninhados realizando 3 operações: i percorre cada linha da primeira matriz, j percorre cada linha da segunda matriz e k percorre as linhas e colunas, realizando a multiplicação das matrizes. Ou seja, está ocorrendo operações n * n * n, ao invés de ter complexidade O(n²), será O(n³).

## Principais Notações Utilizadas

| Complexidade | Descrição | Exemplo |
|:----------:|:-----------:|:---------|
| O(1) | Tempo constante | Acesso a um elemento de um array |
| O(log n) | Tempo logarítmico | Busca binária |
| O(n) | Tempo linear | Percorrer um Array |
| O(n log n) | Tempo linearítmico | Merge Sort |
| O(n²) | Tempo quadrático | Bubble Sort |
| O(2ⁿ) | Tempo exponencial | Fibonacci recursivo |
| O(n!) | Tempo fatorial | Permutações de um conjunto |