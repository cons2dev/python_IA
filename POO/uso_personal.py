from personal import Directivo, Oficinista

director = Directivo('Juan', 'Pérez', 'López')
secretario = Oficinista('Juanito', 'Pérez', 'García')

secretario.ficha()
secretario.ficha()
print(secretario.calcula_tiempo_trabajado())

director.ficha()
director.ficha()
print(director.calcula_tiempo_trabajado())

secretario.dietas

lista =[director, secretario]

for empleado in lista:
    print(secretario.calcula_sueldo())
