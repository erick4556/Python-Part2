#import calculadora Forma 1
#from calculadora import (suma, resta, mul, division) Forma 2

 # __name__ Se utiliza para que el script que se esta utilizando sea el principal.

from calculadora import *
from calculadora import __name__ as __name__calculadora__

print(__name__)
print(__name__calculadora__)

if __name__ == '__main__': #Preguntamos si es este el script principal!!.
	print('Es el principal')

n1=int(input("Escribe numero 1 = "))

n2=int(input("Escribe numero 2 = "))


#resultado = calculadora.mul(n1,n2) Forma 1

resultado = suma(n1,n2) + mul(n1,n2)

print("Suma = ",suma(n1,n2),"+ Multipicacion = ",mul(n1,n2)," resultado  = ",resultado)

