import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

board = [list(map(int, input().rstrip().split())) for _ in range(N)]

S, X, Y = map(int, input().rstrip().split())

dx, dy = [1,-1,0,0], [0,0,1,-1]

def BFS(heap, board, temp):
    if temp == S: return
    if not len(heap) : return
    nheap = []
    while len(heap):
        value, x, y = heapq.heappop(heap)

        for i in range(4):
            nextx, nexty = dx[i] + x, dy[i] + y

            if 0 <= nextx < N and 0 <= nexty < N:
                if board[nextx][nexty] != 0 : continue
                board[nextx][nexty] = value
                heapq.heappush(nheap, (board[nextx][nexty], nextx, nexty))
    BFS(nheap, board, temp+1)

heap = []

for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            heapq.heappush(heap, (board[i][j],i,j))

BFS(heap, board, 0)
print(board[X-1][Y-1])