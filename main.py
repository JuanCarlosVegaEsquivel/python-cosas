print("Hola Mundillo")

# Asi se realizan comentarios

"""
Este es un 
comentario de varias lineas
"""

name = "Juan"         #Tipo de dato string
edad = 20             #Tipo de dato entero
altura = 1.73         #Tipo de dato float
es_estudiante = False #Tipo de dato booleano
nada = None           #Valor nulo

"""
Tipos Principales

Int: 5, -3, 1000                                         #Números enteros
float: 3.14, -0.001, 2.0                                 #Números con decimales
str: "Hola", 'Mundo', "123"                              #texto entre comillas
bool: True, False                                        #Valores booleanos
None: None                                               #Valor nuloS
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

saludo = "Hola Humano"

print(len(saludo)) #11 (longitud)
print(saludo.upper()) #"HOLA HUMANO" (mayusculas)
print(saludo.lower()) #"hola humano" (minusculas)
print(saludo.replace("Hola", "Adios")) #"Adios Humano" (reemplaza texto)
print(saludo.split()) #["Hola", "Humano"] (lo divide en una lista)

# Acceder a caracterers por posicion (empiza en 0)
print(saludo[0])   #"H"
print(saludo[-1])  # "o" (ultimo caracter)
print(saludo[0:4]) # ["Hola"] (rebanada: del 0 al 4 sin incluir el 4)

# Unir strings
nombre = "Juan"
apellido = "Vega"
completo = nombre + " " + apellido #"Juan Vega"
print(completo)

"""
Condicionales: if, elif, else

Sirven para que el programa tome decisiones. Fijarse en los dos puntos: y la identacion.
"""

edad = int(input("¿Cuántos años tienes? "))

if edad < 18:
    print("Menos de edad")
elif edad < 65:
    print("Eres adulto")
else:
    print("Eres adulto mayor")

"""
Operadores de comparación:(devuelven True o False)
== (igual)
!= (distinto)
<  (menor)
>  (mayor)
<= (menor o igual)
>= (mayor o igual)
"""

# Operadores logicos para combinar condiciones

edad = 20
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puede conducir")
if edad < 18 or not tiene_licencia:
    print("No puede conducir")

# and -> ambas deben ser verdadereas
# or  -> al menos una debe ser verdadera
# not -> invierte el valor (True a False, False a True)

# BUCLES: REPETIR COSAS
# while -- mientras se cumpla una condicion

contador = 0
while contador <5:
    print(contador)
    contador += 1 # Esto es importante para evitar un bucle infinito.

# for -- recorrer una secuencia

# Recorre un rango de numeros

print("Numeros del 0 al 4:")
for i in range(5): # 0, 1, 2, 3, 4
    print(i)
    
print("Numeros del 1 al 10:")
for i in range(1, 11): # 1, 2, ..., 10
    print(i)

print("Numeros pares del 0 al 18:")
for i in range(0, 20, 2): #del 0 al 18 de 2 en 2
    print(i)

# Recorrer una lista
print("Recorrer una lista:")
frutas = ["manzana", "pera", "banano"]
for fruta in frutas:
    print(fruta)

    # Recorrer un string letra por letra
print("Recorrer un string letra por letra:")
for letra in "Python":
    print(letra)

# break -> sale del bucle inmediatamente
# continue -> salta a la siguiente iteracion del bucle

for i in range(10):
    if i == 5:
        break # se detiene al llegar a 5
    if i % 2 == 0:
        continue # se salta los numeros pares
    print(i)

# Listas: colecciones ordenadas

numeros = [10, 20, 30, 40]
mezclada = [1,"hola", True, 3.14]

# Acceder por indice (empieza en 0)
numeros[0]   # 10
numeros[-1]  # 40 (ultimo elemento)

# Modificar
numeros[0] = 99 # numeros ahora es [99, 20, 30, 40]

# Agregar o quitar
numeros.append(50)     # agrega al final
numeros.insert(0, 5)   # inserta en posicion 0
numeros.remove(30)     # elimina el valor 30
ultimo = numeros.pop() # quita y devuelve el ultimo

# Otras operaciones utiles
len(numeros)      # cantidad de elementos
30 in numeros     # True o False
numeros.sort()    # ordena la lista
numeros.reverse() # invierte el orden

"""
Diccionarios: colecciones de pares clave-valor
Hay que pensar que sea una agenda: una "clace"(key) que apunta a un "valor"(value).
Se definen con llaves {} y los pares se separan por comas, la clave y el valor se separan por dos puntos.
"""

persona = {
    "nombre": "Carlos",
    "edad": 20,
    "ciudad": "San Jose"
}

# Acceder
persona["nombre"]  # Luis

# Modificar o agregar
persona["edad"] = 21          # Modificar edad
persona["profesion"] = "ingeniero"

# Eliminar
del persona["ciudad"] 

# Recorrer
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Comprobar si existe una clave
if "nombre" in persona:
    print("Tiene nombre")


# Funciones: reutilizar codigo

def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Pedro")
saludar("maria")

#con valor de retorno

def sumar(a, b):
    return a + b
resultado = sumar(3, 4)

# Parametros con valor por defecto

def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

saludar("Ana") # Usa el saludo por defecto
saludar("Ana", "Buenas")

"""
Manejo de Errores: try/except

Aveces el codigo puede fallar (por ejemplo, si pides un numero y el usuario escribe texto).
Para evitar que el programa se caiga, usas try/except:
"""

try:
    edad = int(input("edad: "))
    print(f"Tu edad es {edad}")
except ValueError:
    print("Eso no es un numero valido.")