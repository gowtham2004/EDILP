import subprocess
import pyautogui as gui
import datetime
import time as tt
import os

user = [5,6,7,9,12,13,14,10,11,8,3,17,15,16,18,19,20,21,22,4]
file = open("log.txt","w")
now = datetime.datetime.now()
file.write("Log Date/time:"+str(now))



def run_automation(i):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    profile =  "--profile-directory=Profile "+str(i)
    subprocess.Popen([chrome_path,profile])
    print("\n----------Initiated for acc no: "+str(i)+" ----------\n")
    file.write("\n----------Initiated for acc no: "+str(i)+" ----------\n")

    print("tt.sleep(3)\n")
    tt.sleep(3)
    file.write("tt.sleep(3)\n")

    print("gui.click(1731,60)\n")
    gui.click(1731,60)
    file.write("gui.click(1731,60)\n")

    print("tt.sleep(3)\n")
    tt.sleep(3)
    file.write("tt.sleep(3)\n")

    print("gui.click(1607,763)\n")
    gui.click(1607,763)
    file.write("gui.click(1607,763)\n")

    print("tt.sleep(40)\n")
    tt.sleep(40)
    file.write("tt.sleep(40)\n")

    print("gui.click(1434,17)\n")
    gui.click(1434,17)
    file.write("gui.click(1434,17)\n")

    print("tt.sleep(2)\n")
    tt.sleep(2)
    file.write("tt.sleep(2)\n")

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

    print("tt.sleep(3)\n")
    tt.sleep(3)
    file.write("tt.sleep(3)\n")

    print("gui.click(1731,60)\n")
    gui.click(1731,60)
    file.write("gui.click(1731,60)\n")

    print("tt.sleep(3)\n")
    tt.sleep(3)
    file.write("tt.sleep(3)\n")

    print("gui.click(1604,767)\n")
    gui.click(1604,767)
    file.write("gui.click(1604,767)\n")

    print("tt.sleep(40)\n")
    tt.sleep(40)
    file.write("tt.sleep(40)\n")

    print("gui.click(1434,17)\n")
    gui.click(1434,17)
    file.write("gui.click(1434,17)\n")

    print("tt.sleep(2)\n")
    tt.sleep(2)
    file.write("tt.sleep(2)\n")

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

    print("tt.sleep(2)\n")
    tt.sleep(2)
    file.write("tt.sleep(2)\n")

    print("gui.click(1680,58)\n")
    gui.click(1680,58)
    file.write("gui.click(1680,58)\n")

    print("tt.sleep(2)\n")
    tt.sleep(2)
    file.write("tt.sleep(2)\n")

    print("gui.click(1427,410)\n")
    gui.click(1427,410)
    file.write("gui.click(1427,410)\n")

    print("tt.sleep(20)\n")
    tt.sleep(20)
    file.write("tt.sleep(20)\n")

    print("gui.click(1283,0)\n")
    gui.click(1283,0)
    file.write("gui.click(1283,0)\n")

    print("tt.sleep(2)\n")
    tt.sleep(2)
    file.write("tt.sleep(2)\n")

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
    tt.sleep(10)
    for i in user:
        run_automation(i)
    file.close()

def shutdown_pc():
  os.system("shutdown /s /t 0")


time = now.strftime("%H")
t = int(time)
print(t)
if(t == 1):
    dash()
    shutdown_pc()
