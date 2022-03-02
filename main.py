from Ninja import Ninja
from Mascota import Mascota
from Alpacas import Alpacas

Chindolfo = Mascota("Chindolfo","Chinchilla","Flaked Oats",100,100)
Gandolfo = Alpacas("Gandolfo","Alpaca","Manzanas",100,100,"NZ")
Luke= Ninja("Luke","Walker",Gandolfo,"Alpaca Master","Veggie")

Luke.alimentar()
Luke.caminar()
Luke.bañar()

