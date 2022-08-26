from classe import Classe
import functions

menu = """
Selectionner une action:

(1) Creer un eleve
(2) Lister les eleves
(3) Modifier un eleve
(4) Supprimer un eleve
(5) Chercher un eleve
(0) Quitter:"""

routes = {
	"1": functions.creer,
	"2": functions.lister,
	"3": functions.modifier,
	"4": functions.supprimer,
	"5": functions.chercher,
}

classe = Classe("HOGI SCHOOL OF CODE")

while True:
	choix = input(menu)
	if(choix == '0'): break
	routes[choix](classe)
