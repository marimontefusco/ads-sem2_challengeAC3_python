## CLASSE HEROI ##
from .personagem import Personagem

class SuperHeroi(Personagem):
  # Método Sobrescrito
  def get_poder_total(self):
    poder_total = int(1.10 * super.get_poder_total())
    return poder_total
