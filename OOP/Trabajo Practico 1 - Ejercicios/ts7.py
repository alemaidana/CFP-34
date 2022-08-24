"""
Recibiendo una lista de números, escribir una función que retorne una lista sin números duplicados y ordenados de menor a mayor.
unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]
unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]
unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7]
"""

def unique_sort(lista):

	#lo primero es pasar la lista un conjunto(set) para eliminar los duplicados
	conjunto_lista = set(lista)
	#transformo el set a una lista nuevamente ya que la desventaja de los sets
	#es que no tienen orden
	lista_final = list(conjunto_lista)
	#ordeno la lista con el metodo sort() de la clase list
	lista_final.sort()
	#devuelvo la lista ya sin duplicados y ordenada
	return lista_final

print(unique_sort([1, 2, 4, 3])) #➞ [1, 2, 3, 4]
print(unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2])) #➞ [1, 2, 3, 4]
print(unique_sort([6, 7, 3, 2, 1])) #➞ [1, 2, 3, 6, 7]	

#nota de programador --> se que hay formas mas elegantes de resolver esto
#pero soy un poco vago