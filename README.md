# Advance-Hack-with-python
A advance hacking script made in python.
This scripts establishes a connection between the victim and the server and then the server can pass on certain hacking commnads to the client script

Powers of `Server.py`-
1. Access to passwords of all the WIFI's that the victim has ever connected to `(Command - all wifi)`

2. Access to the victim's computer name `(Command - name)`

3. Access to the names of all the users on the victim's computer `(Command - get_user)`

4. Access to victim's public ip `(Command - public ip)`

5. Complete access over Victim's mouse `(Command - Click <1> or <2> ; move <x,y>)`

6. Can boot crash the victim's system(BSOD; works only on win10)  `(Command - crash)`

7. Can shutdown victim's computer anytime `(Command - shutdown)`

8. Access to ipv4 `(Command - ipv4)`

9. Can delete permanentely any file/folder on victim's computer `(Command - del <file_path> or delfld <folder_path> )`

10. Can get the script's location `(Command - cwd)`

11. Can open any url on victim's pc `(Command - openweb <url> )`

12. Access to details of all the programmes running on victim's pc (Just like taskbar) `(Command - pwr Get-Process)`

13. Can get to the on which OS is the victims's computer running on `(Command - OS)`

# How to get this code working?
I) Send the `Hack.pyw` script to the victim's computer

II) On the server side open cmd and run `pip -r install requirements.txt`

III) Perform port forwarding and enter your `public ip` and `port` in the `Hack.pyw` script

IV) Run the `Server.py` and then run `Hack.pyw` script
