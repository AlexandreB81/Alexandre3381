import random

# Fonction pour afficher le plateau de jeu
def afficher_plateau(plateau):
    for ligne in plateau:
        print("|".join(ligne))
    print("\n")

# Fonction pour vérifier si un joueur a gagné
def verifier_victoire(plateau, symbole):
    # Vérification des lignes et des colonnes
    for i in range(3):
        if all(plateau[i][j] == symbole for j in range(3)) or all(plateau[j][i] == symbole for j in range(3)):
            return True
    # Vérification des diagonales
    if all(plateau[i][i] == symbole for i in range(3)) or all(plateau[i][2 - i] == symbole for i in range(3)):
        return True
    return False

# Fonction pour déterminer si le plateau est plein (match nul)
def plateau_plein(plateau):
    return all(plateau[i][j] != " " for i in range(3) for j in range(3))

# Fonction pour le tour de l'IA
def tour_ia(plateau, symbole):
    # Stratégie simple : choix aléatoire d'une case vide
    while True:
        ligne = random.randint(0, 2)
        colonne = random.randint(0, 2)
        if plateau[ligne][colonne] == " ":
            plateau[ligne][colonne] = symbole
            break

# Fonction principale pour jouer au jeu
def jouer_tic_tac_toe():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    symboles = ["X", "O"]
    tour_joueur = 0

    while not verifier_victoire(plateau, symboles[tour_joueur]) and not plateau_plein(plateau):
        afficher_plateau(plateau)
        if tour_joueur == 0:
            tour_ia(plateau, symboles[tour_joueur])
        else:
            print("C'est votre tour (ligne colonne) : ")
            coup = input().split()
            ligne, colonne = int(coup[0]), int(coup[1])
            if plateau[ligne][colonne] == " ":
                plateau[ligne][colonne] = symboles[tour_joueur]
            else:
                print("Case déjà occupée. Essayez encore.")
                continue

        tour_joueur = (tour_joueur + 1) % 2

    afficher_plateau(plateau)

    if verifier_victoire(plateau, "X"):
        print("L'IA a gagné !")
    elif verifier_victoire(plateau, "O"):
        print("Vous avez gagné !")
    else:
        print("Match nul !")

# Appel de la fonction principale pour démarrer le jeu
jouer_tic_tac_toe()
