import os
import socket
print ("\033[37;1m[1].UDP ATTACK\n[2].SYN ATTACK\n[3].PROXY ATTACK")
select = input ("\033[32;1m~H1N1~#")
if select == "1" :
  os.system('clear')
  os.system(' sh udp.sh')
elif select == "2" :
	os.system('clear')
	os.system('python tcpsyn.py')
elif select == "3" :
	os.system('clear')
	os.system('python2 proxyd.py')
elif select == "Help":
  os.system('python Help.py')
else:
	print ("Invalid")
