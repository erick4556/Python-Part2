from ..extra import More
class Multiplicacion(More):
	def __init__(self,numero):
		self.num = numero


	def multi(self):
		n=int(input("Ingresa el numero a multiplicar : "))
		for x in range(self.num+1):
			mul = n * x
			print(x+1,". ",n," x ",x," = ",mul) 	

def mul(val):
	mul = val * 2
	return mul			