############################################
# LECTURA DE ARCHIVOS DE TEXTO             #
############################################
"""
MODOS DE APERTURA DE ARCHIVOS:
"r" - Lectura (por defecto). Error si el archivo no existe
"a" - Append (agregar al final). Crea el archivo si no existe
"w" - Escritura (sobrescribe). Crea el archivo si no existe
"x" - Creación exclusiva. Error si el archivo existe
"+" - Lectura y escritura (combinado con otros modos)
"""

# Abrir un archivo
"""Vamos a abrir directamente el archivo que contiene El Quijote"""
archivo = open("datos/quijote.txt", "r", encoding="utf-8")
print(f"   ✓ Archivo abierto correctamente")

type(archivo)

contenido = archivo.read()
archivo.seek(0)

contenido_lineas = archivo.readlines()

print(f"   Nombre del archivo: {archivo.name}")
print(f"   Modo de apertura: {archivo.mode}")
print(f"   ¿Está cerrado?: {archivo.closed}")
# Cerrar un archivo
archivo.close()
archivo.seek(0)
archivo.read()

print(f"   ✓ Archivo cerrado correctamente")
print(f"   ¿Está cerrado?: {archivo.closed}")

with open("datos/quijote.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

archivo.seek(0)   


# Lectura completa de un archivo
try:
    with open("datos/quijote.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()    
    print(f"   ✓ Archivo leído correctamente")
    print(f"   Tamaño del contenido: {len(contenido)} caracteres")
    print(f"   Primeros 300 caracteres:\n{contenido[:300]}...\n")   
except FileNotFoundError:
    print("   ✗ No se pudo encontrar el archivo 'datos/quijote.txt'")
except Exception as e:
    print(f"   ✗ Error al leer el archivo: {e}")

# Lectura línea por línea
try:
    with open("datos/quijote.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
    
    print(f"   ✓ Archivo leído correctamente")
    print(f"   Número de líneas: {len(lineas)}")
    print(f"   Primeras 5 líneas:")
    for i, linea in enumerate(lineas[:5], 1):
        print(f"   Línea {i}: {linea.strip()}")
    print()
except FileNotFoundError:
    print("   ✗ No se pudo encontrar el archivo 'datos/quijote.txt'\n")




# Búsqueda de palabras en el texto
if 'contenido' in locals():
    print(f"   'Sancho' aparece {contenido.count('Sancho')} veces")
    print(f"   'Quijote' aparece {contenido.count('Quijote')} veces")
    print(f"   'Dulcinea' aparece {contenido.count('Dulcinea')} veces\n")

# Limpieza del texto (eliminar saltos de línea múltiples)
if 'contenido' in locals():
    texto_limpio = contenido.replace("\n\n", "##SALTO_DOBLE##")
    texto_limpio = texto_limpio.replace("\n", " ")
    texto_limpio = texto_limpio.replace("##SALTO_DOBLE##", "\n\n")
    
    print("   ✓ Texto limpiado correctamente")
    print(f"   Ejemplo del texto limpiado:\n{texto_limpio[5000:5100]}...\n")

############################################
# ESCRITURA DE ARCHIVOS DE TEXTO           #
############################################

# Escritura básica (sobrescribe el contenido)

try:
    with open("datos/nombres.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Diego\n")
        archivo.write("Aitor\n")
        archivo.writelines(["Juan\n", "Pedro\n"])
    
    print("   ✓ Archivo creado/sobrescrito correctamente")   
except Exception as e:
    print(f"   ✗ Error al escribir el archivo: {e}")

# Append (agregar al final)
from datetime import datetime
try:
    with open("datos/nombres.txt", "a", encoding="utf-8") as archivo:
        archivo.write("María\n")
        archivo.write(f"Registro añadido el: {datetime.now()}\n")
        archivo.write("-" * 30 + "\n")
    print("   ✓ Contenido agregado correctamente") 
except Exception as e:
    print(f"   ✗ Error al agregar contenido: {e}")

# Lectura del archivo creado
try:
    with open("datos/nombres.txt", "r", encoding="utf-8") as archivo:
        contenido_nombres = archivo.read()  
    print("   Contenido del archivo:")
    print(contenido_nombres)
except FileNotFoundError:
    print("   ✗ No se pudo encontrar el archivo 'datos/nombres.txt'")

############################################
# MODIFICACIÓN DE ARCHIVOS EXISTENTES      #
############################################
# Crear un archivo de prueba
try:
    with open('datos/ejemplo_modificacion.txt', 'w', encoding='utf-8') as archivo:
        for i in range(1, 6):
            archivo.write(f"Línea original {i}\n")
    print("   ✓ Archivo de prueba creado correctamente")
except Exception as e:
    print(f"   ✗ Error al crear archivo de prueba: {e}")

# Modificar una línea específica
try:
    # Leer todas las líneas
    with open('datos/ejemplo_modificacion.txt', 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
    # Modificar la línea 3 (índice 2)
    if len(lineas) >= 3:
        lineas[2] = "Línea 3 MODIFICADA\n"     
        # Reescribir el archivo
        with open('datos/ejemplo_modificacion.txt', 'w', encoding='utf-8') as archivo:
            archivo.writelines(lineas)
        print("   ✓ Línea modificada correctamente")
    else:
        print("   ✗ El archivo no tiene suficientes líneas")
except Exception as e:
    print(f"   ✗ Error al modificar el archivo: {e}")

try:
    # Leer todas las líneas
    with open('datos/ejemplo_modificacion.txt', 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    # Modificar la línea 3 (índice 2)
    contenido = contenido.replace("Línea original 2", "linea 2")    

    with open('datos/ejemplo_modificacion.txt', 'r+', encoding='utf-8') as archivo:
        archivo.writelines(contenido)
    print("   ✓ Línea modificada correctamente")
except Exception as e:
    print(f"   ✗ Error al modificar el archivo: {e}")

# Verificar la modificación
try:
    with open('datos/ejemplo_modificacion.txt', 'r', encoding='utf-8') as archivo:
        contenido_modificado = archivo.read()
    print("   Contenido modificado:")
    print(contenido_modificado)
except FileNotFoundError:
    print("   ✗ No se pudo encontrar el archivo modificado")

############################################
# BUENAS PRÁCTICAS Y RECOMENDACIONES       #
############################################
'''
1. Siempre usar 'with open()' para manejo automático de cierre
2. Especificar siempre la codificación (utf-8 recomendado)
3. Manejar excepciones con try-except
4. Usar rutas relativas en lugar de absolutas cuando sea posible
5. Verificar que los archivos/directorios existen antes de operar
6. Usar os.path.join() para construir rutas multiplataforma
'''
# Ejemplo de buena práctica
print("\nEjemplo de código robusto:")

import os

def leer_archivo_seguro(ruta_archivo):
    """Función segura para leer archivos con manejo de errores"""
    try:
        if not os.path.exists(ruta_archivo):
            print(f"   El archivo {ruta_archivo} no existe")
            return None
        
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        
        print(f"   ✓ Archivo {ruta_archivo} leído correctamente")
        return contenido
        
    except PermissionError:
        print(f"   ✗ Sin permisos para leer {ruta_archivo}")
        return None
    except Exception as e:
        print(f"   ✗ Error inesperado: {e}")
        return None

# Probar la función
print("\nProbando función segura:")
contenido_seguro = leer_archivo_seguro("datos/nombres2.txt")



#############
# Ejercicio #
#############
"""
Crear un archivo llamado dulcinea.txt que contenga las líneas de quijote.txt que contengan el nombre de Dulcinea
"""

# Solución

