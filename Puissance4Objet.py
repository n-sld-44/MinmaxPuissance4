# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:06:08 2023

@author: natha
"""
import math
import random
largeur = 4
hauteur = 4

class Puissance4:
    def __init__(self,tableau= None):
        if tableau == None:
            self.board = self.newGame()    
        else:
            self.board = tableau
        
        self.joueur = self.Joueur()
        self.etatFinal = self.terminalTest()
        self.actions = self.Actions()
        self.utility = self.Utility()
            
    
    def affichage(self):
        for i in range(hauteur-1,-1,-1):
            print('|',end='')
            for j in range(largeur):
                print(self.board[j][i],end='|')
            print()
        
    
    def newGame(self):
        grille = []
        for i in range(largeur):
            grille.append(['.']*hauteur)
        return grille
    
    def Joueur(self):
        o =0
        x = 0
        for i in self.board:
            o += i.count('O')
            x+= i.count('X')
        self.pions = x+o
        self.x = 21-x
        self.o = 21-o
        return 'O' if x>o else 'X'
    
    def Utility(self):
        grille = self.board
        if self.pions==hauteur*largeur:
            return 0
        #test colonne
        for colonne in grille:
            for i in range(hauteur-3):
                if colonne[i]==colonne[i+1]==colonne[i+2]==colonne[i+3] =='X':
                    return self.x+1
                elif colonne[i]==colonne[i+1]==colonne[i+2]==colonne[i+3] =='O':
                    return self.o-1
        #test ligne
        for i in range(hauteur):
            for j in range(largeur-3):
                if grille[j][i] == grille[j+1][i] == grille[j+2][i] ==  grille[j+3][i] == 'X':
                    return self.x+1
                elif grille[j][i] == grille[j+1][i] == grille[j+2][i] ==  grille[j+3][i] == 'O':
                    return self.o-1
        
        #test Diagonale 
        for i in range(hauteur-3):
            for j in range(largeur-3):
                if grille[j][i] == grille[j+1][i+1] == grille[j+2][i+2] ==  grille[j+3][i+3] == 'X':
                    return self.x+1
                elif grille[j][i] == grille[j+1][i+1] == grille[j+2][i+2] ==  grille[j+3][i+3] == 'O':
                    return self.o-1
                
        for i in range(hauteur-1,3,-1):
            for j in range(largeur-1,3,-1):
                if grille[j][i] == grille[j-1][i-1] == grille[j-2][i-2] ==  grille[j-3][i-3] == 'X':
                    return self.x+1
                elif grille[j][i] == grille[j-1][i-1] == grille[j-2][i-2] ==  grille[j-3][i-3] == 'O':
                    return self.o-1
        else:
            return 0
        
        
        
    def terminalTest(self): #A modifier au niveau des signes si erreur
        
        if self.pions == largeur*hauteur or self.pions == 42:
            return True
        for colonne in self.board:
            for i in range(hauteur-3):
                if colonne[i]==colonne[i+1]==colonne[i+2]==colonne[i+3] =='X':
                    return True
                
        #test ligne
        for i in range(hauteur):
            for j in range(largeur-3):
                if self.board[j][i] == self.board[j+1][i] == self.board[j+2][i] ==  self.board[j+3][i] == 'X':
                    return True
        
        #test Diagonale 
        for i in range(hauteur-3):
            for j in range(largeur-3):
                if self.board[j][i] == self.board[j+1][i+1] == self.board[j+2][i+2] ==  self.board[j+3][i+3] == 'X':
                    return True
                
        for i in range(hauteur-1,2,-1):
            for j in range(largeur-1,3,-1):
                if self.board[j][i] == self.board[j-1][i-1] == self.board[j-2][i-2] ==  self.board[j-3][i-3] == 'X':
                    return True
            
        else:
            return False
        
        
        
    def Actions(self):
        listeaction = []
        for i in range(largeur):
            if self.board[i].count('.') >0:
                listeaction.append(i)
        return listeaction
        
        
    def Result(self,colonne):
        grille = self.board[:]
        grille[colonne][grille[colonne].index('.')]= self.joueur
            
        return Puissance4(grille)
        
    def ResultReset(self,colonne):
        grille = self.board
        for i in range(hauteur-1,-1,-1):
            
            if grille[colonne][i]!='.':
                grille[colonne][i] = '.'
                break
        return Puissance4(grille)
            
        
    

#%%

def minimax(jeu, profondeur,maximise):
    if profondeur ==0:
        return jeu.utility
    if jeu.etatFinal :
        return jeu.utility
    if jeu.pions ==largeur*hauteur:
        return 0
    if maximise:
        best = -math.inf
        actions = jeu.actions
        for a in actions:
            jeu = jeu.Result(a)
            best = max(best,minimax(jeu,profondeur-1,not maximise))
            jeu = jeu.ResultReset(a)
        return best
    else:
        best = math.inf
        actions = jeu.actions
        for a in actions:
            jeu = jeu.Result(a)
            best = min(best,minimax(jeu,profondeur-1,not maximise))
            jeu = jeu.ResultReset(a)
        return best
    
def meilleurcoup(jeu,X,profondeur=9):
    if X:
        best_val = -math.inf
        best_move = -1 
        actions = jeu.actions    
        for a in actions:
            jeu = jeu.Result(a)
            move_val = minimax(jeu,profondeur-1,False)
            jeu = jeu.ResultReset(a)
            
            if move_val> best_val:
                best_move,best_val = a,move_val
        return best_move
    else:
        best_val = math.inf
        best_move = -1 
        actions = jeu.actions    
        for a in actions:
            jeu = jeu.Result(a)
            move_val = minimax(jeu,profondeur-1,True)
            jeu = jeu.ResultReset(a)
            
            if move_val< best_val:
                best_move,best_val = a,move_val
        return best_move

def jeuIA():
    humain = int(input('0 pour jouer en premier, 1 pour jouer en deuxieme'))
    jeu = Puissance4()
    jeu.affichage()
    if humain== 1:
        while True:
            coup = meilleurcoup(jeu,True)
            jeu = jeu.Result(coup)
            jeu.affichage()
            if jeu.etatFinal  :
                print(jeu.joueur+' a perdu')
                break
            coup = int(input('Votre Coup'))
            jeu = jeu.Result(coup)
            jeu.affichage()
            if jeu.etatFinal :
                print(jeu.joueur+' a perdu')
                break
    
    else:
        while True:
            coup = int(input('Votre Coup'))
            jeu = jeu.Result(coup)
            jeu.affichage()
            if jeu.etatFinal:
                print(jeu.joueur+' a perdu')
                break
            coup = meilleurcoup(jeu,False)
            jeu = jeu.Result(coup)
            jeu.affichage()
            if jeu.etatFinal:
                print(jeu.joueur+' a perdu')
                break        
        
        
#%% Alpha Beta
#Soucis sur l'alpha beta, la grille d'origine n'est pas restituée
   
def minimaxAlphaBeta(jeu,alpha,beta,maximise):
    
    if jeu.etatFinal :
        return jeu.utility
    if jeu.pions ==largeur*hauteur:
        return 0
    if maximise:
        best = -math.inf
        actions = jeu.actions
        for a in actions:
            jeu = jeu.Result(a)
            best = max(best,minimaxAlphaBeta(jeu,alpha,beta,not maximise))
            jeu = jeu.ResultReset(a)
            if best>=beta:
                return best
            alpha = max(alpha,best)
        return best
    else:
        best = math.inf
        actions = jeu.actions
        for a in actions:
            jeu = jeu.Result(a)
            best = min(best,minimaxAlphaBeta(jeu,alpha,beta,not maximise))
            jeu = jeu.ResultReset(a)
            if best<= alpha:
                return best
            beta = min(beta,best)
        return best
    
    
def meilleurcoupAlphaBeta(jeu,alpha,beta,X):
    if X:
        best_val = -math.inf
        best_move = -1 
        actions = jeu.actions    
        for a in actions:
            jeu = jeu.Result(a)
            move_val = minimaxAlphaBeta(jeu,alpha,beta,False)
            jeu = jeu.ResultReset(a)
            
            if move_val> best_val:
                best_move,best_val = a,move_val
        return best_move
    else:
        best_val = math.inf
        best_move = -1 
        actions = jeu.actions    
        for a in actions:
            jeu = jeu.Result(a)
            move_val = minimaxAlphaBeta(jeu,alpha,beta,True)
            jeu = jeu.ResultReset(a)
            
            if move_val< best_val:
                best_move,best_val = a,move_val
        return best_move




def jeuIAalphabeta():
    humain = int(input('0 pour jouer en premier, 1 pour jouer en deuxieme'))
    jeu = Puissance4()
    jeu.affichage()
    if humain== 1:
        while True:
            coup = meilleurcoupAlphaBeta(jeu,-math.inf,math.inf,True)
            jeu = jeu.Result(coup)
            print(coup)
            jeu.affichage()
            if jeu.etatFinal  :
                print(jeu.joueur+' a perdu')
                break
            coup = int(input('Votre Coup'))
            jeu = jeu.Result(coup)
            print(coup)
            jeu.affichage()
            if jeu.etatFinal :
                print(jeu.joueur+' a perdu')
                break
    
    else:
        while True:
            coup = int(input('Votre Coup'))
            jeu = jeu.Result(coup)
            print(coup)
            jeu.affichage()
            if jeu.etatFinal:
                print(jeu.joueur+' a perdu')
                break
            coup = meilleurcoupAlphaBeta(jeu,-math.inf,math.inf,False)
            jeu = jeu.Result(coup)
            print(coup)
            jeu.affichage()
            if jeu.etatFinal:
                print(jeu.joueur+' a perdu')
                break  