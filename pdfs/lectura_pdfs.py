from PyPDF2 import PdfReader
import re

reader1 = PdfReader("pdfs/339741.pdf")
reader2 = PdfReader("pdfs/FDS 2023 - SALFUMAN - AGUA FUERTE.pdf")
reader3 = PdfReader("pdfs/SDB-9277-ES-ES.pdf")
"""
number_of_pages = len(reader.pages)
text = ""
for page in reader.pages:
    text += page.extract_text()
print(text)
"""
print(reader1.pages[2].extract_text())

# Localizar la sección 2
for reader in [reader1, reader2,reader3]:
    texto =reader.pages[0].extract_text()
    texto +=reader.pages[1].extract_text()
    patron = r"Identificaci ?ón de los peligros"
    x = re.search(patron, texto, re.IGNORECASE)

    """Posiciones inicial y final de **la primera coincidencia**"""

    x.regs

    ((inicio, fin),) = x.regs

# Localizar la sección 3
for reader in [reader1, reader2,reader3]:
    texto =reader.pages[0].extract_text()
    texto +=reader.pages[1].extract_text()
    texto +=reader.pages[2].extract_text()
    patron = r"Composici ?ón/informaci ?ón sobre los componentes"
    x = re.search(patron, texto, re.IGNORECASE)

    """Posiciones inicial y final de **la primera coincidencia**"""

    x.regs

    ((inicio, fin),) = x.regs

def seccion2(reader, patron_inicio=r"Identificaci ?ón de los peligros", patron_final=r"Composici ?ón/informaci ?ón sobre los componentes"):
    texto =reader.pages[0].extract_text()
    texto +=reader.pages[1].extract_text()
    texto +=reader.pages[2].extract_text()
    x = re.search(patron_inicio, texto, re.IGNORECASE)
    ((inicio, _),) = x.regs
    x = re.search(patron_final, texto, re.IGNORECASE)
    ((_, final),) = x.regs
    return texto[inicio:final]

print(seccion2(reader1))
print(seccion2(reader2))
print(seccion2(reader3))

patron = r"H\d{3}"
resultado = set()
iterable_ocurrencias = re.finditer(patron, seccion2(reader3))
for ocurrencia in iterable_ocurrencias:
    resultado.add(ocurrencia.group())