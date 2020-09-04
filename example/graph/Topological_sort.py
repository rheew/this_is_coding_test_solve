import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

indegree = [0] * (N + 1)
node = [[] for _ in range(N + 1)]


for i in range(M):
    a, b = map(int, input().rstrip().split())
    node[a].append(b)
    indegree[b] += 1

d = deque()
for i in range(1, N):
    if indegree[i] == 0:
        d.append(i)

while d:
    cur = d.popleft()
    print(cur)
    for i in node[cur]:
        indegree[i] -= 1
        if indegree[i] == 0:
            d.append(i)

# input
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4
