# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:44:21 2023

@author: natha
"""

"""
"""
import math
class Ttt:
    def __init__(self,tableau= None):
        if tableau == None:
            self.board = self.newGame()    
        else:
            self.board = tableau
        
        self.joueur = self.Joueur()
        self.etatFinal = self.terminalTest()
        self.actions = self.Actions()
        
            
    
    def affichage(self):
        board = self.board
        print(board[0],'|',board[1],'|',board[2])
        print('----------')
        print(board[3],'|',board[4],'|',board[5])
        print('----------')
        print(board[6],'|',board[7],'|',board[8])
    
    def newGame(self):
        return ['.']*9
    
    def Joueur(self):
        x = 0
        o = 0
        for i in self.board:
            o += i.count('O')
            x+= i.count('X')
        self.caselibre = 9-x+o
        
        
        return 'O' if x>o else 'X'
    
    def terminalTest(self):
        board  = self.board
        
        for row in board:
            if all(cell == 'X' for cell in row):
                return 10
            elif all(cell == 'O' for cell in row):
                return -10

        for col in range(3):
            if all(board[row][col] == 'X' for row in range(3)):
                return 10
            elif all(board[row][col] == 'O' for row in range(3)):
                return -10

        if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
            return 10
        elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
            return -10

        return 0
        
     
     
    def Actions(self):
    
        listeaction = []
        for i in range(9):
            if self.board[i]== '.':
                listeaction.append(i)
        return listeaction
        
        
    def Result(self,colonne):
        grille = list(self.board)
        grille[colonne] = self.joueur
            
        return Ttt(grille)
        
    def ResultReset(self,colonne):
        grille = self.board
        grille[colonne] == '.' 
            
        
        return Ttt(grille)
    

    
    
def Minimax(jeu,maximise):
    if maximise:
        meilleurcoup,score= -1,-math.inf
        for a in jeu.actions:
            jeu = jeu.Result(a)
            scorebis = MinValue(jeu)
            if scorebis>score:
                meilleurcoup,score == a,scorebis
            jeu = jeu.ResultReset(a)
    if not maximise:
        meilleurcoup,score= -1,math.inf
        for a in jeu.actions:
            jeu = jeu.Result(a)
            scorebis = MaxValue(jeu)
            jeu = jeu.ResultReset(a)
            if scorebis<score:
                meilleurcoup,score == a,scorebis
            
    return meilleurcoup

def MinValue(jeu):
    if jeu.etatFinal!=-1:
        return jeu.utility #A modifier si ca ne marche pas 
    value = math.inf
    for a in jeu.actions:
        jeu = jeu.Result(a)
        value = min(value,MaxValue(jeu))
        jeu = jeu.ResultReset(a)
    return value
    
def MaxValue(jeu):
    if jeu.etatFinal!=-1:
        return jeu.utility
    value = -math.inf
    for a in jeu.actions:
        jeu = jeu.Result(a)
        value = max(value,MinValue(jeu))
        jeu = jeu.ResultReset(a)
    return value

def Jeu():
    jeu = Ttt()
    jeu.affichage()
    while True:
        coup = int(input('Votre Coup'))
        jeu = jeu.Result(coup)
        jeu.affichage()
        if jeu.etatFinal!=-1:
            print(jeu.joueur+' a perdu')
            break
        
        
def jeuVsia():
    humain = int(input('0 pour jouer en premier, 1 pour jouer en deuxieme'))
    jeu = Ttt()
    jeu.affichage()
    if humain== 1:
        while True:
            coup = Minimax(jeu, True)
            print('Coup joué '+str(coup))
            jeu = jeu.Result(coup)
            jeu.affichage()
            if jeu.etatFinal!=-1:
                print(jeu.joueur+' a perdu')
                break
            coup = int(input('Votre Coup '))
            print('Coup joué '+str(coup))
            jeu = jeu.Result(coup)
            jeu.affichage()
            if jeu.etatFinal!=-1:
                print(jeu.joueur+' a perdu')
                break
    
    else:
        while True:
            coup = int(input('Votre Coup'))
            print('Coup joué '+str(coup))
            jeu = jeu.Result(coup)
            jeu.affichage()
            if jeu.etatFinal!=-1:
                print(jeu.joueur+' a perdu')
                break
            coup = Minimax(jeu,False)
            print('Coup joué '+str(coup))
            jeu = jeu.Result(coup)
            jeu.affichage()
            if jeu.etatFinal!=-1:
                print(jeu.joueur+' a perdu')
                break

        
    
   
def evaluate(board):
    # Fonction d'évaluation pour le jeu Tic-Tac-Toe
    # Retourne 10 si le joueur X gagne, -10 si le joueur O gagne, 0 sinon
    for row in board:
        if all(cell == 'X' for cell in row):
            return 10
        elif all(cell == 'O' for cell in row):
            return 

    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 10
        elif all(board[row][col] == 'O' for row in range(3)):
            return -10

    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return 10
    elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return -10

    return 0

def is_moves_left(board):
    # Vérifie s'il reste des coups à jouer sur le plateau
    return any(cell == ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    # Algorithme minimax
    score = evaluate(board)

    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = ' '
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = ' '
        return best

def find_best_move(board):
    # Trouve le meilleur coup à jouer en utilisant l'algorithme minimax
    best_val = float('-inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Exemple d'utilisation
board = [['X', 'X', 'O'],
         ['O', 'O', 'X'],
         ['X', 'O', ' ']]

best_move = find_best_move(board)
print("Meilleur coup:", best_move)
    
    