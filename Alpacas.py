from Mascota import Mascota

class Alpacas(Mascota):

    def __init__(self, name, tipo, golosinas, salud, energía,origen):
        super().__init__(name, tipo, golosinas, salud, energía)
        self.origen=origen

    def truco(self):
        print("Rumiar")

    def jugar(self):
        super().jugar()
        self.truco()
