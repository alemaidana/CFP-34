"""
Crear una función que tome dos listas y retorne True, si la segunda lista continua el orden de la primer lista y False de lo contrario.
Determina si la segunda lista es la primer lista “movida” en una posición hacia la derecha.
simon_says([1, 2], [5, 1]) ➞ True
simon_says([1, 2], [5, 5]) ➞ False
simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) ➞ True
simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) ➞ False
"""

"""
		Para resolver este problema usamos el slicing
		es una buena herramienta para resolver si la primera
		es continuacion de la segunda
		
		he aqui dos listas

		l1 = [1, 2, 3, 4, 5]

		l2 = [0, 1, 2, 3, 4]

		crearemos dos listas nuevas usando el slice:	
		-una tomando todos los indices sin incluir el ultimo valor
		-otra tomando los valores desde el primer indice
		
		-nota del programador:
		(todo esto si las listas son del mismo tamaño, )
		"""


def simon_says(lista1, lista2):	
		
    lista_normal = lista1[:-1] #[1, 2, 3, 4] excluimos el 5
    lista_movida = lista2[1:] #[1, 2, 3, 4] excluimos el 0

	#ahora preguntamos si la lista movida es una continuacion
	#de la lista normal movida una posicion a la derecha
    return lista_movida == lista_normal


print(simon_says([1, 2], [5, 1])) #➞ True
print(simon_says([1, 2], [5, 5])) #➞ False
print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4])) #➞ True
print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3])) #➞ False	