# Simulateur d'incendie

Projet: Un jeu de simulateur d'incendie

Le projet sera un jeu, avec un grille constituée de carrées dans un premier temps, avec chaque case de la grille qui constituera un élément. Chaque élément aura des caractéristiques différente de propagation, longueur de tenue du feu, et extinction.

Exemple de modèles de case:
-Champs: propagation de feu rapide et consumption rapide
-Forêt: Propagation plus lente et consumption lente
-Route: inflammable

Fonctions :
get_adj : Fonction prenant en paramètre les coordonnées d'une case et renvoyant une liste d'adjaceants.
main : toutes les classes sont composées d'une fonction main, qui s'occupe de l'action de la case. Cette fonction peut appeler une autre fonction de la classe.

Création du terrain:
Le terrain est instancié grâce à une matrice, et ensuite, une boucle parcourant la liste crée les différentes cases.

Etapes de développement:

V0: Création de la boucle basique:
Quelques éléments, propagation et extinction automatique de feu.

