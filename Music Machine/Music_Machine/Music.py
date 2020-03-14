# Niranjan prof
#https://github.com/Niranjanprof
#Mailme @ niranjannb7777@gmail.com

# Music Machine Project

# Open a online virtual piano or drumming web site  RUN THE CODE CHANGE THE PORT as of Arduino's in step 15



import serial       # for port
import time         # for time.sleep
import pyautogui    # pressing keys
from pygame import mixer  # playing music

# ser is a filehandler
ser = serial.Serial('COM6',9600)  # specify your port

time.sleep(2)
time.sleep(2)

while(True):  # infinite loop
    aaa = ser.readline()       # collecting string from Serial monitor
    aaa = aaa.decode()
    aaa = aaa.rstrip()
    a = aaa.find('+')          # Finding the added symbols
    b = aaa.find('-')
    s1 = aaa[0:a]
    s2 = aaa[a+1:b]            # Spliting the Strings
    s3 = aaa[b+1:len(aaa)]
    if (s1.isdigit() and s2.isdigit() and s3.isdigit()) :
        r1 = int(s1)
        r3 = int(s2)              # Converting them to Integers
        r2 = int(s3)

# Controller 1
        if(r1<3):
            pyautogui.press('a')     # a will be pressed
        if (r1 >= 3 and r1 < 6):
            pyautogui.press('b')
        if (r1 >= 6 and r1 < 9):
            pyautogui.press('c')
        if (r1 >=9 and r1 < 12):
            pyautogui.press('d')
        if (r1 >=12 and r1 < 15):
            pyautogui.press('e')
        if (r1 >=15 and r1 < 18):
            pyautogui.press('f')
        if (r1 >=18 and r1 < 21):
            pyautogui.press('g')
        if (r1 >=21 and r1 < 24):
            pyautogui.press('h')
        if (r1 >=24 and r1 < 27):
            pyautogui.press('i')
        if (r1 >=27 and r1 < 30):
            pyautogui.press('j')
        if (r1 >=30 and r1 < 33):
            pyautogui.press('k')
# Controller 2
        if (r2 < 3):
            pyautogui.press('l')
        if (r2 >=3 and r2 < 6):
            pyautogui.press('m')
        if (r2 >=6 and r2 < 9):
            pyautogui.press('n')
        if (r2 >=9 and r2 < 12):
            pyautogui.press('o')
        if (r2 >=12 and r2 < 15):
            pyautogui.press('p')
        if (r2 >=15 and r2 < 18):
            pyautogui.press('q')
        if (r2 >=18 and r2 < 21):
            pyautogui.press('r')
        if (r2 >=21 and r2 < 24):
            pyautogui.press('s')
        if (r2 >=24 and r2 < 27):
            pyautogui.press('t')
        if (r2 >=27 and r2 < 30):
            pyautogui.press('u')
        if (r2 >=30 and r2 < 33):
            pyautogui.press('v')
        if (r2 >=33 and r2 < 36):
            pyautogui.press('w')
# Music Controller
        if (r3 < 5):
            mixer.init()
            mixer.music.load('h.mp3')    # give address of the music inside
            mixer.music.play()
        if (r3 >= 5 and r3 < 10) :
            mixer.init()
            mixer.music.load('ml.mp3')
            mixer.music.play()
        if (r3 >= 10 and r3 < 15) :
            mixer.init()
            mixer.music.load('p.mp3')
            mixer.music.play()
        if (r3 >= 15 and r3 < 20) :
            mixer.init()
            mixer.music.load('in.mp3')
            mixer.music.play()
        if (r3 >= 20 and r3 < 25) :
            mixer.init()
            mixer.music.load('mi.mp3')
            mixer.music.play()
