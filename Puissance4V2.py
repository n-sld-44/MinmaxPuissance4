import math 
import os 


def pause():
    programPause = input("Press the <ENTER> key to continue...")


largeur = 7
hauteur = 6


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
    for i in range(largeur-3):
        for j in range(hauteur -3):
            if grille[i][j] == grille[i+1][j+1] == grille[i+3][j+3] == grille[i+2][j+2] != '.':
                return True 
    for i in range(3,largeur):
        for j in range(hauteur-3):
            if grille[i][j] == grille[i-1][j+1] == grille[i-3][j+3] == grille[i-2][j+2] != '.' :
                return True
    return False


def scoreWindow(window,joueur):
    
    score = 0
    if joueur == 'X':
        adv = 'O'
    else:
        adv = 'X'
        
    if window.count(joueur) == 4:
        score += 100
    elif window.count(joueur) == 3 and window.count('.')==1:
        score += 5
    elif window.count(joueur) == 2 and window.count('.')==2:
        
        score+=2
    if window.count(adv) == 3  and window.count('.') == 1:
        score -= 4
    return score 
        
        
    
    
            
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
    
def utility(jeu,joueur):
    score = 0
    #Horizontal
    for li in range(hauteur):
        lignes = [i for i in list(jeu[:][li])]
        for col in range(largeur-3):
            window = lignes[col:col+4]
            score += scoreWindow(window,joueur)
    #Vertical
    for col in range(largeur):
        colonne = [i for i in list(jeu[col][:])]
        for li in range(hauteur-4):
            window = colonne[li:li+4]
            score += scoreWindow(window,joueur)
    # Diago montante
    for li in range(hauteur-3):
        for col in range(largeur-3):
            window =[jeu[col+i][li+i] for i in range(4)]
            score += scoreWindow(window,joueur)       
    #Diago Descendante
    for li in range(3,hauteur):
        for col in range(largeur-3):
            window = [jeu[col+i][li-i] for i in range(4)]
            score += scoreWindow(window, joueur)
    
    return score
    


        
    

#%% 

def minimax(jeu,profondeur,maximise):
    
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




def elagage(jeu,profondeur,maximise,alpha,beta):
    
    pions = joueur(jeu)
   
    if pions[1] == 42 or pions[1] == largeur* hauteur:
        return 0
    tt = terminalTest(jeu,pions[0])
    if tt:
        return -100 if pions[0]=='X' else 100
    if profondeur ==0:
        affichage(jeu)
        score =utility(jeu,pions[0])
        print(score)
        return score
     
    
    if maximise:
        best = -math.inf
        act = actions(jeu)
        for a in act:
            jeu = result(jeu,a)
            best = max(best,elagage(jeu,profondeur-1,False,alpha,beta))
            jeu = resultReset(jeu,a)
            alpha = max(alpha,best)
            if alpha>= beta:
                break
        return best
    
    
    else:
        best = math.inf
        act = actions(jeu)
        for a in act:
            jeu = result(jeu, a)
            best = min(best, elagage(jeu,profondeur -1,True,alpha,beta))
            jeu = resultReset(jeu,a)
            beta = min(beta,best)
            if alpha>= beta:
                break
        return best

def meilleurcoup(jeu,profondeur = 8):
    alpha = -math.inf
    beta = math.inf
    player = joueur(jeu)[0]
    if player == 'X':
        best_val = -math.inf
        
        act = actions(jeu)
        for a in act:
            jeu = result(jeu,a)
            move_val = elagage(jeu, profondeur-1,False,alpha,beta)
            jeu = resultReset(jeu, a)
            if move_val>best_val:
                best_val = move_val
                best_move = a 
            print(best_move,best_val)
        return best_move 
    
    if player == 'O':
        best_val = math.inf
        
        act = actions(jeu)
        for a in act:
            jeu = result(jeu,a)
            move_val = elagage(jeu, profondeur-1,True,alpha,beta)
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
        coup = meilleurcoup(jeu,7)
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
jeuIA()
    