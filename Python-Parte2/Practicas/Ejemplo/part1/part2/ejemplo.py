class Salario:
	def __init__(self,nombre,salario):
		self.nom = nombre
		self.sal = salario

	def operacion(self):
		if self.sal <= 500:
			salto = self.sal - (self.sal * 0.03)
			print("Nombre : ",self.nom," - Salario : ",self.sal," - Salario total : ",salto)
		elif self.sal >500:
			salto = self.sal - (self.sal * 0.05)
			print("Nombre : ",self.nom," - Salario : ",self.sal," - Salario total : ",salto)

def par(val):
	for x in range(val):
		if x%2==0:
			print(x+1,". Par : ",x)					