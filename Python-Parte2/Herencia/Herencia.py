class Animal:
	@property
	def terrestre(self):
		return "Terrestre"

	@property
	def aereo(self):
		#print("gato aereo")
		return "gato aereo"
	


class Felino(Animal): #clase padre..
	@property
	def garras_retractiles(self):
		return 'Garras'

	def cazar(self):
		print("El felino esta cazando")	

	def extra(self):
		print('Ejemplo')	


class Gato(Felino):
	def gato_bandido(self):
		self.cazar()

	@property	
	def extra2(self):
		self.extra()

	@property
	def nariz(self):
		return 'Nariz'	


class Jaguar(Felino):
	pass


gato = Gato()

jag = Jaguar() 	


print(gato.gato_bandido())
print(gato.terrestre)
print(jag.garras_retractiles)
gato.extra2
print(gato.aereo)
print(gato.nariz)



