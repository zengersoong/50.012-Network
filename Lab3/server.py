#!/usr/bin/python2

"""
Networks Lab 3: UDP Socket Programming

Server code.
"""

from socket import *
import time
import math
import json
import struct
#H2 SERVER
skipList = []
payloadMsg = "This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes.This is a the payload of about 1008 bytes."
def checkSkipList(msn):
    global skipList
    if skipList.contains(msn):
        skipList.remove(msn)


def checkPayload(payload, msn):
    global skipList
    if payload == payloadMsg:
        return True
    else: 
        print("Corruption in payload Detected!")
        skipList.append(msn)
        return False




if __name__ == "__main__":

    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(('10.0.0.2', 5555)) 
    buffersize=4096 # is in bytes
    print("buffer size = "+ str(buffersize))
    previousMsn=0

    while True:
        data, address = sock.recvfrom(buffersize)
        data = data.decode()
        n = json.loads(data)
        print(str(n["msn"])+ " received")
        currentMsn = n["msn"]
        currentPayload = n["pl"]

        if currentMsn - previousMsn !=1:
            #Out of order packets
            skipList.append(currentMsn)

        previousMsn = currentMsn
        if skipList != []: 
            print("Packet mismatch detected!")
            print(str(skipList) + " segments still not received!, likely dropped")




