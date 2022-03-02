class Mascota:

    def __init__(self, name, tipo, golosinas, salud, energía):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = salud
        self.energía = energía

    def dormir(self):
        self.energía += 25

    def comer(self):
        self.energía += 5
        self.salud += 10

    def jugar(self):
        self.salud += 5

    def sonido(self):
        print("Grrrrrrr")
