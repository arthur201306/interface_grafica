from funcionalidades import *

television = Television(fab='LG', model='LG123')
control = RemoteControl(television)

#Sintonizar um canal na TV usando o controle remoto
control.sintonizarRemotoCanal(channel='Globo')

#Trocar de canal com o que está na lista

#[ Globo ] => Lista de canais
control.trocarRemotoCanal(channel='Globo')

print(television.current_cannel)