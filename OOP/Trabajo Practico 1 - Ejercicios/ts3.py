"""
Crear una función que permita realizar una operación aritmética que incluya adición, sustracción, multiplicación y división teniendo como parámetro de la función los siguientes ejemplos: “12 + 24” , “23 - 21”, “12 // 12”, “12 * 21”
En el caso de la división por cero, retornar -1 o algún mensaje que diga que no se puede realizar la operación.

operacion_aritmetica("12 + 12") ➞ 24 // 12 + 12 = 24
operacion_aritmetica("12 - 12") ➞ 24 // 12 - 12 = 0
operacion_aritmetica("12 * 12") ➞ 144 // 12 * 12 = 144
operacion_aritmetica("12 // 0") ➞ -1 // 12 / 0 = -1

"""

def operacion_aritmetica(argumento):

      #lo primero es quitar los espacios del string con el metodo split()
      #y quedarnos con los valores que realmente necesitamos
      cadena = argumento.split() # salida --> ['12', '+', '12'] 
      """
      ahora preguntamos si la operacion se encuentra en la cadena
      Si lo encuentra, vamos a realizar la operacion con el primer valor
      y el ultimo:
      cadena[0] = "12" --> lo pasamos a int --> 12
      cadena[-1] = "12" --> lo pasamos a int --> 12
      ahora que podemos operar, realizamos la operacion
      y asi vamos con todos los casos
      """
      if "+" in cadena:
        print(int(cadena[0]) + int(cadena[-1]))
      elif "-" in cadena:
        print(int(cadena[0]) - int(cadena[-1]))
      elif "*" in cadena:
        print(int(cadena[0]) * int(cadena[-1]))
      elif "/" in cadena:
        if int(cadena[-1]) == 0:
          print(-1)
        else:  
          print(float(cadena[0]) / float(cadena[-1]))
      else:
          print("No ingreso ningun signo para operar")    


operacion_aritmetica("12 + 12") #➞ 24 // 12 + 12 = 24
operacion_aritmetica("12 - 12") #➞ 24 // 12 - 12 = 0
operacion_aritmetica("12 * 12") #➞ 144 // 12 * 12 = 144
operacion_aritmetica("12 / 0") #➞ -1 // 12 / 0 = -1
