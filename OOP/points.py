class Umuntu:
	def __init__(self, nom, adress, age):
		self.nom = nom
		 self.adress = adress
		self.age = age
	
	def __str__(self):
		return f"nitwa {self.nom} mba {self.adress} mfise imyaka {self.age}"

	def kwimuka(self, ahandi):
		self.adress = ahandi

	def gukura(self):
		self.age += 1

jewe = Umuntu("NKURUNZIZA", "Kiganga", 12)
jewe.kwimuka("Gihosha")
print(jewe)
jewe.gukura()
jewe.gukura()
print(jewe)