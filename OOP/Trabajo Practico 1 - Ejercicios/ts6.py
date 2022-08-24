"""
Crear una función que eleve al cuadrado cada dígito del número pasado por parámetro.
square_digits(9119) ➞ 811181
square_digits(2483) ➞ 416649
square_digits(3212) ➞ 9414
"""

def square_digits(argumento):

	#pasamos el argumento a string asi podemos iterar sobre cada digito de el
	numero = str(argumento)
	#a esta varible le asignaremos cada digito elevado al cuadrado
	#en cada vuelta del ciclo
	numero_final = ""

	#con el for recorremos el numero
	for num in numero:
		#en esta variable almacenamos cada digito elevado al cuadrado
		resutado = int(num) ** 2
		#el resultado se lo agregamos a la variable numero_final
		numero_final += str(resutado)

	#mostramos el resultado	por pantalla
	print(int(numero_final))	


square_digits(9119) #➞ 811181
square_digits(2483) #➞ 416649
square_digits(3212) #➞ 9414	