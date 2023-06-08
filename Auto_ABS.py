import subprocess
import pyautogui as gui
import datetime
import time
import os
import platform

user = [5,6,7,9,12,13,14,10,11,8,3,17,15,16,18]
file = open("log.txt","w")
now = datetime.datetime.now()
file.write("Log Date/time:"+str(now))



def run_automation(i):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    profile =  "--profile-directory=Profile "+str(i)
    subprocess.Popen([chrome_path,profile])
    print("\n----------Initiated for acc no: "+str(i)+" ----------\n")
    file.write("\n----------Initiated for acc no: "+str(i)+" ----------\n")

    print("time.sleep(3)\n")
    time.sleep(3)
    file.write("time.sleep(3)\n")

    print("gui.click(1731,60)\n")
    gui.click(1731,60)
    file.write("gui.click(1731,60)\n")

    print("time.sleep(3)\n")
    time.sleep(3)
    file.write("time.sleep(3)\n")

    print("gui.click(1554,672)\n")
    gui.click(1554,672)
    file.write("gui.click(1554,672)\n")

    print("time.sleep(40)\n")
    time.sleep(40)
    file.write("time.sleep(40)\n")

    print("gui.click(1434,17)\n")
    gui.click(1434,17)
    file.write("gui.click(1434,17)\n")

    print("time.sleep(2)\n")
    time.sleep(2)
    file.write("time.sleep(2)\n")

    print("gui.keyDown('ctrl')\n")
    gui.keyDown('ctrl')
    file.write("gui.keyDown('ctrl')\n")

    print("gui.keyDown('shift')\n")
    gui.keyDown('shift')
    file.write("gui.keyDown('shift')\n")

    print("gui.press('i')\n")
    gui.press('i')
    file.write("gui.press('i')\n")

    print("gui.keyUp('ctrl')\n")
    gui.keyUp('ctrl')
    file.write("gui.keyUp('ctrl')\n")

    print("gui.keyUp('shift')\n")
    gui.keyUp('shift')
    file.write("gui.keyUp('shift')\n")

    print("time.sleep(3)\n")
    time.sleep(3)
    file.write("time.sleep(3)\n")

    print("gui.click(1731,60)\n")
    gui.click(1731,60)
    file.write("gui.click(1731,60)\n")

    print("time.sleep(3)\n")
    time.sleep(3)
    file.write("time.sleep(3)\n")

    print("gui.click(1554,672)\n")
    gui.click(1554,672)
    file.write("gui.click(1554,672)\n")

    print("time.sleep(40)\n")
    time.sleep(40)
    file.write("time.sleep(40)\n")

    print("gui.click(1434,17)\n")
    gui.click(1434,17)
    file.write("gui.click(1434,17)\n")

    print("time.sleep(2)\n")
    time.sleep(2)
    file.write("time.sleep(2)\n")

    print("gui.keyDown('ctrl')\n")
    gui.keyDown('ctrl')
    file.write("gui.keyDown('ctrl')\n")

    print("gui.keyDown('shift')\n")
    gui.keyDown('shift')
    file.write("gui.keyDown('shift')\n")

    print("gui.press('i')\n")
    gui.press('i')
    file.write("gui.press('i')\n")

    print("gui.keyUp('ctrl')\n")
    gui.keyUp('ctrl')
    file.write("gui.keyUp('ctrl')\n")

    print("gui.keyUp('shift')\n")
    gui.keyUp('shift')
    file.write("gui.keyUp('shift')\n")

    print("time.sleep(2)\n")
    time.sleep(2)
    file.write("time.sleep(2)\n")

    print("gui.click(1680,58)\n")
    gui.click(1680,58)
    file.write("gui.click(1680,58)\n")

    print("time.sleep(2)\n")
    time.sleep(2)
    file.write("time.sleep(2)\n")

    print("gui.click(1427,410)\n")
    gui.click(1427,410)
    file.write("gui.click(1427,410)\n")

    print("time.sleep(20)\n")
    time.sleep(20)
    file.write("time.sleep(20)\n")

    print("gui.click(1283,0)\n")
    gui.click(1283,0)
    file.write("gui.click(1283,0)\n")

    print("time.sleep(2)\n")
    time.sleep(2)
    file.write("time.sleep(2)\n")

    print("gui.keyDown('alt')\n")
    gui.keyDown('alt')
    file.write("gui.keyDown('alt')\n")

    print("gui.press('f4')\n")
    gui.press('f4')
    file.write("gui.press('f4')\n")

    print("gui.keyUp('alt')\n")
    gui.keyUp('alt')
    file.write("gui.keyUp('alt')\n")

    print("----------ENDING----------\n")
    file.write("----------ENDING----------\n")


def dash():
    subprocess.Popen(["C:\Program Files\Windscribe\Windscribe.exe"])
    print("\n----------initiating vpn----------")
    file.write("\n----------initiating vpn----------")
    time.sleep(10)
    for i in user:
        run_automation(i)


time = now.strftime("%H")
t = int(time)
print(t)
dash()