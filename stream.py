import cv2
import io
import socket
import struct
import time
import pickle
import zlib
import imutils
import base64
BUFF_SIZE=65536
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
msg=b"Hello"
sock.sendto(msg,("192.168.100.166", 5657))
vid=cv2.VideoCapture(0)
fps,st,frames_to_count,cnt={60,3,20,4}
while True:
    WIDTH=400
    while(vid.isOpened()):
        _,frame=vid.read()
        frame=imutils.resize(frame, width=WIDTH)
        encoded, buffer=cv2.imencode('.jpg', frame,[cv2.IMWRITE_JPEG_QUALITY,80])
        message=base64.b64encode(buffer)
        sock.sendto(message,("192.168.100.166", 5657))
        key=cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            sock.close()
            break

