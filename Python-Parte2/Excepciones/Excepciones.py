try:
 #print(2/0)
 lista = [3,'Hi']
 print(lista[0])
#Cuando no se conoce el error seria...
except Exception as ex: #Cuando pasa un error...
	print(ex)
	print('No se que paso!!!')
#Siempre se va ejecutra...
finally:
	print("Se termino el script!!") 


#Cuando se conoce los errores..
"""except IndexError as ex:
	print(ex)
	print("No se puede obtener la posicion 9!!") 
except ZeroDivisionError as ex: #Colocamos el nombre del error...
 print(ex)
 print('No es posible dividir por 0!!')"""