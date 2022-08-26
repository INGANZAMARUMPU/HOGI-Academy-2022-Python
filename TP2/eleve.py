class Eleve:
	def __init__(self, no, fullname, maths, engl, sexe):
		self.no = no
		self.fullname = fullname
		self.maths = maths
		self.engl = engl
		self.sexe = sexe

	def total(self):
		return float(self.engl) + float(self.maths)

	def moyenne(self):
		return self.total()/2

	def __str__(self):
		return f"No.{self.no} {self.fullname}"