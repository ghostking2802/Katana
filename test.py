import cv2
import pickle
import socket
import struct
import base64
import numpy as np
BUFF_SIZE=65536
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
sock.bind(("0.0.0.0",5657))
msg, addr= sock.recvfrom(BUFF_SIZE)
print("Got connection from ", addr, " saying ", msg.decode())
while True:
	frame,_=sock.recvfrom(BUFF_SIZE)
	decoded=base64.b64decode(frame, ' /')
	np_data=np.fromstring(decoded, dtype=np.int8)
	dgram=cv2.imdecode(np_data, 1)
	cv2.imshow('Recieving feed.....', dgram)
	key=cv2.waitKey(1) & 0xFF
	if key == ord('q'):
		sock.close()
		break
