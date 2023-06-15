import subprocess_maximize as subprocess
from pyautogui import *
import pyautogui as gui
import time as tt
import os

user = [5,6,7,9,12,13,14,10,11,8,3,17,15,16,18,19,20,21,22,4]
select = [10,11,8,3,17,15,16,18,19,20,21,22,4]



def search(i):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    profile =  "--profile-directory=Profile "+str(i)
    subprocess.Popen([chrome_path,profile],show='maximize', priority=0)
    print("\n----------Initiated for acc no: "+str(i)+" ----------\n")

    print("tt.sleep(3)\n")
    tt.sleep(3)

    print("gui.click(1731,60)\n")
    gui.click(1731,60)

    print("tt.sleep(3)\n")
    tt.sleep(3)

    print("gui.click(1607,763)\n")
    gui.click(1607,763)

    print("tt.sleep(40)\n")
    tt.sleep(40)

    print("gui.click(1434,17)\n")
    gui.click(1434,17)

    print("tt.sleep(2)\n")
    tt.sleep(2)

    print("gui.keyDown('ctrl')\n")
    gui.keyDown('ctrl')

    print("gui.keyDown('shift')\n")
    gui.keyDown('shift')

    print("gui.press('i')\n")
    gui.press('i')

    print("gui.keyUp('ctrl')\n")
    gui.keyUp('ctrl')

    print("gui.keyUp('shift')\n")
    gui.keyUp('shift')

    print("tt.sleep(3)\n")
    tt.sleep(3)

    print("gui.click(1731,60)\n")
    gui.click(1731,60)

    print("tt.sleep(3)\n")
    tt.sleep(3)

    print("gui.click(1604,767)\n")
    gui.click(1604,767)

    print("tt.sleep(40)\n")
    tt.sleep(40)

    print("gui.click(1434,17)\n")
    gui.click(1434,17)

    print("tt.sleep(2)\n")
    tt.sleep(2)

    print("gui.keyDown('ctrl')\n")
    gui.keyDown('ctrl')

    print("gui.keyDown('shift')\n")
    gui.keyDown('shift')

    print("gui.press('i')\n")
    gui.press('i')

    print("gui.keyUp('ctrl')\n")
    gui.keyUp('ctrl')

    print("gui.keyUp('shift')\n")
    gui.keyUp('shift')

    print("tt.sleep(2)\n")
    tt.sleep(2)

    print("gui.click(1680,58)\n")
    gui.click(1680,58)

    print("tt.sleep(2)\n")
    tt.sleep(2)

    print("gui.click(1427,410)\n")
    gui.click(1427,410)

    print("tt.sleep(20)\n")
    tt.sleep(20)

    print("gui.click(1283,0)\n")
    gui.click(1283,0)

    print("tt.sleep(2)\n")
    tt.sleep(2)

    print("gui.keyDown('alt')\n")
    gui.keyDown('alt')

    print("gui.press('f4')\n")
    gui.press('f4')

    print("gui.keyUp('alt')\n")
    gui.keyUp('alt')

    print("----------ENDING----------\n")

def Activity(cid):
    t = 1
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    profile =  "--profile-directory=Profile "+str(cid)
    subprocess.Popen([chrome_path,profile],show='maximize', priority=0)

    print("\n----------Initiated for acc no: "+str(cid)+" ----------\n")
    print("Account Initiated for Acc_id:",cid)

    tt.sleep(5)

    gui.click(380,65)
    print("click(380,65)")
    
    tt.sleep(2)
    print("tt.sleep(2)")

    gui.typewrite("https://rewards.bing.com")
    print("typing https://rewards.bing.com")

    gui.press("enter")
    print("Pressing Enter")

    while 1:
        w_icon = gui.locateOnScreen('Image Ess/MSR.png',grayscale=True, confidence=0.8)
        if w_icon != None:
            print("Page Occur")
            gui.click(1840,340)
            break
        print("page Miss")
    
    #Image Checking Mod for Bing Search
    while 1:
        while t == 100:
            break
        end_img = gui.locateOnScreen('Image Ess/yg.png',grayscale=True, confidence=0.8)
        plus_img = gui.locateOnScreen('Image Ess/plus.bmp',confidence=0.8)
        if end_img != None:
            break
        if plus_img != None:
            x,y = gui.center(plus_img)
            print("HIT:",x,y)
            
            gui.click(x,y)
            print("Click plus")

            #To find X_mark Exist or Not
            tt.sleep(2)
            X_mark = gui.locateOnScreen('Image Ess/xmark.png',region=(0,90,1920,1017))
            if X_mark != None:
                print("Xmark occur")
                x,y = gui.center(X_mark)
                tt.sleep(5)
                gui.click(x,y)
                print("Click xmark:",x,y)
                tt.sleep(5)
                continue
            
            print("Sleep(20)")
            tt.sleep(20)
            

            print("gui.keyDown('ctrl')\n")
            gui.keyDown('ctrl')

            print("gui.press('w')\n")
            gui.press('w')

            print("gui.keyUp('ctrl')\n")
            gui.keyUp('ctrl')

            tt.sleep(5)
            print("Sleep(5)")
        else:
            print("MISS")
            gui.scroll(-100)
            print("Scroll")
            tt.sleep(1)
            t = t + 1

    print("gui.keyDown('alt')\n")
    gui.keyDown('alt')

    print("gui.press('f4')\n")
    gui.press('f4')

    print("gui.keyUp('alt')\n")
    gui.keyUp('alt')


def dash():
    #subprocess.Popen(["C:\Program Files\Windscribe\Windscribe.exe"])
    #print("\n----------initiating vpn----------")
    #tt.sleep(10)
    #for i in select:
    #   search(i)
    for i in user:
        Activity(i)

def shutdown_pc():
  os.system("shutdown /s /t 0")

#os.system("shutdown /s /t 7200")
print("shutdown timer set hogaya")
dash()
shutdown_pc()