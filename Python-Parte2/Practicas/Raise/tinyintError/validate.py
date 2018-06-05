#El valor debe comprender del 0 al 255..
def validate_tiny_int(val):
	return val >= 0 and val <=255

def validate_val(val):
	try:
		return isinstance(int(val),int) #Retornara verdadero o falso si el valor es entero o no.. int(val) convertir un string a entero..
	except ValueError as error:
		return False	