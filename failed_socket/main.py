import socket
import ctypes
import sys
import time
from multiprocessing import Process, Queue
import multiprocessing as mp
import subprocess





def otherprocess():
    subprocess.Popen(['main.love'],shell=True)



if __name__ == '__main__':
    with open("hostinfo.txt","r") as f:
        a = f.read()
        a = a.split("\n")
    
    proc = Process(target = otherprocess)
    proc.start()

    host = '127.0.0.1'
    port=a[1]
    
    print("connection trying...")
    
    socket = socket.socket()
    socket.connect((host, int(port)))
    
    
    socket.sendall("fontDATA".encode("utf-8"))
    
    socket.close()
    p.join()
    