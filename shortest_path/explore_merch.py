import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    board = [list(map(int, input().rstrip().split())) for _ in range(N)]
    visit = [[INF] * N for _ in range(N)]
    visit[0][0] = board[0][0]
    h = []
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    heapq.heappush(h,(board[0][0],0,0))

    while h :

        value, x, y = heapq.heappop(h)
        if visit[x][y] < value : continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx >= N or nx < 0 or ny >= N or ny < 0 : continue
            if value + board[nx][ny] >= visit[nx][ny] : continue
            visit[nx][ny] = value + board[nx][ny]
            heapq.heappush(h, (visit[nx][ny], nx, ny))

    for i in range(N):
        for j in range(N):
            print(visit[i][j], end='')
        print()
    print()

'''
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
'''