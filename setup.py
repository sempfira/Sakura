import os
import time
from time import sleep
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")

print("Пожалуйста подождите..")
sleep(2)
print("\nУстановка...")
sleep(2)
os.system("pkg update && pkg upgrade && pkg install git && pkg install python && git clone https://github.com/sempfira/Sakura.git && cd Sakura && pip install -r requirements.txt && python Sakura.pyc")
