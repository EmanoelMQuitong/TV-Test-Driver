import random

class TV():
    def __init__(tv, power, channel = 1, volume = 1):
        tv.power = power
        tv.channel = channel
        tv.volumeLevel = volume

#Turns On tv              
    def turnOn(tv):
        if tv.power == 'On':
            print("Tv is On") 
            return  True
        
#Turns off Tv.
    def turnOff(tv):
        if tv.power == 'Off':
            print("Tv is Off")     
            return False

#Returns Channel for Tv.
    def getChannel(channel):None

#Set channel a new Channel for Tv.
    def setChannel(tv, channel = 1):
        tv.channel = channel

#Returns Channel for Tv.
    def getVolume(volume): int

#Set channel a new Volume for Tv.
    def setVolume(tv, volumeLevel = 1): 
        tv.volumeLevel = volumeLevel
    
    
#Increases Channel number by 1
    def channelUp(tv): 
        return int(tv.channel) + 1

#Decreases Channel number by 1
    def channelDown(tv):
        return int(tv.channel) - 1

#Increases Volume number by 1
    def volumeUp(tv): 
        return int(tv.volumeLevel) + 1

#Decreases Volume number by 1
    def volumeDown(tv): 
        return int(tv.volumeLevel) - 1
    
    def show(tv):
        print(tv.power, tv.channel, tv.volumeLevel)
        print("Volume down result", tv.volumeDown())
        print("Volume Up result", tv.volumeUp())
        print("Channel down result", tv.channelDown())
        print("Channel Up result", tv.channelUp())

power = 'On'
channel = input("Enter channel: ")
volume = input("Kindly enter volume: ")

Tv1 = TV(power ,  channel, volume)
Tv1.show()