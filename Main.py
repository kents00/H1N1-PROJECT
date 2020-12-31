#Menu 
#H1N1-PROJECT
import os
import time
def Menu():
  os.system('clear')
  time.sleep(0.001)
  print("""\033[37;1m
  ___________________________________
|                                     |
| .##.....##....##...##....##....##.. |
| .##.....##..####...###...##..####.. |
| .##.....##....##...####..##....##.. |
| .#########....##...##.##.##....##.. |
| .##.....##....##...##..####....##.. |
| .##.....##....##...##...###....##.. |
| .##.....##..######.##....##..###### |
| ___________________________________ |
 = Scrpit By Kents00 | Version 0.001 =
 =====================================""")
 
  print ("\033[35;1m[0].DDOS [1].Password Gen ")
  select = input ("\033[32;1m~H1N1~#")
  
  if select == '0':
    print ("\033[37;1m[1].UDP ATTACK\n[2].SYN ATTACK\n[3].PROXY ATTACK")
    Options = input ("\033[32;1m~H1N1~#")
    if select == '1':
      os.system('clear')
      os.system('sh udp.sh')
    elif select == '2':
      os.system('clear')
      os.system('python tcpsyn.py') 
    elif select == '3':
      os.system('clear')
      os.system('python proxyd.py') 
Main()