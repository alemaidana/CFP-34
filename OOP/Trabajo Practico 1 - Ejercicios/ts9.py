"""
Crear una función que retorne la suma de todos los presupuestos de las personas (budget).
get_budgets([
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
]) ➞ 65700

get_budgets([
  { "name": "John",  "age": 21, "budget": 29000 },
  { "name": "Steve",  "age": 32, "budget": 32000 },
  { "name": "Martin",  "age": 16, "budget": 1600 }
]) ➞ 62600
"""

def get_budgets(lista_diccionarios):
	#usaremos esta variable para ir sumando los presupuestos de las personas
	total_presupuesto = 0

	#recorreremos cada diccionario en la lista de diccionarios
	for diccionario in lista_diccionarios:
		#en presupuesto almacenamos cada presupuesto
		#accediendo de forma individual a ese diccionario
		#ejemplo --> lista_diccionarios[0]["budget"] = 23000 
		presupuesto = diccionario["budget"]
		#vamos realizando la sumatoria de presupuestos
		total_presupuesto += presupuesto

	#retornamos el presupuesto final, o sea la sumatoria de los mismos
	return total_presupuesto
	

print(get_budgets([
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
]))# ➞ 65700

print(get_budgets([
  { "name": "John",  "age": 21, "budget": 29000 },
  { "name": "Steve",  "age": 32, "budget": 32000 },
  { "name": "Martin",  "age": 16, "budget": 1600 }
])) #➞ 62600

