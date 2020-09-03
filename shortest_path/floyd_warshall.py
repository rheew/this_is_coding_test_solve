import sys

input = sys.stdin.readline
INF = int(1e9)

N = int(input().rstrip())
M = int(input().rstrip())

city = [[INF] * (N + 1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    city[a][b] = min(c, city[a][b])

for i in range(1,N + 1):
    for j in range(1, N + 1):
        if i == j : city[i][j] = 0

for k in range(1,N + 1):
    for i in range(1,N + 1):
        for j in range(1, N + 1):
            city[i][j] = min(city[i][k] + city[k][j], city[i][j])

for i in range(1,N + 1):
    for j in range(1, N + 1):
        if city[i][j] == INF : print(0, end=' ')
        else : print(city[i][j], end=' ')
    print()