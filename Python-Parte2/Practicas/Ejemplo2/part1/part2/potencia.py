from ..other import Hello

class Potencia(Hello):

	def __init__(self,a,b):
		self.n = a
		self.e = b

	def pot(self):
		mul = 1
		for in range(self.e):
			mul = mul * self.n
		return mul		