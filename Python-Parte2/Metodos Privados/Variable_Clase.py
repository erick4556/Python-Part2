class Circulo:

	pi = 3.1416

	def __init__(self, radio):
		self.radio = radio;
	
	def area(self):
		return self.radio * self.radio * self.pi		

#Si se quiere utilizar la variable clase dentro de la clase se usa la palabra reservada self.			

cir_one = Circulo(4)

cir_two = Circulo(3)

print(cir_one.radio)
print(cir_two.pi)


#print(cir_one.__dict__) #Muestra un diccionario con todos los artibutos de la clase excepto las variables de clase....

print(cir_one.area())

