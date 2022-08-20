def ajouter(db):
	no = input("veuillez saisir le numero de l'eleve: ")
	nom = input("veuillez saisir le nom de l'eleve: ")
	engl = float(input("veuillez saisir les point du cours englais: "))
	maths = float(input("veuillez saisir les point du cours maths: "))
	eleve = {
		"no": no,
		"nom": nom,
		"engl": engl,
		"maths": maths
	}
	db.append(eleve)

def lister(db):
	for el in db:
		print(
			el['no'],"\t",
			el['nom'],"\t",
			el['engl'],"\t",
			el['maths']
		),

def rechercher(db):
	print("vous avez choisi de rechercher")

def modifier(db):
	no = input("veuillez saisir le numero de l'eleve: ")
	eleve = None
	index = -1
	for i, el in enumerate(db):
		if el["no"] == no:
			eleve = el
			index = i
			break
	if index != -1:
		nom = input("Nouveau nom: ")
		engl = input("Nouveau points engl: ")
		maths = input("Nouveau points maths: ")
		el = {
			"no": no,
			"nom": nom if nom else eleve["nom"],
			"engl": float(engl) if engl else eleve["engl"],
			"maths": float(maths) if maths else eleve["maths"]
		}
		db[index] = el
	else:
		print("l'eleve n'existe pas")

def supprimer(db):
	print("vous avez choisi de supprimer")