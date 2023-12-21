# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:18:54 2023

@author: natha
"""
import math


#En déclarant notre grille comme ça on peut ajuster l'algorithme sur une grille plus petite et ensuite l'elargir 
largeur = 7

# Initialise une nouvelle grille de jeu
def newGame():
    grille = []
    for i in range(largeur):
        grille.append(['.']*6)
    return grille

# Permet d'afficher la grille 
def affichage(grille):
    for i in range(5,-1,-1):
        print('|',end='')
        for j in range(largeur):
            print(grille[j][i],end='|')
        print()

# Compte le nombre de pions par joueur et retourne le joueur à qui c'est le tour, en supposant que les 'X' jouent en premier
def Joueur(grille):
    o =0
    x = 0
    for i in grille:
        o += i.count('O')
        x+= i.count('X')
    return 'O' if x>o else 'X'
    
#Liste toutes les actions possibles (chaque colonne sauf si l'une d'elles est pleine)    
def Actions(grille):
    listeaction = []
    for i in range(7):
        if grille[i].count('.') >0:
            listeaction.append(i)
    return listeaction


#Applique un coup selon le joueur a qui c'est le tour 
def Result(grille,colonne):
    
    joueur = Joueur(grille)
    grille[colonne][grille[colonne].index('.')]= joueur
    
    return grille

#Reset le coup qui vient d'etre joué. Est utile dans le minimax pour retrouver l'etat du plateau d'origine
def ResultReset(grille,colonne):
    
    for i in range(5,0,-1):
        if grille[colonne][i]!='.':
            grille[colonne][i] = '.'
            return grille
        
    grille[colonne]=['.']*6
    return grille
    
    
    
# Evalue si le jeu est fini ou non, retourne True si la partie est finie
def TerminalTest(grille):
    pions =0
    for i in grille :
        pions += 6-i.count('.')
        if pions == 42:
            return True
    #test colonne
    for colonne in grille:
        for i in range(3):
            if colonne[i]==colonne[i+1]==colonne[i+2]==colonne[i+3] !='.':
                return True
    #test ligne
    for i in range(6):
        for j in range(largeur-3):
            if grille[j][i] == grille[j+1][i] == grille[j+2][i] ==  grille[j+3][i] != '.':
                return True
    
    #test Diagonale 
    for i in range(3):
        for j in range(largeur-3):
            if grille[j][i] == grille[j+1][i+1] == grille[j+2][i+2] ==  grille[j+3][i+3] != '.':
                return True
    for i in range(5,3,-1):
        for j in range(largeur-1,3,-1):
            if grille[j][i] == grille[j-1][i-1] == grille[j-2][i-2] ==  grille[j-3][i-3] != '.':
                return True
 
    else:
        return False

#A definir, cette fonction servira a evaluer un etat du jeu, par exemple si j'ai 3 pions aligné c'est valorisé pour moi et dévalorisé pour l'adversaire
def utility(grille):
    pass

#On itere parmis tous les coups possibles de la grille en simulant le coup adverse
def Minimax(grille):
    a = TerminalTest(grille)

    if a:
        return
    meilleurcoup,score = -1,-math.inf
    for a in Actions(grille):
        grille = Result(grille,a)
        scoreb = minValue(grille,0)
        if scoreb>score:
            meilleurcoup,score = a , scoreb
        
        grille = ResultReset(grille,a)
    return meilleurcoup


#Simule nos coups en cherchant le maximum possible
def maxValue(grille,profondeur):
    a = TerminalTest(grille)
    if a:
        return 100
    if profondeur == 10:
        return 0
    v = -math.inf 
    for a in Actions(grille):
        grille = Result(grille,a)
        v =  max(v,minValue(grille,profondeur+1))
        grille = ResultReset(grille,a)
    return v-profondeur
        

#Simule les coups adverse
def minValue(grille,profondeur):
    a = TerminalTest(grille)
    if a:
        return -100
    if profondeur == 10:
        return 0
    v = math.inf
    for a in Actions(grille):
        grille = Result(grille,a)
        v = min(v,minValue(grille, profondeur+1))
        grille = ResultReset(grille, a)
        
    return v+profondeur
    
#Permet de lancer une partie, il y aura une selection des joueurs et de l'ordre dans lequel on joue
def Jeu():
    pass
    
            
