"""
Spyder Editor

This is a temporary script file.
"""

# 1. Calculadora Simple:
"""
Crea una función que pueda realizar operaciones básicas como suma, resta, 
multiplicación y división. 
Pedirá al usuario elegir una operación a partir de un listado y luego pedirá los valores a operar.


Utiliza funciones separadas para cada operación.
"""
def pedir_opcion():
    opcion = ""
    while opcion not in ["1", "2", "3", "4", "s"]:
        print("""
        Elige la operación a realizar:
        1 = Suma
        2 = Resta
        3 = Multiplicación
        4 = División
        s = salir
        """)
        opcion = input("Introduce una opción: ")
        return opcion

def pedir_numeros():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    return num1, num2

def calculadora():
    opcion = pedir_opcion()
    if opcion != "s":
        num1, num2 = pedir_numeros()
        if opcion == "1":
            resultado = num1 + num2
        elif opcion == "2":
            resultado = num1 - num2
        elif opcion == "3":
            resultado = num1 * num2
        elif opcion == "4":
            resultado = num1 / num2
    else:
            resultado = "Adios"
    print(resultado)

calculadora()




# 2. Número Primo:
"""
Escribe una función que determine si un número dado es primo o no. 
Pedirá al usuario que ingrese un número y muestra un mensaje 
indicando si es primo o no.
"""

def primo(numero):
    candidato_factor = 2
    while candidato_factor < numero:
        if numero % candidato_factor == 0:
            return False
        candidato_factor +=1
    return True

def pregunta_primo():
    numero = int(input("Dame un número entero y te digo si es primo: "))
    if primo(numero):
        print("Es primo")
    else:
        print("No es primo")

primo(98)
pregunta_primo()

# 3. Cálculo del Área:
"""
Implementa funciones para calcular el área de diferentes formas geométricas 
como círculo, cuadrado y triángulo. Pide al usuario que elija la forma y 
luego ingrese los valores necesarios.
"""
def pedir_opcion():
    opcion = ""
    while opcion not in ["1", "2", "3", "s"]:
        print("""
        Opcion
            1 : Circulo
            2 : Cuadrado
            3 : Triángulo
            s: Salir
        """)
        opcion = input("Introduzca una opcion: ")
    return opcion

from math import pi

def area_cir():
    radio = float(input("Dame el radio: "))
    return radio**2*pi

def area_cuad():
    lado = float(input("Dame el lado: "))
    return lado**2

def area_triang():
    base = float(input("Dame la base: "))
    altura = float(input("Dame la altura: "))
    return base*altura/2

def medidor():
    opcion = pedir_opcion()
    if opcion == "s":
        print("Adiós")
        return
    operacion = {"1": area_cir, "2": area_cuad, "3": area_triang}
    print(operacion[opcion]())

medidor()

# 4. Inversión de Cadena:
"""
Crea una función que tome una cadena como entrada y devuelva la cadena invertida. 
Por ejemplo, si la entrada es "python", la salida debería ser "nohtyp".
"""
def inversor(cadena):
    invertida = ""
    for letra in cadena:
        invertida = letra + invertida
    return invertida

inversor("python")


cadena = "python"

cadena[::-1]



# 5. Contador de Palabras:
"""
Desarrolla una función que cuente el número de palabras en una oración. 
Pide al usuario que ingrese una oración y muestra el resultado.
"""

texto_entrante = """Crea una función    que tome una cadena como entrada y devuelva la cadena invertida. 
Por ejemplo, si la       entrada es "python", la salida debería ser "nohtyp"."""


def cuenta_palabras(texto):
    while "  " in texto:
        texto = texto.replace("  ", " ")
    signos = ",.¿?\n"
    for signo in signos:
        texto = texto.replace(signo, "")
    lista = texto.split(" ")
    print(lista)
    return len(lista)

cuenta_palabras(texto_entrante)


# 6. Fibonacci:
"""
Implementa una función para generar los primeros n números de la 
secuencia de Fibonacci. Pide al usuario que ingrese el valor de n.
"""

def fibo(n: int) -> list:
    if n == 1:
        serie =[0]
    else:
        serie = [0,1]
    seguidor = 2
    while seguidor < n:
        termino = serie[-2] + serie[-1]
        serie.append(termino)
        seguidor += 1
    return serie

def fibo(n: int) -> list:
    if n == 1:
        serie =[0]
    else:
        serie = [0,1]
    for _ in range(2,n):
        termino = serie[-2] + serie[-1]
        serie.append(termino)
    return serie

fibo(3)


# 8. Factorial:
"""
Crea una función para calcular el factorial de un número. 
Pide al usuario que ingrese un número y muestra el resultado.
"""

def factorial(num):
    resultado = 1
    for termino in range(2,num+1):
        resultado = resultado*termino
    return resultado

factorial(150000056)

# 9. Conversión de Temperatura:
"""
Implementa funciones para convertir entre Celsius y Fahrenheit. 
Pide al usuario que ingrese la temperatura y la unidad, y luego 
realiza la conversión.
"""

def f_a_c(fah):
    return (fah - 32)*5/9

def c_a_f(cel):
    return cel*9/5 + 32

def pedir_opcion():
    opcion=""
    while opcion not in ("F", "C", "s"):
        print("""
              C: Grados Centígrados
              F: Grados Fahrenheit
              s: Salir
              """)
        opcion = input("¿En qué unidades está la temperatura?: ")
    return opcion

def pedir_temperatura():
    return float(input("Temperatura: "))

def conversor():
    opcion = pedir_opcion()
    match opcion:
        case "C":
            print(c_a_f(pedir_temperatura()))
        case "F":
            print(f_a_c(pedir_temperatura()))
        case _:
            print("Adios")
            return

conversor()


# 10. Juego de Adivinanzas:
"""
Desarrolla un juego simple en el que el programa elige un número aleatorio 
y el jugador tiene que adivinarlo. 
Proporciona pistas sobre si el número es mayor o menor. 
Utiliza funciones para organizar el código.
"""


