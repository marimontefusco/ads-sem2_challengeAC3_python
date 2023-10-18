## CLASSE CONFRONTO ##
from .superHeroi import SuperHeroi
from .vilao import Vilao

class Confronto():
  def lutar(self, superheroi, vilao):
    poderHeroi = SuperHeroi().get_poder_total()
    poderVilao = Vilao.get_poder_total()

    resultado = 0
    if poderHeroi.value() == poderVilao.value():
      resultado = '0'
    elif poderHeroi.value() > poderVilao.value():
      resultado = '1'
    elif poderHeroi.value() < poderVilao.value():
      resultado = '2'

    return resultado
