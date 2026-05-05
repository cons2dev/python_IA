#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:46:48 2023

@author: laptop
"""

####################################
# Programación Orientada a Objetos #
####################################
# Creamos una aplicación para gestionar el "Personal" de una empresa

from datetime import datetime
datetime.now()
#----------------------------------
# Etapa1: Creo una clase "Persona"
#----------------------------------

class Persona:
    def __init__(self, nombre, apellido1, apellido2=""):
        # Características
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        # Estados
        self.trabajando = False
        self.ubicacion = "Rentería"

    # Los métodos son funciones con "self"
    def presentarse(self):
        print(
            f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        print("Biip, Biiiiip")
        self.trabajando = not self.trabajando

    def viaja(self, nueva_ubicacion):
        print(f"{self.ubicacion} -----> {nueva_ubicacion}")
        self.ubicacion = nueva_ubicacion


director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')

print(type(director))
print(type(secretario))

director.presentarse()
secretario.presentarse()

secretario.trabajando
print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")

secretario.ficha()

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Dónde está el director? {director.ubicacion}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
print(f"¿Dónde está el secretario? {secretario.ubicacion}")

director.viaja("Albacete")
director.ubicacion

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Dónde está el director? {director.ubicacion}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
print(f"¿Dónde está el secretario? {secretario.ubicacion}")


#----------------------------------------------------------
# Etapa1: Vamos a llevar una contabilidad de los fichajes
#----------------------------------------------------------

class Persona:
    def __init__(self, nombre, apellido1, apellido2=""):
        # Características
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        # Estados
        self.trabajando = False
        self.ubicacion = "Rentería"
        self.fichajes = []

    # Los métodos son funciones con "self"
    def presentarse(self):
        print(
            f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        print("Biip, Biiiiip")
        self.trabajando = not self.trabajando
        self.fichajes.append(datetime.now())

    def viaja(self, nueva_ubicacion):
        print(f"{self.ubicacion} -----> {nueva_ubicacion}")
        self.ubicacion = nueva_ubicacion


director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')
director.fichajes
secretario.ficha()
secretario.trabajando


#----------------------------------------------------------
# Etapa2: Vamos a llevar una contabilidad del tiempo trabajado
#----------------------------------------------------------
from datetime import timedelta, datetime
entrada = datetime.now()
salida = datetime.now()
intervalo = salida - entrada
intervalo_dia = intervalo + timedelta(1)
type(intervalo_dia.total_seconds())
intervalo_dia.days


class Persona:
    def __init__(self, nombre, apellido1, apellido2=""):
        # Características
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        # Estados
        self.trabajando = False
        self.ubicacion = "Rentería"
        self.fichajes_entrada = []
        self.fichajes_salida = []

    # Los métodos son funciones con "self"
    def presentarse(self):
        print(
            f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        print("Biip, Biiiiip")
        self.trabajando = not self.trabajando
        if self.trabajando:
            self.fichajes_entrada.append(datetime.now())
        else:
            self.fichajes_salida.append(datetime.now())

    def viaja(self, nueva_ubicacion):
        print(f"{self.ubicacion} -----> {nueva_ubicacion}")
        self.ubicacion = nueva_ubicacion

    def calcula_tiempo_trabajado(self):
        if not self.fichajes_entrada or not self.fichajes_salida: return 0
        tiempo_total = 0
        for entrada, salida in zip(self.fichajes_entrada, self.fichajes_salida):
            tiempo_total = tiempo_total + (salida - entrada).total_seconds()
        return tiempo_total

director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')

secretario.ficha()
secretario.trabajando
secretario.fichajes_entrada
secretario.fichajes_salida

secretario.calcula_tiempo_trabajado()
director.ficha()
#----------------------------------------------------------
# Etapa3: Vamos a llevar una contabilidad del sueldo acumulado
#----------------------------------------------------------

class Persona:
    def __init__(self, nombre, apellido1, apellido2=""):
        # Características
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        # Estados
        self.trabajando = False
        self.ubicacion = "Rentería"
        self.fichajes_entrada = []
        self.fichajes_salida = []
        self.sueldo_hora = 20

    # Los métodos son funciones con "self"
    def presentarse(self):
        print(
            f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        print("Biip, Biiiiip")
        self.trabajando = not self.trabajando
        if self.trabajando:
            self.fichajes_entrada.append(datetime.now())
        else:
            self.fichajes_salida.append(datetime.now())

    def viaja(self, nueva_ubicacion):
        print(f"{self.ubicacion} -----> {nueva_ubicacion}")
        self.ubicacion = nueva_ubicacion

    def calcula_tiempo_trabajado(self):
        if not self.fichajes_entrada or not self.fichajes_salida: return 0
        tiempo_total = 0
        for entrada, salida in zip(self.fichajes_entrada, self.fichajes_salida):
            tiempo_total = tiempo_total + (salida - entrada).total_seconds()
        return tiempo_total
    
    def asigna_sueldo(self):
        self.sueldo_hora += float(input("Cuánto quieres variar el sueldo"))
        print(f"Se ha asignado a {self.nombre} {self.apellido1} {self.sueldo_hora}€/h")

    def calcula_sueldo(self):
        horas_trabajadas = self.calcula_tiempo_trabajado() / 3600
        return horas_trabajadas * self.sueldo_hora


director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')

secretario.ficha()
secretario.calcula_tiempo_trabajado()

secretario.calcula_sueldo()
secretario.asigna_sueldo(25)

# Crear un método que asigne una dieta de transporte de un euro cada vez que una persona fiche
# Modificar el método que calcula el sueldo para que añada la dieta de transporte.

class Persona:
    pass

director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')

secretario.ficha()
secretario.calcula_tiempo_trabajado()
secretario.dietas

secretario.calcula_sueldo()
secretario.asigna_sueldo()