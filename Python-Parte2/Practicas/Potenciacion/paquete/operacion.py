class Oper:
	def __init__(self,num,cant):
		self.numero = num
		self.cantd = cant

	def potencia(self):
		mul = 1
		for x in range(self.cantd):
			mul = self.numero * mul
		return mul	