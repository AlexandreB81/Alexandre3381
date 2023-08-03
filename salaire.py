numerateur=input("Entrez le salaire annuel net:")
denominateur=input("Entrez le nombre de mois travaillés:")
try:
	resultat=int(numerateur) / int(denominateur)
	print(f"Le resultat est:{resultat} euros net mensuels")

except ZeroDivisionError:
	print("Erreur : Division par 0 impossible")

except ValueError:
	print("Erreur : Conversion de type incorrecte")