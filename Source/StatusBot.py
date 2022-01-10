#Made by: Ignas Mikolaitis
#Website: ignuxas.com

import requests
import random
from colored import fg
from time import sleep
from os import system

black = fg("#424242")
red = fg("#E91E63")

def cls():
    system("cls")
def clt(StatusLen):
    StatLen = StatusLen
    print ("\033[A"+ " "*StatusLen + "\033[A")

#Get Options

cls()

RandomOption = input(black+"Random status? (y / n): "+red)
if RandomOption.upper() == 'Y':
    RandomStatus = True
else:
    RandomStatus = False

def GetTime():
    global SwitchTime
    try:
        TimeOption = input(black+"How many seconds per switch?: "+red)
        SwitchTime = int(TimeOption)
    except:
        print("Please input a number")
        GetTime()
GetTime()

cls()

print(black+"Random Status:"+red, RandomStatus)
print(black+"Seconds Per Switch:"+red, SwitchTime,"\n\n")

#Get Auth Token

authFile = open('DiscordKey.txt', 'r')
auth = authFile.readline()
authFile.close()

headers = {
    'authorization': auth.replace("\n", "")
}

#Get random status
Statuses = []
with open('statuses.txt') as f:
    for line in f:
        Statuses.append(line.replace("\n", ""))

#Functions

lastStatusLen = 0

def RandomDiscordStatus():
    global lastStatusLen

    while True:
        Status = random.choice(Statuses)
        payload = {"custom_status":{"text": Status}}

        PatchDiscord(payload)
        clt(lastStatusLen)
        print(black+"Current Status: "+red+Status)
        sleep(SwitchTime)
        lastStatusLen = len(Status)+16

def OrederedDiscordStatus():
    global lastStatusLen
    
    for Status in Statuses:
        payload = {"custom_status":{"text": Status}}

        PatchDiscord(payload)
        clt(lastStatusLen)
        print(black+"Current Status: "+red+Status)
        sleep(SwitchTime)
        lastStatusLen = len(Status)+16

    OrederedDiscordStatus()

def PatchDiscord(payload):
    r = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=payload)
    if r.status_code != 200:
        cls()
        print(red+"Please enter a correct Discord Token and try again")
        input()
        exit()

#Start Bot

if (RandomStatus == True):
    RandomDiscordStatus()
else:
    OrederedDiscordStatus()
