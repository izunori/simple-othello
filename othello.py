from collections import Counter
from itertools import product
class Board:
    marks = {-1:'W', 1:'B',0:'-'}
    def __init__(self, size=8):
        self.size = size
        self.board = [[0]*size for _ in range(size)]
    def __getitem__(self, key):
        return self.board[key]
    def __str__(self):
        res = ' abcdefgh\n'
        for i,row in enumerate(self.board):
            temp = str(i+1)+"".join(map(lambda x : self.marks[x], row))
            res += temp+'\n'
        nb, nw = count(self.board)
        res += f" {self.marks[1]}:{nb} {self.marks[-1]}:{nw}\n"
        return res
    def count(self):
        nw = sum(row.count(1) for row in self.board)
        nb = sum(row.count(-1) for row in self.board)
        return nb,nw

def generate(size=8):
    assert size % 2 == 0
    board = Board(size)
    half_size = size//2
    board[half_size-1][half_size-1] = -1 # white
    board[half_size][half_size-1] = 1 # black
    board[half_size-1][half_size] = 1
    board[half_size][half_size] = -1
    return board

def move(board, turn, pos, inplace=False):
    assert turn in [-1,1]
    x, y = pos

    if not board[x][y] == 0:
        return 0

    dirs = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
    cnt = 0
    rvs = []
    for dx, dy in dirs:
        temp = 0
        trvs = []
        nx,ny = x+dx,y+dy
        while 0<=nx<board.size and 0<=ny<board.size:
            if board[nx][ny] == -turn:
                trvs.append((nx,ny))
                temp += 1
            elif board[nx][ny] == turn:
                rvs.extend(trvs)
                cnt += temp
                break
            else: # 0
                break
            nx,ny = nx+dx,ny+dy
    if cnt > 0 and inplace == True:
        board[x][y] = turn 
        for tx,ty in rvs:
            board[tx][ty] = turn
    return cnt

def optionsOf(board, turn):
    result = []
    for x in range(board.size):
        for y in range(board.size):
            if move(board, turn, (x,y)) > 0:
                result.append((x,y))
    return result

def count(board):
    nb = sum(row.count(1) for row in board)
    nw = sum(row.count(-1) for row in board)
    return nb,nw

if __name__=='__main__':
    board = generate(8)
    print(board)
    move(board, 1, (3,2), True)
    print(board)
    move(board, -1, (2,2), True)
    print(board)


