import subprocess
import pyautogui as gui
import datetime
import time
import os
import platform

user = [5,6,7,9,12,13,14,10,11,8,3]
choice=[5,6,7,9,12,13,14,10,11,8,3]
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


def default(j,f):
    if f == 404:
        #default 
        for i in user:
            run_automation(i)
        subprocess.Popen(["C:\Program Files\Windscribe\Windscribe.exe"])
        print("\n----------initiating vpn----------")
        file.write("\n----------initiating vpn----------")
        time.sleep(10)
        for i in user:
            run_automation(i)

    elif f == 452:
        #continue 
        L = len(user)
        for k in range(j,L):
            run_automation(user[k])
        subprocess.Popen(["C:\Program Files\Windscribe\Windscribe.exe"])
        print("\n----------initiating vpn----------")
        file.write("\n----------initiating vpn----------")
        time.sleep(10)
        for i in user:
            run_automation(i)

    elif f == 450:
        #default only
        for i in user:
            run_automation(i)

    elif f == 440:
        #vpn only
        subprocess.Popen(["C:\Program Files\Windscribe\Windscribe.exe"])
        print("\n----------initiating vpn----------")
        file.write("\n----------initiating vpn----------")
        time.sleep(10)
        for i in user:
            run_automation(i)

    elif f == 420:
        #vpn continue
        L = len(user)
        for k in range(j,L):
            run_automation(user[k])

    else:
         run_automation(user[j])


    
def home():
    print("1)Normal\n2)Continue\n3)single\n4)default only\n5)vpn only\n6)vpn continue\n")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        default(0,404)
    elif ch == 2:
        print("Enter the id number to continue:")
        print("DGSpidey - 0\nSpideycoder - 1\nSpideyhacker - 2\nC - 3\nFlutter - 4\nGowtham - 5\njava - 6\njavascript - 7\nPython - 8\nR - 9\nVS code - 10")
        c = int(input("Enter your choice to continue:"))
        if c <= 10:
            default(c,452)
        else:
            print("Aww snap! sorry try again")
    elif ch == 3:
        print("Enter the id number to open:")
        print("DGSpidey - 0\nSpideycoder - 1\nSpideyhacker - 2\nC - 3\nFlutter - 4\nGowtham - 5\njava - 6\njavascript - 7\nPython - 8\nR - 9\nVS code - 10")
        c = int(input("Enter your choice to open:"))
        if c <= 10:
            default(c,400)
        else:
            print("Aww snap! sorry try again")
            home()
    elif ch == 4:
        default(0,450)
    elif ch == 5:
        default(0,440)
    elif ch == 6:
        print("Enter the id number to continue:")
        print("DGSpidey - 0\nSpideycoder - 1\nSpideyhacker - 2\nC - 3\nFlutter - 4\nGowtham - 5\njava - 6\njavascript - 7\nPython - 8\nR - 9\nVS code - 10")
        c = int(input("Enter your choice to continue:"))
        if c <= 10:
            default(c,420)
        else:
            print("Aww snap! sorry try again")
    else:
        print("Aww snap! sorry try again")
        home()

print("MSR automata")
print("developer:lonley_programmer</>")
home()

#subprocess.Popen(["C:\Program Files\Windscribe\Windscribe.exe"])
#time.sleep(20)
#subprocess.Popen(["C:\Program Files (x86)\MacroRecorder\MacroRecorder.exe"])


# test
#subprocess.Popen(["C:\Program Files\Windscribe\Windscribe.exe"]) 
#time.sleep(2)
#for i in range(0,10000):
#            print("\n"+str(i))
#            if connect():
#                break
#subprocess.Popen(["C:\Program Files (x86)\MacroRecorder\MacroRecorder.exe"])
    
