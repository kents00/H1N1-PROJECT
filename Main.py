#H1N1 
#DoS/DDoS Attack Tool
import socket
import os
from tqdm import tqdm
import time
for i in tqdm(range(1000)):
  time.sleep(0.001)
    
os.system('clear')
print ("""\033[37;1m
=====================================
 .##.....##....##...##....##....##..
 .##.....##..####...###...##..####..
 .##.....##....##...####..##....##..
 .#########....##...##.##.##....##..
 .##.....##....##...##..####....##..
 .##.....##....##...##...###....##..
 .##.....##..######.##....##..######
=====================================
= Scrpit By Kents00 | Version 0.001 =
=====================================""")
print ("\033[34;1mType 'Help' to see tools")
select = input ("\033[32;1m~H1N1~#")

if select == "Help":
  os.system('python lrsd.py')
else:
	print ("Invalid")
