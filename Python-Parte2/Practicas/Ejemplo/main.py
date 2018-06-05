from part1 import Salario,par,impar,suma

nombre = input("Ingresa nombre :  ")

salario = float(input("Ingresa Salario : "))

obj = Salario(nombre,salario)

obj.operacion()

can =int(input("Ingresa una cantidad : "))

par(can)

print("\n")

impar(can)

suma(can)
 