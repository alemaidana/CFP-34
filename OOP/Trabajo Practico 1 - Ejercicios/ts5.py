"""
Un número es “Disarium” si la suma de los dígitos elevados a su respectiva posición da como resultado el mismo número en sí mismo. Crear una función que determine si un número es o no “Disarium”.
is_disarium(75) ➞ False # 7^1 + 5^2 = 7 + 25 = 32
is_disarium(135) ➞ True # 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
is_disarium(544) ➞ False
is_disarium(518) ➞ True
is_disarium(466) ➞ False
is_disarium(8) ➞ True

"""

def is_disarium(argumento):

	#Lo primero es convertir el argumento a cadena para poder iterar sobre el
	argumento_cadena = str(argumento)
	#definimos variable para elevar cada numero en el ciclo
	i = 1
	#aqui en variable final tendremos la sumatoria de cada ciclo
	final = 0

	#mediante un for recorremos la cadena
	for numero in argumento_cadena:
		#realizamos la operacion de elevar numero a su respectiva posicion
		total = int(numero) ** i
		#vamos sumando en final el resultado
		print(total)
		final += total
		#en cada vuelta le sumamos una posicion al numero
		i+=1

	#imprimimos si la sumatoria es de los digitos elevados a su posicion
	#es igual al numero 
	print(final)
	print(final == int(argumento_cadena))	


is_disarium(75) #➞ False # 7^1 + 5^2 = 7 + 25 = 32
is_disarium(135) #➞ True # 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
is_disarium(544) #➞ False # 5^1 + 4^2 + 4^3 = 5 + 16 + 64 = 85
is_disarium(518) #➞ True # 5^1 + 1^2 + 8^3 = 5 + 1 + 512 = 518
is_disarium(466) #➞ False # 4^1 + 6^2 + 6^3 = 4 + 36 + 216 = 256
is_disarium(8) #➞ True 8^1 = 8 = 8
