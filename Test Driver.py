from TV import TV
import pyfiglet
from colored import fg

#pyfiglet format :
# color = fg('blue')
#text_print = (f"Text")
#print(color + pyfiglet.figlet_format(text_print , font= "digital")) 
color = fg('blue')
#Colors
BLUE = '\033[94m'
DARKCYAN = '\033[36m'
PURPLE = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'
BORDER = 175*'='
BORDER = print(GREEN+BOLD+BORDER+END)
print(GREEN+BOLD+BORDER+END)

text_print = (f"Television 1")
print(color + pyfiglet.figlet_format(text_print , font= "bubble"))
print('\n') 
Tv1 = TV()
Tv1.turnOn()
Tv1.turnOff()

Tv1.getChannel()
print(BLUE +"Current Channel: "+ END, Tv1.channel)
print('\n')
Tv1.setChannel()
print(BLUE +"Current Channel: "+ END, Tv1.channel)
print('\n')

Tv1.getVolume()
print(BLUE +"Current Volume: "+ END, Tv1.volume)
print('\n')
Tv1.setVolume()
print(BLUE +"Current Volume: "+ END, Tv1.volume)
print('\n')

Tv1.channelUp()
print(BLUE +"Current Channel: "+ END, Tv1.channel)
print('\n')
Tv1.channelDown()
print(BLUE +"Current Channel: "+ END, Tv1.channel)
print('\n')

Tv1.volumeUp()
print(BLUE +"Current Volume: "+ END, Tv1.volume)
print('\n')
Tv1.volumeDown()
print(BLUE +"Current Volume: "+ END, Tv1.volume)
print('\n')

print(PURPLE +"Final Channel: "+ END, Tv1.channel)
print(PURPLE +"Final Volume Level: "+ END, Tv1.volume)
print(PURPLE +"Is it on?: "+ END, Tv1.power)

print(GREEN+BOLD+BORDER+END)
print(GREEN+BOLD+BORDER+END)