from Mascota import Mascota


class Ninja:

    def __init__(self, nombre, apellido, mascotas, premio, comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.mascotas = mascotas
        self.premio = premio
        self.comida_mascota = comida_mascota

    def caminar(self):
        self.mascotas.jugar()

    def alimentar(self):
        self.mascotas.comer()

    def bañar(self):
        self.mascotas.sonido()
