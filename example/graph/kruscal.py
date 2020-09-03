import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

root = [i for i in range(N+1)]
edge = []
ans = 0

def union(a, b):
    parentsA = find(a)
    parentsB = find(b)
    if parentsA < parentsB:
        root[parentsB] = parentsA
    elif parentsA > parentsB:
        root[parentsA] = parentsB
    return

def find(a):
    if a == root[a]:
        return a

    parents = find(root[a])
    root[a] = parents
    return parents

for i in range(M):
    a, b, cost = map(int, input().rstrip().split())
    edge.append((cost,a,b))

edge.sort()

for cost, a, b in edge:
    if find(a) == find(b):
        continue
    else :
        union(a, b)
        ans += cost
        
print(ans)
#input
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25
