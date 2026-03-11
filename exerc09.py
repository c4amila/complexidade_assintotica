def produto_de_matrizes(A, B, n): 
    C = [[0] * n for _ in range(n)] 
    for i in range(n): 
        for j in range(n): 
            for k in range(n): 
                C[i][j] += A[i][k] * B[k][j] 
    return C

n = 3
A = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
B = [[9, 8, 7],
      [6, 5, 4],
      [3, 2, 1]]
C = produto_de_matrizes(A, B, n)
print("Produto das matrizes:")
for row in C:
    print(row)