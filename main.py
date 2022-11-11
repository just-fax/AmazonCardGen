import ctypes
import os
import random
import string
import sys
import time

import pyfiglet
import requests
from colorama import Fore
from luhn import verify

print(f'''{Fore.RED}
▄▄▄      ▒███████▒  ██████  ▄████▄       ▄████ ▓█████  ███▄    █ 
▒████▄    ▒ ▒ ▒ ▄▀░▒██    ▒ ▒██▀ ▀█      ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▒██  ▀█▄  ░ ▒ ▄▀▒░ ░ ▓██▄   ▒▓█    ▄    ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
░██▄▄▄▄██   ▄▀▒   ░  ▒   ██▒▒▓▓▄ ▄██▒   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
 ▓█   ▓██▒▒███████▒▒██████▒▒▒ ▓███▀ ░   ░▒▓███▀▒░▒████▒▒██░   ▓██░ -Close the window to shut down the program
 ▒▒   ▓▒█░░▒▒ ▓░▒░▒▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░    ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
  ▒   ▒▒ ░░░▒ ▒ ░ ▒░ ░▒  ░ ░  ░  ▒        ░   ░  ░ ░  ░░ ░░   ░ ▒░
  ░   ▒   ░ ░ ░ ░ ░░  ░  ░  ░           ░ ░   ░    ░      ░   ░ ░ 
      ░  ░  ░ ░          ░  ░ ░               ░    ░  ░         ░ 
          ░                 ░                                        
Amazon Storecard Generator Made by: RebootedOrbit#0533, discord server: https://discord.gg/EsvpGV7vHv                       
                               ''')


print(f"{Fore.BLUE}[?][/] Enter to start generating.")
check2 = input(f'{Fore.RED}[?]>')

#60457811 - use this bin if you dong got another

BIN = check2

print(f"{Fore.BLUE}[/] Starting.")
time.sleep(3)
while True:

        cc = ('').join(random.choices(string.digits, k=8))
       
        card = BIN + cc 
        check = verify(card)
        if check == True:

                print(f"{Fore.GREEN}[>] {card} is a valid Store Card!")
                f = open("cards.txt",'a')
                f.write(f"{card}\n")
                f.close()
                time.sleep(1)
                

        else:
         print(f"{Fore.RED}[!] {card} is not a valid Store Card!")
         time.sleep(1)


