class Carro:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def descripcion(self):
        return f"Carro: {self.marca} {self.modelo}, Año: {self.año}"

class Barco:
    def __init__(self, nombre, tipo, capacidad):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad

    def descripcion(self):
        return f"Barco: {self.nombre}, Tipo: {self.tipo}, Capacidad: {self.capacidad} personas"

class Avion:
    def __init__(self, aerolinea, modelo, capacidad):
        self.aerolinea = aerolinea
        self.modelo = modelo
        self.capacidad = capacidad

    def descripcion(self):
        return f"Avión: Aerolínea {self.aerolinea} {self.modelo}, Capacidad: {self.capacidad} pasajeros"

carro1 = Carro("Ford", "Explorer", 2016)
carro2 = Carro("Toyota", "Corolla", 2007)

barco1 = Barco("Poseidón", "Crucero", 3000)
barco2 = Barco("Aventura", "Velero", 10)

avion1 = Avion("American Airlines", "Boeing 737", 180)
avion2 = Avion("Emirates", "Airbus A380", 850)

vehiculos = [carro1, carro2, barco1, barco2, avion1, avion2]
for vehiculo in vehiculos:
    print(vehiculo.descripcion())