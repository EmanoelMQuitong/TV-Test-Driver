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

def main():
    name = input("pls enter name")