
import pyHook, sys, logging, pythoncom, time, threading

file_log = 'E:\\org\\software\\python\\darkSouls\\data\\keylogger.txt'

key_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
key_position = {
    'backspace': 0, 'tab': 1, 'enter': 2, 'shift': 3, 'ctrl': 4, 'alt': 5,
    'spacebar': 6, 'end': 7, 'home': 8, 'a': 9, 'c': 10, 'd': 11, 
    'e': 12, 'f': 13, 'g': 14, 'h': 15, 'i': 16, 'j': 17, 'k': 18, 'l': 19,
    'o': 20, 'r': 21, 's': 22, 'u': 23, 'v': 24, 'w': 25, 'q': 26, 
    'arrowUp': 27, 'arrowDown': 28, 'arrowLeft': 29, 
    'arrowRight': 30, 'pageUp': 31, 'pageDown': 32,
}

# Aproximatly 1 KB/s
periode = 0.1

def threadTime():
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    while True:
        logging.log(10,":".join(map(str,key_state)))
        time.sleep(periode)

def OnKeyDown(event):
    key = chr(event.Ascii)
    if key in key_position:
        if key_state[key_position[key]]  is 0:
            key_state[key_position[key]] = 1
    return True

def OnKeyUp(event):
    key = chr(event.Ascii)
    if key in key_position:
        if key_state[key_position[key]]  is 1:
            key_state[key_position[key]] = 0
    return True

logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyDown
hooks_manager.KeyUp= OnKeyUp
hooks_manager.HookKeyboard()
threadDeadTime = threading.Thread(target=threadTime)
# thread.deamon = True
threadTime.start()
pythoncom.PumpMessages()
