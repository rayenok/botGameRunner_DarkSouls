
import pyHook, sys, logging, pythoncom, time, threading

file_log = 'E:\\org\\software\\python\\darkSouls\\data\\keylogger2.txt'

key_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
key_position = {
    'Back': 0, 'Tab': 1, 'Return': 2, 'Lshift': 3, 'Lcontrol': 4, 'Lmenu': 5,
    'Space': 6, 'End': 7, 'Home': 8, 'A': 9, 'C': 10, 'D': 11, 
    'E': 12, 'F': 13, 'G': 14, 'H': 15, 'I': 16, 'J': 17, 'K': 18, 'L': 19,
    'O': 20, 'R': 21, 'S': 22, 'U': 23, 'V': 24, 'W': 25, 'Q': 26, 
    'Up': 27, 'Down': 28, 'Left': 29, 
    'Right': 30, 'Prior': 31, 'Next': 32,
}

periode = 0.25

import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")
shell.AppActivate("DARK SOULS")

def threadTime():
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    periodCounter = 0
    while True:
        # line: <period>:<key>,<key>,<key>,....
        if 1 in key_state:
            line=str(periodCounter)+":"
            for key,x in enumerate(key_state):
                if x == 1:
                    line += str(key)+","
            if line:
                logging.log(10,line[:-1])

        time.sleep(periode)
        periodCounter+=1

def OnKeyDown(event):
    # key = chr(event.Ascii)
    key = event.GetKey()
    # logging.log(10,event.Ascii)
    # logging.log(10,"getKey: "+event.GetKey())
    if key in key_position:
        if key_state[key_position[key]]  is 0:
            key_state[key_position[key]] = 1
    return True

def OnKeyUp(event):
    # key = chr(event.Ascii)
    key = event.GetKey()
    # logging.log(10,"getKey: "+event.GetKey())
    # logging.log(10,event.Ascii)
    if key in key_position:
        if key_state[key_position[key]]  is 1:
            key_state[key_position[key]] = 0
    return True

logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyDown
hooks_manager.KeyUp= OnKeyUp
hooks_manager.HookKeyboard()
thread= threading.Thread(target=threadTime)
# thread.deamon = True
thread.start()
pythoncom.PumpMessages()
