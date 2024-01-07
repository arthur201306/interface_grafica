#Desafio Bradesco Curso

#A partir disso, foi dada mais uma missão: criar uma classe ControleRemoto, cujo atributo é televisão (isto é, recebe um objeto da classe Televisor). Neste caso, você deve criar métodos para aumentar/diminuir volume, trocar e sintonizar um novo canal, que adiciona um novo canal à lista de canais (somente se esse canal não estiver nessa lista).

import tv

class RemoteControl:
  def __init__(self, tv: tv):
    self.tv = tv.Television
    
  def aumentarRemotoVolume(self):
    self.tv.aumentarVolume(20)

  def diminuirRemotoVolume(self):
    self.tv.diminuirVolume(30)

  def trocarRemotoCanal(self, channel):
    self.tv.trocarCanal(channel)

  def sintonizarRemotoCanal(self, channel):
    self.tv.sintonizarCanal(channel)