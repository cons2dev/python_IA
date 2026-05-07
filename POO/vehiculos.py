class Coche:
    def __init__(self, marca, modelo, longitud, precio):
        self.marca = marca
        self.modelo = modelo
        self.longitud = int(longitud*100)
        self.precio = precio

    def __del__(self):
        print(f"Se ha borrado el {self.marca} {self.modelo}")
    
    def __len__(self):
        return self.longitud
    
    def __str__(self):
        return f"{self.marca} {self.modelo} de {self.precio} €"
    
    def saludar(self):
        print(f"Hola, soy un {self.marca} {self.modelo}")

    def __lt__(self, otro):
        if isinstance(otro, Coche):
            return self.precio < otro.precio
        else:
            print(f"{otro} no es un coche")