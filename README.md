# Simulateur d'incendie

## Projet: Un jeu de simulateur d'incendie

Le projet sera un jeu, avec un grille constituée de carrées dans un premier temps, avec chaque case de la grille qui constituera un élément. Chaque élément aura des caractéristiques différente de propagation, longueur de tenue du feu, et extinction.

Exemple de modèles de case:
-Champs: propagation de feu rapide et consumption rapide
-Forêt: Propagation plus lente et consumption lente
-Route: inflammable

Fonctions :
get_adj : Fonction prenant en paramètre les coordonnées d'une case et renvoyant une liste d'adjaceants.
main : toutes les classes sont composées d'une fonction main, qui s'occupe de l'action de la case. Cette fonction peut appeler une autre fonction de la classe.

main: Une fonction qui est présente sur toutes les classes. Elle prend en paramètre la fenâte display et permet l'action de chaque élément.

Création du terrain:
Le terrain est instancié grâce à une matrice, et ensuite, une boucle parcourant la liste crée les différentes cases.

Etapes de développement:

### V0: Création de la boucle basique (MVP):

Création de classes pour les différentes cases:
-Bord: case immuable, constituant les bords du terrain
-Route: case de terrain, inflammable
-Champs: case inflammable, et qui propage le feu

Comportement du feu:
-Propagation du feu d'une case inflammable à une autre
-Extinction du feu sur une case qui brûle assez longtemps

### V1 : 
Ajout de l'hérédité lors de l'instanciation des cases

Ajout de nouvelles classes :
-Forêt: case inflammable, qui prends plus de temps à brûle et s'inflamme plus lentement

Comportement du feu:
-Ajout du vent, qui influe sur la propagation du feu
-Ajout des brandons, qui permettent d'enflammer des cases non adjaceantes.

### V2 :
Transformation des cases du terrain en hexagones
