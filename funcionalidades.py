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

class RemoteControl:
  def __init__(self, tv):
    self.tv = tv
    
  def aumentarRemotoVolume(self):
    self.tv.aumentarVolume(20)

  def diminuirRemotoVolume(self):
    self.tv.diminuirVolume(30)

  def trocarRemotoCanal(self, channel):
    self.tv.trocarCanal(channel)

  def sintonizarRemotoCanal(self, channel):
    self.tv.sintonizarCanal(channel)