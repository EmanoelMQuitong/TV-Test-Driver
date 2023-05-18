from TV import TV
#Colors
BLUE = '\033[94m'
DARKCYAN = '\033[36m'
PURPLE = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'
BORDER = 170*'='
BORDER = print(GREEN+BOLD+BORDER+END)

def main():
    Tv1 = TV()
    response = input("Would you to turn the Television 1 'On' or 'Off'?:  ")
    if response == Tv1.turnOn():
        ('/n')
        
        #Get channel
        channel = input("What channel do you want to watch?(Choose from 1-120 only): ")
        channel = Tv1.getChannel(channel)
        ask_change_chan = input("Would you like to change the channel?('yes' or 'no') ")
        
        ('/n')
        #Change Channel
        if ask_change_chan.lower() == 'yes':
            while ask_change_chan.lower() == 'yes':
                New_channel = Tv1.setChannel()
                ask_change_chan = input("Would you like to change the channel?('yes' or 'no'): ")
                ('/n')
            channel = New_channel

        elif ask_change_chan.lower() == 'no':
            pass

        else:
            raise Exception(RED +"Please choose between 'yes' or 'no' only."+ END)

        ('/n')

        #Get Volume
        volumeLevel = input("What is your desired volume Level? (Choose from 1-7 only): ")
        volume = Tv1.getVolume(volumeLevel)

    elif response == Tv1.turnOff():
        print("Television 1 is Off.")
    else:
        raise Exception ("Please answer 'On' or 'Off' only.") 
        
