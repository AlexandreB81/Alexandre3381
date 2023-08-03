from random import choice
 
 
COUP = ("Pierre", "Feuille", "Ciseaux")
 
 
while input("Jouez (y/n): ").lower() != "n":
 
    print("\n------------------------------------")
    print("Le jeu du: Pierre - Feuille - Ciseaux")
    print("------------------------------------\n")
 
    a = int(input("Choisissez un chiffre:\n0: Pierre\n1: Feuille\n2: Ciseaux\n-> "))
    b = choice(range(3))
 
    print("\n{} VS {}".format(COUP[a], COUP[b]))
    if a == b:
        print("ÉGALITÉ\n")
    elif (a>b and b+1==a) or (a<b and a+b==2):
        print("VOUS GAGNEZ\n")
    else:
        print("VOUS PERDEZ\n")
else:
    print("Bye Bye")
