import math 
import os 


def pause():
    programPause = input("Press the <ENTER> key to continue...")


largeur = 4
hauteur = 4


def newGame():
    grille = []
    for i in range(largeur):
        grille.append(['.']*hauteur)
    return grille

def joueur(grille):
    x =0
    o = 0 
    for i in grille:
        x += i.count('X')
        o += i.count('O')
    return ('O',x+o) if x>o else ('X',x+o)

def affichage(grille):
    for i in range(hauteur-1,-1,-1):
            print('|',end='')
            for j in range(largeur):
                print(grille[j][i],end='|')
            print()
            
def terminalTest(grille, pions ):
    
    if pions == largeur* hauteur or pions ==42:
        return True
    #Colonnes 
    for col in grille:
        for i in range(hauteur-3):
            
            if col[i] == col[i+1] == col[i+2] == col[i+3] != '.':
                return True
    #Lignes
    for i in range(hauteur):
        for j in range(largeur-3):
            
            
            if grille[j][i] == grille[j+1][i] == grille[j+2][i] == grille[j+3][i] != '.':
                return True 
    #Diagonales
    for i in range(hauteur-3):
        for j in range(largeur -3):
            if grille[i][j] == grille[i+1][j+1] == grille[i+3][j+3] == grille[i+2][j+2] != '.':
                return True 
    for i in range(3,hauteur):
        for j in range(largeur-3):
            if grille[i][j] == grille[i-1][j+1] == grille[i-3][j+3] == grille[i-2][j+2] != '.' :
                return True
    return False



            
def actions(grille):
    listeaction = []
    for i in range(largeur):
        if grille[i].count('.') >0:
            listeaction.append(i)
    return listeaction

def result(grille,col):
    grille[col][grille[col].index('.')] = joueur(grille)[0]
    return grille

def resultReset(grille,colonne):
    for i in range(hauteur-1,-1,-1):
        if grille[colonne][i] != '.':
            grille[colonne][i] = '.'
            break
    return grille 
    
def utility(jeu,pions,tt):
    if tt:
        if pions[0] == 'X':
            return -22+pions[1]//2
        if pions[1]== 'O':
            return 21 - pions[1]//2
        else:
            return 0 
        
    

#%% 

def minimax(jeu,profondeur,maximise):
    '''affichage(jeu)
    print(jeu)
    pause()'''
    pions = joueur(jeu)
    '''if profondeur ==0:
            return utility(jeu,pions)'''
    if pions == 42 or pions == largeur* hauteur:
        return 0
    tt = terminalTest(jeu,pions[1])
    if tt:
        return utility(jeu,pions,tt)
     
    
    if maximise:
        best = -math.inf
        act = actions(jeu)
        for a in act:
            jeu = result(jeu,a)
            best = max(best,minimax(jeu,profondeur-1,not maximise))
            jeu = resultReset(jeu,a)
        return best
    else:
        best = math.inf
        act = actions(jeu)
        for a in act:
            jeu = result(jeu, a)
            best = min(best, minimax(jeu,profondeur -1,not maximise))
            jeu = resultReset(jeu,a)
        return best

def meilleurcoup(jeu,profondeur = 10):
    player = joueur(jeu)[0]
    if player == 'X':
        best_val = -math.inf
        best_move = None 
        act = actions(jeu)
        for a in act:
            jeu = result(jeu,a)
            move_val = minimax(jeu, profondeur-1,False)
            jeu = resultReset(jeu, a)
            if move_val>best_val:
                best_val = move_val
                best_move = a 
            print(best_move,best_val)
        return best_move 
    
    if player == 'O':
        best_val = math.inf
        best_move = None 
        act = actions(jeu)
        for a in act:
            jeu = result(jeu,a)
            move_val = minimax(jeu, profondeur-1,True)
            jeu = resultReset(jeu, a)
            if move_val<best_val:
                best_val = move_val
                best_move = a 
            print(best_move,best_val)
        return best_move 

def jeuIA(jeu = None):
    if jeu == None:
        jeu = newGame()
    affichage(jeu)
    while True:
        coup = meilleurcoup(jeu,100)
        jeu = result(jeu,coup)
        affichage(jeu)
        j = joueur(jeu)
        if j[1] == hauteur * largeur:
            print('Nul')
            break
        if terminalTest(jeu,j[1]):
            print(j[0] +' a perdu')
            break
        coup = int(input('Votre Coup'))
        jeu = result(jeu, coup)
        affichage(jeu)
        j = joueur(jeu)
        if j[1] == hauteur * largeur:
            print('Nul')
            break
        if terminalTest(jeu,j[1]):
            print(j[0] + ' a perdu')
            break
jeuIA([['X', 'O', '.', '.'], ['X', 'O', '.', '.'], ['O', 'X', '.', '.'], ['X', 'O', '.', '.']])
    