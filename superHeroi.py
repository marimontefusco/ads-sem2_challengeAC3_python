## CLASSE HEROI ##
from personagem import Personagem

class SuperHeroi(Personagem):
  # Método Sobrescrito
  def get_poder_total(self):
    poder_total = super().get_poder_total()

    poder_total *= 1.10 # poder com acréscimo de 10%
    
    return int(poder_total)
