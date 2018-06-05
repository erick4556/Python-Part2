import random

valor = random.randint(0,10) #Va tirar un numero de aleaotrio entre el 0 y el 10....

#print(valor)

lista = [True,'String', 23, False, "Hi"]

valor2 = random.choice(lista)

#print (valor2)

print(lista)

random.shuffle(lista) #Ordenar de una forma random...

print (lista)