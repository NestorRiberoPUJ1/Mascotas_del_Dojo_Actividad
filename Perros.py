from Mascota import Mascota

class Perros(Mascota):

    def __init__(self, name, tipo, golosinas, salud, energía,raza):
        super().__init__(name, tipo, golosinas, salud, energía)
        self.raza=raza

    def truco(self):
        print("Saltar")

    def sonido(self):
        print("GUAU GUAU")