
from socket import *
import argparse
import json
import struct
import time

messageSequenceNumber = 0
limit_reached = False
time_limit = False
bits_sent = 0
init = 0
messageSequenceNumber = 1
packetSize = 4000*8+(16*8) #16 estimated for additional json character
with open('payload.txt', 'r') as myfile:
  payloadMsg = myfile.read()
# def reset():
# 	global limit_reached
# 	global time_limit
# 	global bytes_sent
# 	global init
# 	if (limit_reached == True or time_limit==True):
# 		print("Passed Reset")
# 		limit_reached = False
# 		time_limit = False
# 		bytes_sent = 0

def send_Msg(byteslimit):
	global limit_reached
	global time_limit
	global messageSequenceNumber
	global bits_sent
	json_string = {}
	json_string  = {"msn": messageSequenceNumber, "pl" : payloadMsg }
	jason =json.dumps(json_string)
	data = str(jason)
	sent = sock.sendto(data.encode(),('10.0.0.2',5555))
	messageSequenceNumber += 1
	bits_sent += packetSize + 20*8 + 8*8 # UDP header is 20bytes ip header , 8 bytes udp header
	print("Packet sent with: "+ str(packetSize+ 20*8 + 8*8)+" bits"+ "messageSequenceNumber of : {}".format(messageSequenceNumber))

# def check_time():
# 	global init
# 	global time_limit
# 	currentTime = time.time()
# 	if (currentTime - init >= 1.0):
# 		time_limit = True
# 		print("One second's up")
# 		return True
# 	else: return False

# def check_limit():
# 	global limit_reached
# 	global bytes_sent
# 	if(bytes_sent >= bytelimit):
# 		limit_reached = True
# 		return True
# 	else: return False

def checkSendRate():
	global init
	global bits_sent
	currentTime = time.time()
	timeElapsed = currentTime - init
	return (bits_sent/timeElapsed) / (10**6)


if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-r', type=float, dest='rate',help='Packet rate in Mbps (eg; -r 1.5 is 1.5 Mbps)')
	args = parser.parse_args()
	if args.rate == None:
		print("USAGE:")
		print("python2 client.py -r 3.0:")
	else:
		bytelimit = args.rate*(10**6) #Megabit
		print(bytelimit)
		print("Client sending rate is {} Mbps.".format(args.rate))
		sock = socket(AF_INET, SOCK_DGRAM)
		server_address = ('127.0.0.1', 5555)
		#sock.connect(server_address)
		print("Each packet size is : " + str(packetSize + 20 + 8)+ " bytes")
		init=time.time()	
	#8 bytes is the UDP header which supposed to hold the source port, dest port , length as well as checksum
	# 20 bytes is the IP header (minimum)
		while(True):
			send_Msg(bytelimit)
			time.sleep((packetSize+20*8+8*8)/bytelimit)
			print(str(checkSendRate())+" Megabits/s")

			# if check_time() is True:
			# 	init = time.time()
			# 	bytes_sent = 0
			# else: 
			# 	if check_limit() is True:
			# 		print("Send limit reached, gonna waste time...")
			# 	else:
			# 		send_Msg(bytelimit)
			# 		print(bytes_sent)


