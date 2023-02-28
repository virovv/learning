
n = int(input())
A = [[int(_) for _ in input().split()]for _ in range(n)]


m = int(input())

C = [[0 * n for l in range(n)]for j in range(n)]
B = A
for k in range(m-1):
    for i in range(n):
        for j in range(n):
            for r in range(n):
                C[i][j] += B[i][r] * A[r][j]
    B = C.copy()
    C = [[0 * n for l in range(n)]for j in range(n)]
    
for x in B:
    print(*x)