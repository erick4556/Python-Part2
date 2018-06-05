class Animal:
	@property
	def terrestre(self):
		return True



class Felino(Animal): #clase padre..
	@property
	def garras_retractiles(self):
		return 'Garras'

	def cazar(self):
		print("El felino esta cazando")	

	def hi(self):
		print("Hola")	


class Mascota:
	#nombre = 'Lola'

	def mostrar_nombre(self):
		print(self.nombre)

		

	@property
	def sal(self):
		return self.hi()
		

class Gato(Felino,Mascota):
	def gato_bandido(self):
		self.cazar()


gato = Gato()
fe = Felino()

gato.nombre="Scoby doo"
gato.mostrar_nombre()
print(gato.terrestre)
gato.cazar()
gato.gato_bandido()
print(fe.garras_retractiles)
gato.sal


