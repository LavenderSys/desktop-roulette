import random
import os

username = os.getlogin()

folder_path = ("C:/Users/"+username+"/Desktop")

desktop = os.listdir(folder_path)
desktop.remove("desktop.ini")    
desktop.remove("DESKTOP-ROULETTE.py")

random_variable = random.choice(desktop)

print("Launching",random_variable+"...")
os.startfile("C:/Users/"+username+"/Desktop/"+random_variable)
