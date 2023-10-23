## CLASSE CONFRONTO ##
class Confronto:
  def lutar(self, superheroi, vilao):
    poderHeroi = superheroi.get_poder_total()
    poderVilao = vilao.get_poder_total()

    if poderHeroi == poderVilao:
      resultado = 0

    elif poderHeroi > poderVilao:
      resultado = 1

    elif poderHeroi < poderVilao:
      resultado = 2

    return resultado
