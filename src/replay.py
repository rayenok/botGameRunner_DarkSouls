
import pyHook, sys, logging, pythoncom, time, threading, re
import win32api
import time
import win32com.client
  
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")
shell.AppActivate("DARK SOULS")
# You can use this function to obtain the break code from the make
def makeCodeToBreakCode(make):
    return "0x{:02x}".format(make+0x80)

HW_KEY2CODE= {
    'backspace': 0x0E, # Cancel menu
    'tab': 0x0F, # Counter-attack
    'enter': 0x1C, # Accept
    'shift': 0x2A, # Shield defense
    'ctrl': 0x1D, # Walk slow
    'alt': 0x38, # Switch one-handed, dual-handed
    'spacebar': 0x39, # Dodge
    'end': 0xCF, # Menu
    'home': 0xC7, # Windows live
    'a': 0x1E, # Move Left
    'c': 0x2E, # Change left hand
    'd': 0x20, # Move right
    'e': 0x12, # Activate consumable
    'f': 0x21, # Change consumable
    'g': 0x22, # Gesture
    'h': 0x23, # Light attack
    'i': 0x17, # Move up camera
    'j': 0x24, # Move left camera
    'k': 0x25, # Move down camera
    'l': 0x26, # Move right camera
    'o': 0x18, # Puts the camera behind the character and lock enemies
    'r': 0x13, # Change spell
    's': 0x1F, # Move back
    'u': 0x16, # Heavy attack
    'v': 0x2F, # Change right hand
    'w': 0x11, # Move forward
    'q': 0x10, # Pick up objects/open doors 
    'arrowUp': 0xC8, # Move up menu
    'arrowDown': 0xD0, # Move down menu
    'arrowLeft': 0xCB, # Move left menu
    'arrowRight': 0xCD, # Move right menu
    'pageUp': 0xC9, # Move to right menu
    'pageDown': 0xC1 # Move to left menu
}

HW_ACTION2CODE= {
    'cancel':  0x0E, # Cancel menu
    'counter': 0x0F, # Counter-attack
    'accept': 0x1C, # Accept
    'defense': 0x2A, # Shield defense
    'slow': 0x1D, # Walk slow
    'switchWield': 0x38, # Switch one-handed, dual-handed
    'dodge': 0x39, # Dodge
    'menu': 0xCF, # Menu
    'windowsLive': 0xC7, # Windows live
    'left': 0x1E, # Move Left
    'changeLeft': 0x2E, # Change left hand
    'right': 0x20, # Move right
    'useObject': 0x12, # Activate consumable
    'changeObject': 0x21, # Change consumable
    'gesture': 0x22, # Gesture
    'light': 0x23, # Light attack
    'cameraUp': 0x17, # Move up camera
    'cameraLeft': 0x24, # Move left camera
    'cameraDown': 0x25, # Move down camera
    'cameraRight': 0x26, # Move right camera
    'lock': 0x18, # Puts the camera behind the character and lock enemies
    'changeSpell': 0x13, # Change spell
    'back': 0x1F, # Move back
    'heavy': 0x16, # Heavy attack
    'changeRight': 0x2F, # Change right hand
    'forward': 0x11, # Move forward
    'use': 0x10, # Pick up objects/open doors 
    'arrowUp': 0xC8, # Move up menu
    'arrowDown': 0xD0, # Move down menu
    'arrowLeft': 0xCB, # Move left menu
    'arrowRight': 0xCD, # Move right menu
    'pageUp': 0xC9, # Move to right menu
    'pageDown': 0xC1 # Move to left menu
}
file_log = 'E:\\org\\software\\python\\darkSouls\\data\\farmSoulsDrake.txt'
# file_log = 'E:\\org\\software\\python\\darkSouls\\data\\keylogger2.txt'

key_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

key_pressed = {
    '0': 'backspace', '1': 'tab', '2': 'enter', '3': 'shift', '4': 'ctrl', '5': 'alt', 
    '6': 'spacebar', '7': 'end', '8': 'home', '9': 'a', '10': 'c', '11': 'd', 
    '12': 'e', '13': 'f', '14': 'g', '15': 'h', '16': 'i', '17': 'j', '18': 'k', '19': 'l', 
    '20': 'o', '21': 'r', '22': 's', '23': 'u', '24': 'v', '25': 'w', '26': 'q', 
    '27': 'arrowUp', '28': 'arrowDown', '29': 'arrowLeft', 
    '30': 'arrowRight', '31': 'pageUp', '32': 'pageDown', 
}

periode = 0.25
data = {}

def data2Dictionary():
   f = open(file_log,"r")
   for line in f:
      line = line.split("\n")[0]
      period = line.split(":")[0]
      keys = line.split(":")[1].split(",")
      data[period] = keys
   print "data2Dictionary: lastPeriod: "+str(period)
   f.close()
   return period
   # thread= threading.Thread(target=threadTime,args=(int(period)))
   # thread.deamon = True
   # thread.start()

def replay(lastPeriod):
    periodCounter = 0
    print data
    while periodCounter <= int(lastPeriod):
        # line: <period>:<key>,<key>,<key>,....
        print "periodCounter {} <=> {} lastPeriod".format(periodCounter,lastPeriod)
        if str(periodCounter) in data:
            print "Periodo con info:"
            #Grab the keys and do the calls
            for key in data[str(periodCounter)]:
               if key_state[int(key)] == 0:
                   nameKey = key_pressed[key]
                   print "tecla: "+nameKey+" pulsada"
                   win32api.keybd_event(0,HW_KEY2CODE[nameKey],0,0)
                   key_state[int(key)] = 1
            # If there is any extra key active in key_state  but not pressed, update the state
            keysState = [i for i,x in enumerate(key_state) if x == 1]
            keysDown = map(int,data[str(periodCounter)])
            for key in keysState:
                if key not in keysDown:
                   nameKey = key_pressed[str(key)]
                   key_state[int(key)] = 0
                   print "tecla: "+nameKey+" levantada"
                   win32api.keybd_event(0,HW_KEY2CODE[nameKey],KEYEVENTF_KEYUP,0)
        else:
            if 1 in key_state:
                #Key up
                print "Limpia las teclas restantes"
                for x,y in enumerate(key_state):
                    if y == 1:
                        nameKey = key_pressed[str(x)]
                        # key_state[int(key)] = 0
                        key_state[int(x)] = 0
                        print "tecla: "+nameKey+" levantada"
                        win32api.keybd_event(0,HW_KEY2CODE[nameKey],KEYEVENTF_KEYUP,0)
        time.sleep(periode)
        periodCounter+=1

p=data2Dictionary() 
while True:
   replay(p)
   time.sleep(10)
