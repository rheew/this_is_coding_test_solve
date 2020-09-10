import sys
import copy
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().rstrip().split())

board = [list(map(int, input().rstrip().split())) for _ in range(N)]
visit = [[-1] * N for _ in range(N)]

dx, dy = [1,-1,0,0], [0,0,1,-1]
totalPeople = [[0,0] for _ in range(N * N + 1) ]
packindex = -1
ans = 0

def packCity():
    nvisit = copy.deepcopy(visit)
    global packindex, ans, totalPeople
    for i in range(N):
        for j in range(N):
            if nvisit[i][j] != -1 : continue
            BFS(nvisit, i, j)
    if movePeople(nvisit) :
        totalPeople = [[0,0] for _ in range(N * N + 1) ]
        packindex = -1
        ans += 1
        packCity()

def movePeople(nvisit):
    flag = False

    for i in range(N):
        for j in range(N):

            if nvisit[i][j] == -1 : continue
            index = nvisit[i][j]
            board[i][j] = totalPeople[index][0] // totalPeople[index][1]
            flag = True

    return flag
def BFS(nvisit, i, j) :

    d = deque()
    d.append((i,j))
    global packindex
    packindex += 1
    totalPeople[packindex][0] = board[i][j]
    totalPeople[packindex][1] += 1
    nvisit[i][j] = packindex

    while d :
        x, y = d.popleft()
        for a in range(4) :
            nx, ny = dx[a] + x, dy[a] + y

            if 0 <= nx < N and 0 <= ny < N :
                if nvisit[nx][ny] != -1 : continue
                if L <= abs(board[x][y] - board[nx][ny]) <= R:
                    nvisit[nx][ny] = packindex
                    totalPeople[packindex][0] += board[nx][ny]
                    totalPeople[packindex][1] += 1
                    d.append((nx, ny))
    if totalPeople[packindex][0] == board[i][j] :
        nvisit[i][j] = -1
        totalPeople[packindex][1] = 0
        packindex -= 1

packCity()
print(ans)