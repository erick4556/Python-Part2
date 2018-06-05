from part1 import Potencia,nom,par


num = int(input("Ingresa el numero a elevar : "))
can = int(input("Ingresa la elevacion : "))

ob = Potencia(num,can)


print("Resultado de la potencia : ".ob.pot())


ob.cualquiera()


nom("Carlos")

n = int(input("Ingresa el numero a calcular : "))

par(n)