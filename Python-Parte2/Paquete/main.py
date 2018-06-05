#from animals.gato import Gato #No es la mejor forma de importar..
from animals import Gato
from animals import creador_gatos
from animals import const

#gato = Gato('Silvestre')
gato = creador_gatos('Buen estado..')
print(gato.name)
print(const)