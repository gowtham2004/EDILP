#EDILP(Even Dead Iam Lonley_Programmer</>) 
#An Intelligent Assistant for Lonley_programmer<Hemasundar>
#copyright@2023 by spidey industries

import pyttsx3
from datetime import datetime
import http.client as httplib
import requests
import psutil

netstate = False
now = datetime.now()
#engine set up
eng = pyttsx3.init('sapi5')
#properties
vol = eng.getProperty("volume")
#print("volume:",vol)
rate = eng.getProperty("rate")
#print("Rate:",rate)
eng.setProperty('rate',150)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
##print (voices [1].id)
#for voice in voices:
    ##print(voice.id)
engine.setProperty('voice', voices[1].id)

#modules
def edilp_term():
    print("--------------------INITIALIZING EDILP PROCESSES--------------------\n");
    print("STARTING EDILP!.....")
    sym = "#" #input("Enter a character to #print letter:")
    rows = 7
    col = 29
    for i in range(0,rows+1):
        for j in range(0,col+1):
            if((i==1 and j==1)or(i==2 and j==1)or(i==3 and j==1)or(i==4 and j==1)or(i==5 and j==1)or(i==6 and j==1)or(i==7 and j==1)or(i==1 and j==2)or(i==4 and j==2)or(i==7 and j==2)or(i==1 and j==3)or(i==4 and j==3)or(i==7 and j==3)or(i==1 and j==4)or(i==4 and j==4)or(i==7 and j==4)or(i==1 and j==5)or(i==4 and j==5)or(i==7 and j==5)or(i==1 and j==7)or(i==2 and j==7)or(i==3 and j==7)or(i==4 and j==7)or(i==5 and j==7)or(i==6 and j==7)or(i==7 and j==7)or(i==1 and j==8)or(i==7 and j==8)or(i==1 and j==9)or(i==7 and j==9)or(i==2 and j==10)or(i==6 and j==10)or(i==3 and j==11)or(i==4 and j==11)or(i==5 and j==11)or(i==1 and j==13)or(i==7 and j==13)or(i==1 and j==14)or(i==7 and j==14)or(i==1 and j==15)or(i==2 and j==15)or(i==3 and j==15)or(i==4 and j==15)or(i==5 and j==15)or(i==6 and j==15)or(i==7 and j==15)or(i==1 and j==16)or(i==7 and j==16)or(i==1 and j==17)or(i==7 and j==17)or(i==1 and j==19)or(i==2 and j==19)or(i==3 and j==19)or(i==4 and j==19)or(i==5 and j==19)or(i==6 and j==19)or(i==7 and j==19)or(i==7 and j==20)or(i==7 and j==21)or(i==7 and j==22)or(i==7 and j==23)or(i==1 and j==25)or(i==2 and j==25)or(i==3 and j==25)or(i==4 and j==25)or(i==5 and j==25)or(i==6 and j==25)or(i==7 and j==25)or(i==1 and j==26)or(i==4 and j==26)or(i==1 and j==27)or(i==4 and j==27)or(i==2 and j==28)or(i==3 and j==28)):          
                print(sym, end = '')
            else:
                print(' ', end = '')
        print()
    print("\nYOUR INELLIGENT ASSISTANT</>");

def greet():
    time = now.strftime("%H")
    t = int(time)
    if (1 <= t < 11):
       eng.say("GOOD MORNING sir")
    elif(11 <= t < 16):
       eng.say("GOOD AFTERNOON sir")
    elif(16 <= t < 18):
        eng.say("GOOD EVENING sir")
    else:
        eng.say("WONDERFUL NIGHT sir")
    eng.say("it's EDILP"+" "+"your intillegent assistant")
    eng.say("Services and process are firing up")

#network availablity
def netcheck(url="www.geeksforgeeks.org",timeout=3):
    connection = httplib.HTTPConnection(url,timeout=timeout)
    try:
        connection.request("HEAD", "/")
        connection.close()  # connection closed
        #print("Internet On")
        eng.say("Network is currently Activated")
        return True
    except Exception as exep:
        #print(exep)
        eng.say("Network not Activated")
        return False

#current time
def time():
    H = now.strftime("%H")
    M = now.strftime("%M")
    mer = "AM"
    h = int(H)
    m = int(M)
    M = str(m)
    if(h==00):
        H = str(12)
    if(h>12):
        h -= 12
        H = str(h)
        mer = "PM"
    if(m==0):
        M = ""
    #print("TIME:"+H+" "+M+" "+mer)
    eng.say("Its"+" "+H+" "+M+" "+mer)

#current weather
def weather():
        api_key = "8aa0ae2e5e8dbf6f9cfdaf96b12b100c"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + "karur"
        #print(complete_url)
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] not in ["404","401"]:
            y = x["main"]
            current_temperature = y["temp"] - 273.15
            current_temperature = int(current_temperature)
            z = x["weather"]
            weather_state = z[0]["description"]
            #print("weather:",current_temperature)
            #print("state:",weather_state)
            eng.say("its currently"+str(current_temperature)+"degree celsius"+"with"+" "+str(weather_state))

#battery check
def bat_check():
    battery = psutil.sensors_battery()
    bat = str(battery.percent)
    eng.say(bat+"Percent Charge remaining")

edilp_term()
greet()
time()
if(netcheck()):
    weather()
bat_check()
eng.say("System is now ready to rock")
eng.runAndWait()

