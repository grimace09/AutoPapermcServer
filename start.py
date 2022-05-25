import tkinter.messagebox
import os
import urllib.request

url = "https://eternallybored.org/misc/wget/1.21.3/64/wget.exe"
filename = "wget.exe"
urllib.request.urlretrieve(url, filename)

os.system('wget https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/344/downloads/paper-1.18.2-344.jar')
os.system('wget https://playit.gg/downloads/playit-0.8.1-beta-signed.exe')
os.system('wget https://raw.githubusercontent.com/grimace09/AutoPapermcServer/main/start.bat')
os.system('del wget.exe')
os.system('paper-1.18.2-344.jar')
tkinter.messagebox.showinfo(title="Instructions", message="Once youre done dealing with the EULA just double click start.bat and your server should start. :)" )
os.system('notepad eula')
os.system('del start.py')