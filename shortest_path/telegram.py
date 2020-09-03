import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, M, C = map(int, input().rstrip().split())

city = [[] * N for _ in range(N)]
cost = [INF] * N

for i in range(M):
    a, b, v =  map(int, input().rstrip().split())
    city[a-1].append((b,v))

h = []
heapq.heappush(h, (C, 0))
cost[C-1] = 0
while len(h):
    node, value = heapq.heappop(h)

    if cost[node - 1] < value : continue
    for ind, val in city[node - 1]:
        sum = val + value
        if cost[ind - 1] > sum :
            cost[ind - 1] = sum
            heapq.heappush(h, (ind, sum))

ans = -1
maxValue = 0
for i in cost:
    if i == INF: continue
    ans += 1
    maxValue = max(maxValue, i)

print(ans, maxValue)

# 3 2 1
# 1 2 4
# 1 3 2