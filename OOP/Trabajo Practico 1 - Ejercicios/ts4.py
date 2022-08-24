"""
Crear una función que tome dos listas y determine si existe lo que en poker se denomina “color” (cinco cartas del mismo palo). 
La primer lista son las 5 cartas repartidas en la mesa. 
La segunda lista representa 2 cartas en tu mano. Notación: número y palo de la carta 
(S = Espadas, H = Corazones, D = Diamantes, C = Picas) separados por un guion bajo.
check_flush(["A_S", "J_H", "7_D", "8_D", "10_D"], ["J_D", "3_D"]) ➞ True // diamantes
check_flush(["10_S", "7_S", "9_H", "4_S", "3_S"], ["K_S", "Q_S"]) ➞ True // espadas
check_flush(["3_S", "10_H", "10_D", "10_C", "10_S"], ["3_S", "4_D"]) ➞ False

"""

def check_flush(lista1, lista2):
	#Lo primero que hago es sumar las listas asi tengo una sola para evaluar todos los palos
	lista3 = lista1 + lista2

	#creo una lista filtrando solo palos, para ello accedo al ultimo valor de cada cadena en la lista
	#ejemplo lista3 --> lista3 = ["A_S", "J_H", "7_D", "8_D","10_D","J_D","3_D"]
	#ejemplo filtrado --> ['S', 'H', 'D', 'D', 'D', 'D', 'D']
	lista_palos = [cadena[-1] for cadena in lista3]

	#pueba de escritorio
	#print(lista_palos)

	#creamos un diccionario a partir de la lista de palos
	#donde cada clave sera el palo y el valor sera la cantidad de veces que se repite
	#ejemplo lista_palos --> ['S', 'H', 'D', 'D', 'D', 'D', 'D']
	#ejemplo diccionario de palos --> {'S': 1, 'H': 1, 'D': 5}
	cantidad_palos = { palo : (lista_palos.count(palo)) for palo in lista_palos } 

	#pueba de escritorio
	#print(cantidad_palos)

	#Inicializamos la variable color como False
	#cambiara de valor solo si la cantidad de palos es mayor o igual a 5
	color = False

	#iteramos sobre el diccionario buscando si hay color
	for palo, cantidad in cantidad_palos.items():
		#si logramos "color" (cinco cartas del mismo palo)
		if cantidad >= 5:
			#cambiamos el valor de la variable color y retornamos True
			color = True
			return color 
	
	#En caso no encontrar "color" se devolvera la variable con su valor inicial que es False
	return color


print(check_flush(["A_S", "J_H", "7_D", "8_D", "10_D"], ["J_D", "3_D"])) #➞ True // diamantes
print(check_flush(["10_S", "7_S", "9_H", "4_S", "3_S"], ["K_S", "Q_S"])) #➞ True // espadas
print(check_flush(["3_S", "10_H", "10_D", "10_C", "10_S"], ["3_S", "4_D"])) #➞ False	






