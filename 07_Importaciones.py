############################################
# IMPORTACIÓN DE MÓDULOS PERSONALIZADOS    #
############################################

#=== IMPORTACIÓN DE MÓDULOS PERSONALIZADOS ===

# Método 1: Importar funciones específicas desde funciones.circulo
from funciones.circulo import area, perimetro

print(f"   Área de círculo radio 5: {area(5):.2f}")
print(f"   Perímetro de círculo radio 5: {perimetro(5):.2f}")

# Método 2: Importar el módulo completo
import funciones.circulo as circulo

print(f"   Área de círculo radio 5: {circulo.area(5):.2f}")
print(f"   Perímetro de círculo radio 5: {circulo.perimetro(5):.2f}\n")

############################################
# GESTIÓN DE RUTAS DE IMPORTACIÓN          #
############################################

#=== GESTIÓN DE RUTAS DE IMPORTACIÓN ===

import os
import sys

# Método 1: Cambiar directorio de trabajo temporalmente
# Sólo con el REPL
print("1. Cambiando directorio de trabajo:")
directorio_original = os.getcwd()
try:
    os.chdir("funciones/")
    import circulo as cir_temp
    print("   ✓ Módulo importado correctamente después de cambiar directorio")
except FileNotFoundError:
    print("   ✗ No se pudo encontrar el directorio 'funciones/'")
finally:
    os.chdir(directorio_original)  # Volver al directorio original

print(f"   Área de círculo radio 3: {cir_temp.area(3):.2f}")
print(f"   Perímetro de círculo radio 25: {cir_temp.perimetro(25):.2f}")

# Método 2: Añadir ruta al sys.path (RECOMENDADO)
ruta_funciones = os.path.join(os.getcwd(), "funciones")
#ruta_funciones = os.getcwd() + "/" + "funciones"
if ruta_funciones not in sys.path:
    sys.path.append(ruta_funciones)
    print(f"   ✓ Ruta añadida: {ruta_funciones}")

# Ahora podemos importar normalmente
import circulo as cir

print(f"   Área de círculo radio 3: {cir.area(3):.2f}")
print(f"   Perímetro de círculo radio 25: {cir.perimetro(25):.2f}")



sys.path.append("C:/Documentos/mis_cosillas")
