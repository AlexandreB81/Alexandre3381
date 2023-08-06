import random

# Définir les dimensions de la grille
TAILLE_GRILLE = 8

# Symboles pour représenter les états de la grille
CASE_VIDE = '-'
CASE_BATEAU = 'B'
CASE_TOUCHE = 'X'
CASE_EAU = 'O'

# Définir les tailles des bateaux
TAILLES_BATEAUX = [5, 4, 4, 3, 3, 3, 2, 2, 2, 2]

# Fonction pour initialiser la grille
def initialiser_grille():
    return [[CASE_VIDE for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]

# Fonction pour placer les bateaux aléatoirement sur la grille
def placer_bateaux(grille):
    for taille_bateau in TAILLES_BATEAUX:
        while True:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                x = random.randint(0, TAILLE_GRILLE - taille_bateau)
                y = random.randint(0, TAILLE_GRILLE - 1)
                positions = [(x + i, y) for i in range(taille_bateau)]
            else:
                x = random.randint(0, TAILLE_GRILLE - 1)
                y = random.randint(0, TAILLE_GRILLE - taille_bateau)
                positions = [(x, y + i) for i in range(taille_bateau)]
            
            if all(grille[x][y] == CASE_VIDE for x, y in positions):
                for x, y in positions:
                    grille[x][y] = CASE_BATEAU
                break

# Fonction pour afficher la grille
def afficher_grille(grille):
    for ligne in grille:
        print(' '.join(ligne))

# Fonction pour le tour de jeu d'un joueur
def tour_de_jeu(joueur, grille_adverse):
    print(f"Tour du joueur {joueur}")
    while True:
        try:
            x = int(input("Entrez la coordonnée X (0-7) du tir : "))
            y = int(input("Entrez la coordonnée Y (0-7) du tir : "))
            if not (0 <= x < TAILLE_GRILLE and 0 <= y < TAILLE_GRILLE):
                raise ValueError()
            break
        except ValueError:
            print("Coordonnées invalides. Veuillez réessayer.")

    if grille_adverse[x][y] == CASE_BATEAU:
        print("Coup réussi !")
        grille_adverse[x][y] = CASE_TOUCHE
        return True
    else:
        print("Coup dans l'eau.")
        grille_adverse[x][y] = CASE_EAU
        return False

# Fonction pour vérifier si tous les bateaux ont été coulés
def tous_bateaux_coules(grille):
    return all(CASE_BATEAU not in ligne for ligne in grille)

# Fonction principale pour exécuter le jeu
def bataille_navale():
    print("Bienvenue dans le jeu de bataille navale !")
    grille_joueur = initialiser_grille()
    grille_adverse = initialiser_grille()

    placer_bateaux(grille_joueur)
    placer_bateaux(grille_adverse)

    joueur = 1
    while True:
        afficher_grille(grille_joueur)
        print("\nGrille adverse :")
        afficher_grille(grille_adverse)

        if joueur == 1:
            print("\nJoueur 1, c'est à votre tour !")
            if tour_de_jeu(joueur, grille_adverse):
                if tous_bateaux_coules(grille_adverse):
                    print("Félicitations ! Joueur 1 a gagné !")
                    break
            joueur = 2
        else:
            print("\nJoueur 2, c'est à votre tour !")
            if tour_de_jeu(joueur, grille_joueur):
                if tous_bateaux_coules(grille_joueur):
                    print("Félicitations ! Joueur 2 a gagné !")
                    break
            joueur = 1

# Lancer le jeu
bataille_navale()
