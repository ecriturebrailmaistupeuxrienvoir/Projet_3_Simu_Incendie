import pygame
pygame.init()
import sys
import math
import random

display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

vents = ["nord", "sud", "est", "ouest"]
sens_vent = 0
tick_vent = 1
class Route :
    def __init__ (self, x, y) :
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.color = (103, 113, 121)
        self.infla = False

    def main(self, display) :
        pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height))

class Champs :
    def __init__ (self, x, y) :
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.color = (0, 86, 27)
        self.infla = True
        self.etat = "eteint"
        self.proba_combu = 200
        self.temps_combu = random.randint(100, 200)
        self.temps_brule = 0
        self.adjacents = []
    
    def main(self, display) :
        
        self.adjacents = get_adj(self.x, self.y)
            
        if self.etat == "brule" :
            action_feu(self, self.adjacents)
        
        if self.etat == "eteint" :
            self.color = (0, 86, 27)
        if self.etat == "brule" :
            self.color = (187, 11, 11)
        if self.etat == "consume" :
            self.color = (70, 63, 50)
        
        pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height))

class Foret :
    def __init__ (self, x, y) :
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.color = (0, 86, 27)
        self.infla = True
        self.etat = "eteint"
        self.proba_combu = 1000
        self.temps_combu = random.randint(900, 1200)
        self.temps_brule = 0
        self.adjacents = []
    
    def main(self, display) :
        
        self.adjacents = get_adj(self.x, self.y)
            
        if self.etat == "brule" :
            action_feu(self, self.adjacents)
        
        if self.etat == "eteint" :
            self.color = (27, 79, 8)
        if self.etat == "brule" :
            self.color = (109, 7, 26)
        if self.etat == "consume" :
            self.color = (61, 43, 31)
        
        pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height))

class Bord :
    def __init__ (self, x, y) :
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.color = (0, 0, 0)
        self.infla = False

    def main(self, display) :
        pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height))
    

def get_adj(x : int, y : int ) -> list :
    """
    Parameters
    ----------
    x : int
        Coordonnées X de la case
    y : int
        Coordonnées Y de la case
    Returns
    -------
    list 
        Liste des adjaceants de la case
    """
    adj = []
    x = int(x/20)
    y = int(y/20)
    adj.append(plateau[y-1][x-1])
    adj.append(plateau[y-1][x])
    adj.append(plateau[y-1][x+1])
    adj.append(plateau[y][x-1])
    adj.append(plateau[y][x+1])
    adj.append(plateau[y+1][x-1])
    adj.append(plateau[y+1][x])
    adj.append(plateau[y+1][x+1])
    return adj


def action_feu(self, adj : list) -> None :
    """
    Parameters
    ----------
    adj : list
        Liste des adjaceants de la case v
    -------
    Ne retourne rien: la fonction sert à gérer l'action du feu dans les différentes cases.
    """
    self.temps_brule += 1
    if self.temps_brule == self.temps_combu :
        self.etat = "consume"
        self.infla = False
    for i in adj :
        if i.infla :
            #if 
            if random.randint(0, i.proba_combu) == 42 :
                i.etat = "brule"



plateau = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #initialisation de la matrice permettant la création du plateau
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 3, 3, 3, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


for i in range (len(plateau)) :
    for j in range (len(plateau[1])) :
        if plateau[i][j] == 0 :
            plateau[i][j]=Champs(j*20, i*20)
        if plateau[i][j] == 1 :
            plateau[i][j]=Bord(j*20, i*20)
        if plateau[i][j] == 2 :
            plateau[i][j]=Route(j*20, i*20)
        if plateau[i][j] == 3 :
            plateau[i][j]=Foret(j*20, i*20)

plateau[18][3].etat = "brule"

while True :    
    mouse_x, mouse_y = pygame.mouse.get_pos() 

    for event in pygame.event.get(): #Récupération des evenements
        if event.type == pygame.QUIT : #Permet de quitter proprement pygame
            sys.exit()

    #Action du vent
    tick_vent -= 1
    if tick_vent == 0 :
        sens_vent = random.randint(1, 4)


    
    for i in range (len(plateau)) : #Permet l'action de toutes les cases du plateau
        for j in range (len(plateau[1])) :
            plateau[i][j].main(display)
    
    
    clock.tick(60) #Permet de faire tourner le jeu à 60 fps
    pygame.display.update() #Update la fenêtre
