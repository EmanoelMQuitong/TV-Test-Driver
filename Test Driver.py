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
print(GREEN+BOLD+BORDER+END)
print(GREEN+BOLD+BORDER+END)

text_print = (f"Television 1")
print(color + pyfiglet.figlet_format(text_print , font= "bubble")+END)
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

print(PURPLE +"Final Channel of Television 1: "+ END, Tv1.channel)
print(PURPLE +"Final Volume Level of Television 1: "+ END, Tv1.volume)
print(PURPLE +"Is Television 1 on?: "+ END, Tv1.power)

print(GREEN+BOLD+BORDER+END)
print(GREEN+BOLD+BORDER+END)

text_print = (f"Television 2")
print(color + pyfiglet.figlet_format(text_print , font= "bubble")+END)
print('\n') 
Tv2 = TV()
Tv2.turnOn()
Tv2.turnOff()

Tv2.getChannel()
print(BLUE +"Current Channel: "+ END, Tv2.channel)
print('\n')
Tv2.setChannel()
print(BLUE +"Current Channel: "+ END, Tv2.channel)
print('\n')

Tv2.getVolume()
print(BLUE +"Current Volume: "+ END, Tv2.volume)
print('\n')
Tv2.setVolume()
print(BLUE +"Current Volume: "+ END, Tv2.volume)
print('\n')

Tv2.channelUp()
print(BLUE +"Current Channel: "+ END, Tv2.channel)
print('\n')
Tv2.channelDown()
print(BLUE +"Current Channel: "+ END, Tv2.channel)
print('\n')

Tv2.volumeUp()
print(BLUE +"Current Volume: "+ END, Tv2.volume)
print('\n')
Tv2.volumeDown()
print(BLUE +"Current Volume: "+ END, Tv2.volume)
print('\n')

print(PURPLE +"Final Channel of Television 2: "+ END, Tv2.channel)
print(PURPLE +"Final Volume Level of Television 2: "+ END, Tv2.volume)
print(PURPLE +"Is Television 2 on?: "+ END, Tv2.power)

print(GREEN+BOLD+BORDER+END)
print(GREEN+BOLD+BORDER+END)


print('\n')
print('\n')


print(BOLD+BORDER+END)
print(BOLD+BORDER+END)
print('\n')
#output
print(PURPLE+BOLD+"OUTPUT: "+END)
print('\n')
if Tv1.power == True:
    print(PURPLE+"Television 1's channel is ,"+END,Tv1.channel,".", PURPLE+" Television 1's volume is ,"+END,Tv1.volume,".")
else: 
    print(RED+"Television 1 is Off."+END)
print('\n')
if Tv2.power == True:
    print(PURPLE+"Television 2's channel is ,"+END,Tv2.channel,".", PURPLE+" Television 2's volume is ,"+END,Tv2.volume,".")
else: 
    print(RED+"Television 2 is Off."+END)

print('\n')
print(BOLD+BORDER+END)
print(BOLD+BORDER+END)