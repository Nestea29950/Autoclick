from statistics import quantiles
from pyautogui import *
import time
import keyboard
import random
import sys, bot, keyboard
from time import sleep
import sys
import threading


pausee = False

def pause():
    while True:
        if keyboard.is_pressed('q'):
            pausee = True
            print(pausee)

def clicker():
    while True:
        if pausee == False:
            click()
            print(pausee)
            time.sleep(2)
            print("click")
        else:
            break

th1 = threading.Thread(target=pause)
th2 = threading.Thread(target=clicker)

th1.start()
th2.start()

th1.join()
th2.join()