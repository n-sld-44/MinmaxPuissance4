

def newGame():
    board = []
    for i in range(3):
        board.append(['.','.','.'])

    return board 

def affichage(board):
    print('-------------')
    print('|',board[0][0],'|',board[0][1],'|',board[0][2],'|')
    print('-------------')
    print('|',board[1][0],'|',board[1][1],'|',board[1][2],'|')
    print('-------------')
    print('|',board[2][0],'|',board[2][1],'|',board[2][2],'|')
    print('-------------')
    
def coup(board,a):
   tour = joueur(board)
   board[(a-1)//3][(a-1)%3] = tour
   return board

def joueur(board):
    x = 0
    o = 0
    for i in board:
        x += i.count('X')
        o += i.count('O')
    return 'O' if x>o else 'X'


def game():
    board = newGame()
    affichage(board)
    while len(coupsPossibles(board)) !=0:
        
        a = int(input('Coup à Jouer:  '))
        
        board = coup(board,a)
        affichage(board)
        

def coupsPossibles(board):
    coups = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                coups.append((i,j))
    return coups

def evaluate(board):
    for i in range(3):
        if board[i][1]== board[i][2]== board[i][2]== 'X':
            return 10
        if board[0][i]== board[1][i]== board[2][i]== 'X':
            return 10
        if board[i][1]== board[i][2]== board[i][2]== 'O':
            return -10
        if board[0][i]== board[1][i]== board[2][i]== 'O':
            return -10
        
    if board[0][0] == board[1][1] == board[2][2] =='X':
        return 10
    if board[0][0] == board[1][1] == board[2][2] =='O':
        return -10
    
    if board[0][2] == board[1][1] == board[2][0] =='X':
        return 10
    if board[0][2] == board[1][1] == board[2][0] =='O':
        return -10
    
    else:
        return 0
    
def coupsrestants(board):
    count = 0
    for i in board:
        count += i.count('.')
    return count == 0


def minmax(board,profondeur,maximise):
    score = evaluate(board)
    if score ==10:
        return score-profondeur
    if score == -10:
        return score+profondeur
    
    if coupsrestants(board):
        return 0
    
    if maximise:
        best = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = 'X'
                    best = max(best, minmax(board,profondeur + 1 ,not maximise))
                    board[i][j] = '.'
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                    best = min(best, minmax(board,profondeur + 1 , maximise))
                    board[i][j] = '.'
    return best


def MeilleurCoup(board):
    
    best_val = float('-inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                board[i][j] = 'X'
                move_val = minmax(board, 0, True)
                board[i][j] = '.'
    
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move
    




