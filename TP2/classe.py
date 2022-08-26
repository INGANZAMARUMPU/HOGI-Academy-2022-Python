from eleve import Eleve

class Classe:
	def __init__(self, nom):
		self.nom = nom
		self.eleves:list[Eleve] = []

	def ajouter(self, eleve):
		eleve = self.rechercher(eleve.no)
		if(eleve):
			raise Exception(f"l'eleve No.{eleve.no} existe déjà")
		self.eleves.append(eleve)

	def rechercher(self, id):
		for eleve in self.eleves:
			if eleve.no == id:
				return eleve
		return None

	def supprimer(self, id):
		eleve = self.rechercher(id)
		if(eleve):
			self.eleves.remove(eleve)

	def __str__(self):
		for e in self.eleves:
			print(f"{e.no} {e.fullname} {e.maths} {e.engl} {e.sexe}")

