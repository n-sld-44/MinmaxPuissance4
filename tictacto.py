# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:44:21 2023

@author: natha
"""

"""
"""
def newGame():
    board = ['.']*9
    return board     

def affichage(board):
    print(board[0],'|',board[1],'|',board[2])
    print('----------')
    print(board[3],'|',board[4],'|',board[5])
    print('----------')
    print(board[6],'|',board[7],'|',board[8])
        

def Joueur(board):
    x = board.count('X')
    o = board.count('O')
    return 'O' if x>o else 'X'

def Coup(board,coup):
    joueur = Joueur(board)
    if board[coup] != '.':
        return board, False
    else:
        board[coup] = joueur
        return board,True
    
    
def evaluation(board):
    joueur = Joueur(board)
    #lignes
    
    for i in range(3):
        if board[3*i] == board[1+3*i] == board[2+3*i] != '.':
            return -10 if joueur == board[3*i] else 10
    
    #colonnes
    for i in range(3):
        if board[i] == board[i+3] ==board[i+6] != '.':
            return -10 if joueur == board[3*i] else 10
    
    #diago
    if board[0] == board[4] ==board[8] != '.':
        return -10 if joueur == board[0] else 10
    if board[2] == board[4] ==board[6] != '.':
        return -10 if joueur == board[0] else 10
    else:
        return 0

def Jeu():
    board = newGame()
    affichage(board)
    while True:
        
        test = False
        while test !=True:
            coup = int(input())
            board, test = Coup(board,coup)
        evalu = evaluation(board)
        affichage(board)
        print(evalu)
      
def actions(board):
    listeaction = []
    for i in range(9):
        if board[i]== '.':
            listeaction.append(i)
    return listeaction
        
def maxvalue(board,profondeur):
    evalu = evaluation(board)
    if evalu !=0:
        return evalu
    v = -20
    for a in actions(board):
        board[a] = Joueur(board)
        v = max(v,minvalue(board,profondeur+1))
        board[a] = '.'
        
    return v -profondeur
        

def minvalue(board,profondeur):
    evalu = evaluation(board)
    if evalu !=0:
        return evalu
    v = 20
    for a in actions(board):
        board[a] = Joueur(board)
        v = min(v,maxvalue(board,profondeur+1))
        board[a] = '.'
        
    return v +profondeur

def minimax(board,profondeur):
    meilleurcoup,score = -1,-20
    for a in actions(board):
        board[a] = Joueur(board)
        
        s = max(score,minvalue(board,profondeur+1))
        board[a] = '.'
        if s > score:
            meilleurcoup,score = a,s
    return meilleurcoup

def tour(board,Ia):
    if Ia ==False:
        test = False
        while test !=True:
            coup = int(input())
            board, test = Coup(board,coup)
        if evaluation(board)>0:
            print("Le joueur a gagné")
            affichage(board)
            return None
        
    if Ia == True:
        board,test = Coup(board,minimax(board, 0))
        affichage(board)
        if evaluation(board)>0:
            print("L'IA a gagné")
            return None
    
    tour(board,not Ia)

def jeuVsIA():
    ordre = int(input("0 pour jouer en premier, 1 sinon"))
    
    board = newGame()
    affichage(board)
    tour(board,ordre)
        
    
   
            
    
    