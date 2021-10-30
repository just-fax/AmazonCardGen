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
 ▄▄▄       ███▄ ▄███▓ ▄▄▄      ▒███████▒ ▒█████   ███▄    █     ▄████▄   ▄▄▄       ██▀███  ▓█████▄   ██████ 
▒████▄    ▓██▒▀█▀ ██▒▒████▄    ▒ ▒ ▒ ▄▀░▒██▒  ██▒ ██ ▀█   █    ▒██▀ ▀█  ▒████▄    ▓██ ▒ ██▒▒██▀ ██▌▒██    ▒ 
▒██  ▀█▄  ▓██    ▓██░▒██  ▀█▄  ░ ▒ ▄▀▒░ ▒██░  ██▒▓██  ▀█ ██▒   ▒▓█    ▄ ▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌░ ▓██▄   
░██▄▄▄▄██ ▒██    ▒██ ░██▄▄▄▄██   ▄▀▒   ░▒██   ██░▓██▒  ▐▌██▒   ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌  ▒   ██▒
 ▓█   ▓██▒▒██▒   ░██▒ ▓█   ▓██▒▒███████▒░ ████▓▒░▒██░   ▓██░   ▒ ▓███▀ ░ ▓█   ▓██▒░██▓ ▒██▒░▒████▓ ▒██████▒▒
 ▒▒   ▓▒█░░ ▒░   ░  ░ ▒▒   ▓▒█░░▒▒ ▓░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░
  ▒   ▒▒ ░░  ░      ░  ▒   ▒▒ ░░░▒ ▒ ░ ▒  ░ ▒ ▒░ ░ ░░   ░ ▒░     ░  ▒     ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒ ░ ░▒  ░ ░
  ░   ▒   ░      ░     ░   ▒   ░ ░ ░ ░ ░░ ░ ░ ▒     ░   ░ ░    ░          ░   ▒     ░░   ░  ░ ░  ░ ░  ░  ░  
      ░  ░       ░         ░  ░  ░ ░        ░ ░           ░    ░ ░            ░  ░   ░        ░          ░  
                               ░                               ░                            ░              
     -Made By Fax                          
                               ''')


print(f"{Fore.RED}[?] What Bin would you like to use?")
check2 = input(f'{Fore.RED}[?]>')

#60457811 - use this bin if you dong got another




BIN = check2



print(f"{Fore.GREEN}[:] Gen Starting in 3 seconds!.")
time.sleep(3)
while True:

        cc = ('').join(random.choices(string.digits, k=8))
       
        card = BIN + cc 
        check = verify(card)
        if check == True:

                print(f"{Fore.GREEN}[VALID] {card}")
                f = open("Codes.txt",'a')
                f.write(f"{card}\n")
                f.close()
                time.sleep(1)
                

        else:
         print(f"{Fore.RED}[INVALID] {card}")
         time.sleep(1)


