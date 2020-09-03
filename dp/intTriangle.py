import sys

input = sys.stdin.readline

N = int(input().rstrip())

board = [list(map(int, input().rstrip().split())) for _ in range(N)]

for i in range(1, len(board)):
    for j in range(len(board[i])):
        if j == 0 :
            board[i][j] += board[i-1][j]
            continue
        elif  j == len(board[i])-1 :
            board[i][j] += board[i-1][j-1]
            continue
        board[i][j] += max(board[i-1][j], board[i-1][j-1])
print(max(board[N-1]))