## CLASSE PERSONAGEM -> super() ##
from .superPoder import SuperPoder

class Personagem:
  # Construtor
  def __init__(self, nome, nome_vida_real):
    self.__nome = nome
    self.__nome_vida_real = nome_vida_real
    self.__poderes = []

  # Outros Métodos
  def adicionar_super_poder(self, superpoder):
    # Verifica se superpoder já existe na lista
    if superpoder not in self.__poderes:
      self.__poderes.append(superpoder)
    else:
      print('O superpoder não pode ser usado mais que uma vez!!') 
          
  def get_poder_total(self):
    poder_total = 0

    for superpoder in self.__poderes:
      poder_total += int(superpoder.get_categoria())

    return poder_total
