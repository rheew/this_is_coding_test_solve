import copy
def turn(key):
    key.reverse()
    return [list(i) for i in zip(*key)]

def move(key, lock, board):
    end = len(key) - 1 + len(lock)
    for i in range(end):
        for j in range(end):
            inboard = insert(key, board, i, j)
            
            if isSolve(inboard, lock, len(key)-1) : return True
    return False

def insert(key, board, a, b):
    nboard = copy.deepcopy(board)
    for i in range(len(key)):
        for j in range(len(key)):
            nboard[a+i][b+j] = key[i][j]
    return nboard

def isSolve(board, lock, a):
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0 and board[a+i][a+j] == 0: return False
            elif lock[i][j] == 1 and board[a+i][a+j] == 1: return False
        
    return True

def solution(key, lock):
    answer = True
    boardlen = (len(key) - 1) * 2 + len(lock)
    board = [[0] * boardlen for _ in range(boardlen)]
    
    for i in range(4):
        if move(key, lock, board): return True
        key = turn(key)

    return False