# 1. Contador de números pares e impares:
"""
Escribe un programa que utilice un bucle for o while para contar y mostrar 
la cantidad de números pares e impares en un rango específico, 
por ejemplo, del 1 al 100.
"""

cantidad_pares = 0
cantidad_impares = 0
lista_pares = []
lista_impares = []
limite = int(input("Dime el límite: "))


for numero in range(1, limite + 1):
    if numero % 2 == 0:
        cantidad_pares += 1
        lista_pares.append(numero)
    else:
        cantidad_impares += 1
        lista_impares.append(numero)

print("Cantidad de números pares:", cantidad_pares)
print("Cantidad de números impares:", cantidad_impares)


# Lo mismo con while
cantidad_pares = 0
cantidad_impares = 0
lista_pares = []
lista_impares = []
limite = int(input("Dime el límite :"))

numero = 1
while numero <= limite:
    if numero % 2 == 0:
        cantidad_pares += 1
        lista_pares.append(numero)
    else:
        cantidad_impares += 1
        lista_impares.append(numero)
    numero += 1

print("Cantidad de números pares:", cantidad_pares)
print("Cantidad de números impares:", cantidad_impares)



# 2. Suma de números primos:
"""
Crea un programa que solicite al usuario un número y utilice un bucle 
while para sumar todos los números primos menores o iguales al número 
ingresado.
"""
lista_primos = []

numero = 97

candidato_factor = 2
es_primo = True
while candidato_factor < numero:
    if numero % candidato_factor == 0:
        es_primo = False
        break
    candidato_factor +=1
if es_primo:
    lista_primos.append(numero)
print(es_primo)



limite = int(input("Introduce el límite de los primos: "))

numero = 2
lista_primos = []
suma_primos = 0
while numero < limite:
    candidato_factor = 2
    es_primo = True
    while candidato_factor < numero:
        if numero % candidato_factor == 0:
            es_primo = False
            break
        candidato_factor +=1
    if es_primo:
        lista_primos.append(numero)
        suma_primos = suma_primos + numero
    numero +=1
print(lista_primos)
print(suma_primos)





# 3. Tabla de multiplicar:
"""
Pide al usuario que ingrese un número y luego muestra la tabla de 
multiplicar de ese número del 1 al 10 utilizando un bucle for.
"""
numero = int(input("Ingrese un número: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)


# 4. Generador de patrones:
"""
Escribe un programa que solicite al usuario un número y utilice 
un bucle for o while para generar patrones como el siguiente, donde 
el número ingresado determine la cantidad de filas:
"""
1
22
333
4444
55555
numero = int(input("Ingrese un número: "))

for i in range(1, numero+1):
    patron = str(i) * i
    print(patron)

# 5. Adivina el número:
"""
Crea un juego en el que el programa genera un número aleatorio y el 
usuario tiene que adivinarlo. Utiliza un bucle while para que el usuario 
pueda seguir intentando hasta que adivine el número. Proporciona pistas 
para indicar si el número a adivinar es mayor o menor que el intento del 
usuario.
"""
from random import randint

# Generar un número aleatorio entre 1 y 100
numero_aleatorio = randint(1, 100)

# Pedir al usuario que adivine el número
while True:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    if intento == numero_aleatorio:
        print("¡Correcto! Adivinaste el número.")
        break
    elif intento < numero_aleatorio:
        print("El número a adivinar es mayor que", intento)
    else:
        print("El número a adivinar es menor que", intento)

