import socket
import time
#import thread
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)
print("hello")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()

        while(True):
            conn, addr = s.accept()
            
            #thread.start_new_thread(on_new_client,(conn,addr))
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