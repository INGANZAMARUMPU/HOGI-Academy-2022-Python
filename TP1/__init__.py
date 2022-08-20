from functions import *

db = []

while True:
	choix = input("""
Vous voulez:
(1) Ajouter
(2) modifier
(3) supprimer
(4) Rechercher
(5) Lister
(0) pour terminer: """
	)

	if(choix == "1"):
		ajouter(db)
	elif(choix == "2"):
		modifier(db)
	elif(choix == "3"):
		supprimer(db)
	elif(choix == "4"):
		rechercher(db)
	elif(choix == "5"):
		lister(db)
	else:
		break