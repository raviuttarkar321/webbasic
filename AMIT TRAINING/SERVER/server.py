import socket
#from _thread import *
import threading
import time

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)
print("hello")

"""to create new thread for serving client connection"""
def serv_client(conn1,addr1):
    print("in thread1")
    """with conn1:
                print('Connected by', addr1)
                while True:
                    data = conn1.recv(1024)
                    if not data:
                        print("no data received")
                        break
                    print(type(data),data)
                    s=str(data)
                    
                    s=s.upper()
                    print(s)
                    #time.sleep(30)
                    
                    conn.sendall(s.encode())"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    
    
    while True:
        sock.listen()

        while(True):
            conn, addr = sock.accept()
            #threading.Thread(target=serv_client, args=(conn,addr))
            
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        print("no data received")
                        break
                    print(type(data),data)
                    s=str(data)
                    
                    s=s.upper()
                    print(s)
                    #time.sleep(30)
                    
                    conn.sendall(s.encode())
                    i=i+1"""