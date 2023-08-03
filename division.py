numerateur=input("Entrez le numerateur:")
denominateur=input("Entrez le denominateur:")
try:
	resultat=int(numerateur) / int(denominateur)
	print(f"Le resultat est:{resultat}")

except ZeroDivisionError:
	print("Erreur : Division par 0 impossible")

except ValueError:
	print("Erreur : Conversion de type incorrecte")
