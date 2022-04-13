# Journal

## V0 : En cours de création

11/04/2022 :  
Instanciation des 3 classes terminées  
Création du plateau terminée et opérationnelle  
Comportement du feu en cours de création :  
Code pour la propagation terminé, mais non testé  
Problème : Fonction get_adj non opérationnelle (index out of range)  

13/04/2022 :
V0 terminée :
Réparation de la fonction get_adj:  
  -Problème encontré: inversion de l'axe des abscisses et celui des ordonnées  
Réparation du code de propagation du feu :  
  -Problème encontré: liste self.adjacents était une liste composée d'un seul élément, qui était la liste d'adjacents: réglé dans l'appel de la fonction            get_adj dans la fonction main
 Ajout de l'extinction du feu au bout d'un certain temps.
