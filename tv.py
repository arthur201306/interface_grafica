#Desafio do curso de interface gráfica do Bradesco

#Para isso, é preciso criar métodos para aumentar/diminuir volume, trocar e sintonizar um novo canal, adicionando um novo canal à lista (somente se esse canal não estiver nessa lista). No atributo lista de canais, devem estar armazenados todos os canais já sintonizados dessa TV.

#Criar uma classe Televisão

class Television:
  def __init__(self, fab, model):
    self.fab = fab
    self.model = model
    self.current_cannel = None
    self.list_of_channels = []
    self.volume = 20

  #Criar um método de aumentar/diminuir o volume
  def aumentarVolume(self, value):
    if (self.volume+ value <= 100):
      self.volume += value
    else:
      self.volume = 100

  def diminuirVolume(self, value):
    if (self.volume- value >= 0):
      self.volume -= value
    else:
      self.volume = 0

  def trocarCanal(self, channel):
    if channel in self.list_of_channels:
      self.current_cannel = channel

  #Sintonizar canal
  def sintonizarCanal(self, channel):
    if channel not in self.list_of_channels:
      self.list_of_channels.append(channel)