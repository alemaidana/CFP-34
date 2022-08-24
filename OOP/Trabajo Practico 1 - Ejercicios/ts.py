#Tengo la lista
lista = ["cow", "pig", "cow", "cow"]

#La transformo a un diccionario para ver cuantas repeticiones hay
dict_lista = { elemento : lista.count(elemento) for elemento in lista }

#imprimo como prueba de escritorio
#print(dict_lista) #Salida --> {'cow': 3, 'pig': 1}

#agregado nos va a devolver la palabra con "s" si su valor es mayor a 1, lo cual nos dice
#que se repite
agregado = { (key + "s" if value > 1 else key): value for (key, value) in dict_lista.items()}

#imprimimos el diccionario como un conjunto
print(set(agregado))

#Funcion final
def pluralize(lista_repetidos):
	#transformamos la lista a un diccionario para chequear repeticiones
	dc = { elemento : lista_repetidos.count(elemento) for elemento in lista_repetidos }
	#ahorramos codigo devolviendo en una sola salida
	print(set({ (key + "s" if value > 1 else key): value for (key, value) in dc.items()}))


#Salidas
pluralize(["cow", "pig", "cow", "cow"])# ➞ { "cows", "pig" }
pluralize(["table", "table", "table"]) #➞ { "tables" }
pluralize(["chair", "pencil", "arm"]) #➞ { "chair", "pencil", "arm" }







