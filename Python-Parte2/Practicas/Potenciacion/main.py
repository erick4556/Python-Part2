from paquete import Oper


num = int(input("Ingresa el numero a elevar : "))
cant = int(input("Ingresa la cantidad de la potencia : "))

obj = Oper(num,cant)

print("Resultado :",obj.potencia())