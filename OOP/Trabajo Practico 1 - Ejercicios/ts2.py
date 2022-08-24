"""
same_length("110011100010") ➞ True
same_length("101010110") ➞ False
same_length("111100001100") ➞ True
same_length("111") ➞ False
"""

#tenemos la cadena
cadena = "110011100010"

#con el metodo split filto por 0 o por 1 y formo dos listas nuevas
a = cadena.split("1") 
b = cadena.split("0") 

#prueba de escritorio
print(a) #['', '', '00', '', '', '000', '0']
print(b) #['11', '', '111', '', '', '1', '']

#ahora filto solo los elementos que no son espacio
d = [elemento for elemento in a if elemento != '']
e = [elemento for elemento in b if elemento != '']

#prueba de escritorio
print(d) #['00', '000', '0']
print(e) #['11', '111', '1']

#obtengo la cantidad de elementos agrupados
f = [len(elemento) for elemento in d]
g = [len(elemento) for elemento in e]

#prueba de escritorio
print(f) #[2, 3, 1]
print(g) #[2, 3, 1]

#imprimo si f es igual a g
print(f == g)


def same_length(cadena):
	#separo
	a = cadena.split("1") 
	b = cadena.split("0") 
	#limpio
	d = [elemento for elemento in a if elemento != '']
	e = [elemento for elemento in b if elemento != '']
	#obtengo cantidades
	f = [len(elemento) for elemento in d]
	g = [len(elemento) for elemento in e]
	#comparo
	print(f == g)

 
print("*******SALIDA DEL PROGRAMA*********") 
same_length("110011100010") #➞ True
same_length("101010110") #➞ False
same_length("111100001100") #➞ True
same_length("111") #➞ False
