class Usuario:
	def __init__(self,username,password,email):
		self.username = username
		#__password Atributo privado..
		self.__password = self.__generar_pass(password)
		self.email = email

	#Cifrar el password
	
	def __generar_pass(self,password):
		return password.upper()	

	def get_pass(self):
		return self.__password	


obj = Usuario('Eduardo',"Loco123","ejemplo@hotmail.com")

print(obj.username)
print(obj.get_pass())
print(obj.email)
