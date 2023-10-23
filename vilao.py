## CLASSE VILAO ##
from personagem import Personagem

class Vilao(Personagem):
    # Construtor
    def __init__(self, nome, nome_vida_real, tempo_de_prisao):
        super().__init__(nome, nome_vida_real)
        self.tempo_de_prisao = tempo_de_prisao
