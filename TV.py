import random

#Colors and Bold
BLUE = '\033[94m'
DARKCYAN = '\033[36m'
PURPLE = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'


class TV():
    def __init__(tv, power = 'Off', channel = 1, volume = 1):
        tv.power = power
        tv.channel = channel
        tv.volume = volume

#Turns On tv              
    def turnOn(tv):
        return True
            
            
        
#Turns off Tv.
    def turnOff(tv):
        return False
            
                             
#Returns Channel for Tv.
    def getChannel(tv):
        tv.channel = int(tv.channel)
        if tv.channel < 120:
            if tv.channel >= 1:
                return int(tv.channel)
            else: 
                raise Exception(RED + "Sorry, no numbers below zero (0)."+ END)
        else:
            raise Exception (RED + "Sorry, no numbers greater than 120"+ END)
        
#Set channel a new Channel for Tv.
    def setChannel(new_channel):
        new_channel = input("Please enter NEW CHANNEL: ")
        if int(new_channel) < 120:
            if int(new_channel) >= 1:
                return int(new_channel)
            else: 
                raise Exception(RED + "Sorry, no numbers below zero (0)."+ END)
        else:
            raise Exception (RED + "Sorry, no numbers greater than 120"+ END)

#Returns Channel for Tv.
    def getVolume(tv):
        tv.volume = int(tv.volume) 
        if tv.volume < 8:
            if tv.volume >= 1:
                return int(tv.volume)
            else: 
                raise Exception(RED + "Sorry, no numbers below zero (0)."+ END)
        else:
            raise Exception (RED + "Sorry, no numbers greater than 7"+ END)
        
#Set channel a new Volume for Tv.
    def setVolume(tv): 
        new_volume = input("Please enter NEW VOLUME LEVEL: ")
        if int(new_volume) < 8:
            if int(new_volume) >= 1:
                return int(new_volume)
            else: 
                raise Exception(RED + "Sorry, no numbers below zero (0)."+ END)
        else:
            raise Exception (RED + "Sorry, no numbers greater than 7"+ END)
         
#Increases Channel number by 1
    def channelUp(tv): 
        return int(tv.channel) + 1

#Decreases Channel number by 1
    def channelDown(tv):
        return int(tv.channel) - 1

#Increases Volume number by 1
    def volumeUp(tv): 
        return int(tv.volume) + 1

#Decreases Volume number by 1
    def volumeDown(tv): 
        return int(tv.volume) - 1
    def show(tv):
        print(tv.power, tv.channel, tv.volume)

Tv1 = TV()
Tv1.show()