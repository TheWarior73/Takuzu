from random import*
from copy import* 
import pygame
from pygame.locals import*
import sys

## Bellot Ewen          | 3
## Ador Louan           | 3
## Strazzeri Maxence    | 3
## Bonino Noé           | 2



## Utilisation fichier
## Mode d'emploi

# Pour jouer en mode console, on éxecute la commande takuzu('grille4x4_1') pour jouer avec la grille correspondante qui est donnée en format .txt.
# Pour jouer en mode graphique sur pygame, on éxecute la fonction takuzu_graphique('grille4x4_1') pour jouer avec la grille correspondante qui est donnée en format .txt.



#
###
#####
####################@ | Maxence
#####
###
#


## Création et affichage de la grille

# Fonction de lecture de la situation de départ
def lecture(nom_fic):
    """Cette fonction prend en paramètre :
    - une chaine de caractères désignant un nom de fichier (sans l'extension .txt)
    Elle renvoie une liste de liste automate contenant des 0 et des 1 avec :
    grille[l][c] contient 0 si la case de la ligne l et de la colonne c représente une cellule morte et 1 si elle c'est une cellule vivante.
    """
    # Ouverture du fichier en mode lecture ('r'ead)
    fichier = open(nom_fic + '.txt', 'r')
    tempo = []
    # Parcours des lignes du fichier :
    for ligne in fichier:
        # On ajoute à automate la ligne :
        # - débarassée des espaces superflus (strip())
        # - transformée en liste de caractères (list( ... ))
        tempo.append(list(ligne.strip()))
    # Fermeture du fichier :
    fichier.close()
    # Conversion des éléments en 0/1 à la place de '0'/'1'
    grille = [ [ int(tempo[l][c]) for c in range(len(tempo[l])) ] for l in range(len(tempo))]
    return grille



def affiche(g):
    """Cette fonction affiche la grille formatée comme il faut dans la console d'éxecution
    paramètre : (list) liste de liste carré et de taille pair
    """
    temp = ''
    grille = lecture(g)
    if len(grille) == 4 :
        print('  A B C D')
    elif len(grille) == 6 :
        print('  A B C D E F')
    elif len(grille) == 8 :
        print('  A B C D E F G H')
    elif len(grille) == 10 :
        print('  A B C D E F G H I J')
    for l in range(len(grille)) :
        for c in range(len(grille[0])) :
            if grille[l][c] == 0:
                temp += ' 0'
            elif grille[l][c] == 1:
                temp += ' 1'
            elif grille[l][c] == 9:
                temp += ' .'
        print(str(l) + temp)
        temp = ''
    pass
#
###
#####
####################@
#####
###
#
             


## Fonctions de jeu

# ======
## Noé
# ======
def demande_coup() :
    """ Fonction qui demande au joueur la case dans laquelle il souhaite jouer et la valeur du coup jouée.
    Paramètre : aucun
    Sortie : (str,int) une chaine de caractère correspondant au coup joué et un entier correspondant à la valeur du coup joué.
    """ 
    pass
    
# ======
## Ewen
# ======
def coord_coup_joue(case) :
    """ Fonction qui transforme la case jouée par le joueur au format texte (exemple A1) en coordonnées entières pour retrouver la valeur dans la grille de Takuzu au format liste de liste.
    Paramètre : (str) une chaine de caractère de longueur 2 au format attendu.
    Sortie : (int,int) un couple d'entiers correspondant à la case jouée dans la grille de Takuzu.
    """
    pass
    
# ======
## Maxence
# ======
def joue_coup(g,l,c,v) : 
    """ Fonction qui joue un coup dans la grille g à la ligne l colonne c avec la valeur v.
    Paramètres : (liste,int,int,int) une grille g de Takuzu au format liste de liste, un entier l correspondant à la ligne jouée, un entier c correspondant à la colonne jouée, un entier v (0 ou 1) correspondant à la valeur jouée.
    Sortie : (list) la grille g de Takuzu au format liste de liste mise à jour avec la valeur jouée.
    """
    pass   
    
# ======
## Louan
# ======
def takuzu(grille) :
    """ Fonction qui gère le déroulement d'une partie de TAKUZU """
    pass 

    
#
###
#####
####################@
#####
###
#     

## Fonctions pour tester la validité d'une grille avec les 3 règles

# ======
## 
# ======
def rotation(g) :
    """ Cette fonction construit la transposée d'une grille carrée (les lignes de la grille de départ deviennent les colonnes et inversement en gardant l'ordre).
    Paramètre : (list) une liste de liste g de taille carrée
    Sortie : (list) une liste de liste de taille carrée correspondant à la transposée de g
    """
    pass


# ======
## Ewen
# ======
def grille_remplie(g) :
    """ Fonction qui vérifie si la grille g de TAKUZU entrée en paramètre contient des cases non jouées.
    Paramètre : (list) une grille de Takuzu au format liste de liste
    Sortie : (bool) un booléen indiquant si la grille de Takuzu est complète
    """
    pass
    
# ======
## Louan
# ======
def verif_nb_0_nb_1(g) :
    """ Cette fontion vérifie que pour chaque ligne et chaque colonne de la grille g entrée en paramètre, le nombre de 0 et de 1 est égal à niveau/2.
    Paramètre : (list) un grille de Takuzu au format liste de liste 
    Sortie : (bool) un booléen indiquant si la grille est cohérente au niveau du nombre de 0 et de 1 par ligne et par colonne (Règle 1) 
    """ 
    pass          
 
# ======
## Louan
# ======   
def verif_000_111(g) :
    """ Cette fontion vérifie que pour chaque ligne et chaque colonne de la grille g entrée en paramètre, il n'y a jamais plus de deux 0 ou de deux 1 adjacents
    Paramètre : (list) un grille de Takuzu au format liste de liste 
    Sortie : (bool) un booléen indiquant si la grille est cohérente au niveau du nombre de 0 et de 1 adjacent par ligne et par colonne (Règle 2)
    """ 
    pass
    
# ======
## Noé
# ======
def verif_ligne_colonne(g) :
    """ Cette fontion vérifie que chaque ligne et chaque colonne de la grille g entrée en paramètre est unique.
    Paramètre : (list) un grille de Takuzu au format liste de liste 
    Sortie : (bool) un booléen indiquant si la grille est cohérente au niveau des lignes et des colonnes, chacune est unique (Règle 3)
    """ 
    pass

  
#
###
#####
####################@
#####
###
# 


## Version Graphique (BONUS)


# À FAIRE POUR CEUX QUI LE SOUHAITENT