import random
import pyfiglet
from colored import fg
#Colors and Bold
BLUE = '\033[94m'
DARKCYAN = '\033[36m'
PURPLE = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'
color = fg('blue')
BORDER = 175*'='




class TV():
    def __init__(tv, power = False, channel = 1, volume = 1):
        tv.power = power
        tv.channel = channel
        tv.volume = volume

#Turns On tv              
    def turnOn(tv):
        response = input("Would you like to turn the power 'On' or 'Off'?: ")
        tv.power = response
        if tv.power == 'On':
            tv.power = True
            return tv.power
        elif tv.power == 'Off':
            tv.power = False
            return tv.power
        else:
            raise Exception(RED + "Please choose between 'On' or 'Off' only."+ END)
        ('/n')    
            
        
#Turns off Tv.
    def turnOff(tv):
        if tv.power == False:
            tv.power = False
            return tv.power
        else:
            pass
            
                             
#Returns Channel for Tv.
    def getChannel(tv):
        tv.channel = int(input("What channel do you want to watch?(Choose from 1-120 only): "))
        if tv.channel < 120:
            if tv.channel >= 1:
                tv.channel = int(tv.channel)
                ('/n')
                return tv.channel
            else: 
                raise Exception(RED + "Sorry, no numbers below zero (0)."+ END)
        else:
            raise Exception (RED + "Sorry, no numbers greater than 120"+ END)
       

#Set channel a new Channel for Tv.
    def setChannel(tv):
        
        response = input("Would you like to enter a NEW CHANNEL?('yes'/'no'): ")
        if response == 'yes':
            tv.channel = ''
            while response == 'yes':
                print('\n')
                tv.channel = input("Please enter NEW CHANNEL: ")
                if int(tv.channel) < 120:
                    if int(tv.channel) >= 1:
                        print('\n')
                        response = input("Would you like to enter a NEW CHANNEL?('yes'/'no'): ")                       
                    else: 
                        raise Exception(RED + "Sorry, no numbers below zero (0)."+ END)
                else:
                    raise Exception (RED + "Sorry, no numbers greater than 120"+ END)
            tv.channel = int(tv.channel)
            return tv.channel
        
        elif response.lower() == 'no':
            pass
        else:
            raise Exception(RED +"Please choose between 'yes' or 'no' only."+ END)
        

#Returns Channel for Tv.
    def getVolume(tv):
        tv.volume = int(input("What is your desired volume level?(Choose from 1-7 only): ")) 
        if tv.volume < 8:
            if tv.volume >= 1:
                ('/n')
                return int(tv.volume)
            else: 
                raise Exception(RED + "Sorry, no numbers below zero (0)."+ END)
        else:
            raise Exception (RED + "Sorry, no numbers greater than 7"+ END)
        
#Set channel a new Volume for Tv.
    def setVolume(tv):
        print('\n') 
        response = input("Would you like to enter a NEW VOLUME?('yes'/'no'): ")
        if response == 'yes':
            tv.volume = ''
            while response == 'yes':
                print('\n')
                tv.volume = input("Please enter NEW VOLUME LEVEL: ")
                if int(tv.volume) < 7:
                    if int(tv.volume) >= 1:
                        print('\n')
                        response = input("Would you like to enter a NEW VOLUME VOLUME LEVEL?('yes'/'no'): ")

                    else: 
                        raise Exception(RED + "Sorry, no numbers below zero (0)."+ END)
                else:
                    raise Exception (RED + "Sorry, no numbers greater than 7"+ END)
            
            return int(tv.volume)
        
        elif response.lower() == 'no':
            pass
        else:
            raise Exception(RED +"Please choose between 'yes' or 'no' only."+ END)
        
    
#Increases Channel number by 1
    def channelUp(tv): 
        response = input("Would you like to increase the channel by one (1) ? ('yes'/'no'): ") 
        if response == 'yes':
            while response == 'yes':
                tv.channel = int(tv.channel) + 1
                print('\n')
                response = input("Would you like to increase the channel by one (1) ? ('yes'/'no'): ")
                

            return int(tv.channel)
        elif response.lower() == 'no':
            pass
        else:
            raise Exception(RED +"Please choose between 'yes' or 'no' only."+ END)
        
#Decreases Channel number by 1
    def channelDown(tv):
        response = input("Would you like to decrease the channel by one (1) ? ('yes'/'no'): ") 
        if response == 'yes':
            while response == 'yes':
                tv.channel = int(tv.channel) - 1
                print('\n')
                response = input("Would you like to decrease the channel by one (1) ? ('yes'/'no'): ")
                

            return int(tv.channel)
        elif response.lower() == 'no':
            pass
        else:
            raise Exception(RED +"Please choose between 'yes' or 'no' only."+ END)
        
#Increases Volume number by 1
    def volumeUp(tv): 
        response = input("Would you like to increase the volume by one (1) ? ('yes'/'no'): ") 
        if response == 'yes':
            while response == 'yes':
                tv. volume = int(tv.volume) + 1
                print('\n')
                response = input("Would you like to increase the volume by one (1) ? ('yes'/'no'): ")
                

            return int(tv.volume)
        elif response.lower() == 'no':
            pass
        else:
            raise Exception(RED +"Please choose between 'yes' or 'no' only."+ END)

#Decreases Volume number by 1
    def volumeDown(tv): 
        response = input("Would you like to decrease the volume by one (1) ? ('yes'/'no'): ") 
        if response == 'yes':
            while response == 'yes':
                tv. volume = int(tv.volume) - 1
                print('\n')
                response = input("Would you like to decrease the volume by one (1) ? ('yes'/'no'): ")
                

            return int(tv.volume)
        elif response.lower() == 'no':
            pass
        else:
            raise Exception(RED +"Please choose between 'yes' or 'no' only."+ END)

