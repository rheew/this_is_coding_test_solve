import sys

T = int(input().rstrip())

for i in range(T):
    N, M = map(int, input().rstrip().split())
    li = list(map(int, input().rstrip().split()))
    nli = []
    for j in range(0, N*M - M + 1, M):
        nli.append(li[j:j+M])
    nli = [list(i) for i in zip(*nli)]

    for j in range(1, M):
        for k in range(N):
            a = k - 1
            if a < 0 : a = 0
            b = k + 2
            nli[j][k] += max(nli[j-1][a:b])
    print(nli)
    ans = 0
    print(max(nli[M-1]))

# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 2 1 5 2 2 4 1 5 0 2 3 0 6 1 2