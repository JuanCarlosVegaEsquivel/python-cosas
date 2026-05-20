print("Hola Mundillo")

# Asi se realizan comentarios

"""
Este es un 
comentario de varias lineas
"""

name = "Juan"        #Tipo de dato string
edad = 20            #Tipo de dato entero
altura = 1.75        #Tipo de dato float
es_estudiante = True #Tipo de dato booleano
nada = None          #Valor nulo

"""
Tipos Principales

Int: 5, -3, 1000                                         #Números enteros
float: 3.14, -0.001, 2.0                                 #Números con decimales
str: "Hola", 'Mundo', "123"                              #texto entre comillas
bool: True, False                                        #Valores booleanos
None: None                                               #Valor nulo
list: [1, 2, 3], ["a", "b", "c"]                         #Colección ordenada y mutable
dict: {"clave": "valor"}, {"nombre": "Juan", "edad": 20} #Colección de pares clave-valor

Para saber el tipo de dato o de algo: type (variable).
"""

# Mostrar texto es con print("Texto a mostrar")
print("Mi nombre es:", name)
print("Tengo", edad, "años")
print("Mi altura es:", altura)
print("¿Soy estudiante?", es_estudiante)
print("Valor de nada:", nada)

# f-strings (la forma moderna y recomendada de meter variables en texto):

print(f"Me llamo {name} y tengo {edad} años.")
# Tambien puedes hacer calculos adentro:
print(f"El año que viene tendré {edad + 1} años.")

# para pedir texto se usa el input()
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola, {nombre}!")

# input() siempre devuelve un string, si quieres un numero debes convertirlo:
edad_input = input("¿Cuántos años tienes? ")  # Esto es string
edad2 = int(edad_input)                       # Convertir el string a un entero
print(f"En 5 años tendrás {edad2 + 5} años.") 

"""
Operaciones matematicas:

suma = 5 + 3              # Resultado: 8
resta = 10 - 4            # Resultado: 6
multiplicacion = 7 * 2    # Resultado: 14
division = 20 / 5         # Resultado: 4.0 (siempre devuelve un float)
division_entera = 20 // 3 # Resultado: 6   (división sin decimales)
modulo = 10 % 3           # Resultado: 1   (resto de la división)
potencia = 2 ** 3         # Resultado: 8   (2 elevado a la 3)
"""

# Operadores de asignación:
contador = 0
contador += 1  # Equivale a: contador = contador + 1
contador -= 1
contador*= 2
contador /= 2

print(f"El contador vale: {contador}")

"""
Funciones utiles

abs(-5)      #5 (valor absoluto)
round (3.7)  #4 (redondea al entero mas cercano)
round(3.14159)  #3.14 a 2 decimales
min(3, 1, 4) #1
max(3, 1, 4) #4

si se desea mas matematicas avanzadas se puede importar la libreria math:
import math
math.sqrt(16)  #4.0 (raiz cuadrada)
math.pi        #3.141592653589793 (valor de pi)
"""

saludo = "Hola Humano!"

len(saludo) #11 (longitud)
saludo.upper() #"HOLA HUMANO!" (mayusculas)
saludo.lower() #"hola humano!" (minusculas)
saludo.replace("Hola", "Adios") #"Adios Humano!" (reemplaza texto)
saludo.split() #["Hola", "Humano!"] (lo divide en una lista)

# Acceder a caracterers por posicion (empiza en 0)
saludo[0]   #"H"
saludo[-1]  # "o" (ultimo caracter)
saludo[0:4] # ["Hola"] (rebanada: del 0 al 4 sin incluir el 4)

# Unir strings
nombre = "Juan"
apellido = "Vega"
completo = nombre + " " + apellido #"Juan Vega"
print(completo)

