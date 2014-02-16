
# Only for debug
import win32api
import time
import win32com.client
  
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
#import dictionary
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
import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")
shell.AppActivate("DARK SOULS")

def enter():
    time.sleep(0.05)
    win32api.keybd_event(0,HW_ACTION2CODE['accept'],0,0)
    time.sleep(0.05)
    win32api.keybd_event(0,HW_ACTION2CODE['accept'],KEYEVENTF_KEYUP,0)

def up():
    time.sleep(0.05)
    win32api.keybd_event(0,HW_ACTION2CODE['arrowUp'],0,0)
    time.sleep(0.05)
    win32api.keybd_event(0,HW_ACTION2CODE['arrowUp'],KEYEVENTF_KEYUP,0)

def down():
    time.sleep(0.05)
    win32api.keybd_event(0,HW_ACTION2CODE['arrowDown'],0,0)
    time.sleep(0.05)
    win32api.keybd_event(0,HW_ACTION2CODE['arrowDown'],KEYEVENTF_KEYUP,0)

def left():
    time.sleep(0.05)
    win32api.keybd_event(0,HW_ACTION2CODE['arrowLeft'],0,0)
    time.sleep(0.05)
    win32api.keybd_event(0,HW_ACTION2CODE['arrowLeft'],KEYEVENTF_KEYUP,0)

time.sleep(3)
enter()

enter()

time.sleep(0.5)
# B virtual key
win32api.keybd_event(0x42,0,0,0)

time.sleep(0.1)
# O virtual key
win32api.keybd_event(0x4F,0,0,0)

time.sleep(0.1)
# T virtual key
win32api.keybd_event(0x54,0,0,0)

time.sleep(0.1)
# Return virtual key
win32api.keybd_event(0x0D,0,0,0)

enter()
enter()
enter()
down()
down()
enter()
time.sleep(0.5)
enter()
up()
up()
up()
enter()
enter()
enter()
enter()
enter()
enter()
enter()
enter()
enter()

enter()
left()
enter()
