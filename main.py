## CLASSE MAIN ##
from confronto import Confronto
from superHeroi import SuperHeroi
from vilao import Vilao
from superPoder import SuperPoder

# Lista de superpoderes dos objetos -> nome do superpoder e categoria de força
superpoderes_heroi = [
  SuperPoder('Velocidade', 3), 
  SuperPoder('Forca', 3), 
  SuperPoder('Braceletes', 1)
]

superpoderes_vilao = [
  SuperPoder('Tentáculos indestruttíveis', 5),
  SuperPoder('Velocidade', 1)
]

# Instanciando os objetos superheroi e vilao
superheroi = SuperHeroi('Mulher-Maravilha', 'Diana')
vilao = Vilao('Octopus', 'Otto Octavius', 0)

# Adicionando superpoderes aos objetos 
for superpoder in superpoderes_heroi:
  superheroi.adicionar_super_poder(superpoder)

for superpoder in superpoderes_vilao:
  vilao.adicionar_super_poder(superpoder)

# Confronto entre o super-herói e o vilão
confronto = Confronto()

result = confronto.lutar(superheroi, vilao)

def exibirVencedor(result):
  match result:
    case 0:
      print("Deu empate!!")

    case 1:
      print(f'{superheroi._Personagem__nome} venceu a partida com o poder total de {superheroi.get_poder_total()}!')

    case 2:
      print(f'{vilao._Personagem__nome} venceu a partida, com o poder total de {vilao.get_poder_total()}!')

exibirVencedor(result)
