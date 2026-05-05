from datetime import datetime

class Empleado:
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
        self.dietas = 0

    # Los métodos son funciones con "self"
    def presentarse(self):
        print(
            f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        print("Biip, Biiiiip")
        self.dietas += 1
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
        self.sueldo_hora += float(input("En cuánto quieres incrementar el sueldo: "))
        print(f"Se ha asignado a {self.nombre} {self.apellido1} {self.sueldo_hora}€/h")

    def calcula_sueldo(self):
        horas_trabajadas = self.calcula_tiempo_trabajado() / 3600
        sueldo_horas = horas_trabajadas * self.sueldo_hora
        sueldo_total = sueldo_horas + self.dietas
        return sueldo_total
    
class Directivo(Empleado):
    pass
    
class Oficinista(Empleado):
    pass
    
class Peon(Empleado):
    pass


if __name__ == "__main__":
    import time
    director = Directivo('Juan', 'Pérez', 'López')
    secretario = Oficinista('Juanito', 'Pérez', 'García')
    soldador = Peon("Luis", "Gómez")

    ### Pruebas Directivo
    director.ficha()
    time.sleep(2)
    director.ficha()
    print("Tiempo trabajado:", director.calcula_tiempo_trabajado())
    print("Dietas:", director.dietas)

    print("Sueldo:", director.calcula_sueldo())
    director.asigna_sueldo()
    print("Sueldo:", director.calcula_sueldo())

    director.asigna_coche("Mercedes", "Maybach", 6.70, 80000)

    director.coche.saludar()

    print(director.coche)

    ### Pruebas Oficinista
    secretario.ficha()
    time.sleep(2)
    secretario.ficha()
    print("Tiempo trabajado:", secretario.calcula_tiempo_trabajado())
    print("Dietas:", secretario.dietas)

    print("Sueldo:", secretario.calcula_sueldo())
    secretario.asigna_sueldo()
    print("Sueldo:", secretario.calcula_sueldo())

    secretario.asignar_bonus()
    secretario.asignar_bonus()

    print("Sueldo:", secretario.calcula_sueldo())

    ### Pruebas Peón soldador
    soldador.ficha()
    time.sleep(2)
    soldador.ficha()
    print("Tiempo trabajado:", soldador.calcula_tiempo_trabajado())
    print("Dietas:", soldador.dietas)

    print("Sueldo:", soldador.calcula_sueldo())
    soldador.asigna_sueldo()
    # soldador.__sueldo_hora = 10000
    print("Sueldo:", soldador.calcula_sueldo())

    print(soldador.guardias)