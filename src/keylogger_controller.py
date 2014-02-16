
import pyHook, sys, logging, pythoncom, time, threading
import pygame
from pygame.locals import *

file_log = 'E:\\org\\software\\python\\darkSouls\\data\\keylogger3.txt'

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

# I have to ignore all the axis values under 0.9 because the controller use rangs of values to increment gradually the velocity and i'm mapping all the actions
# as keyboard input, which use the maxim value always. To be able to make the movements with the same velocity i will have to use this restriction and make 
# sure to move the analogic all the way every time i want to register the key.
# The other option would be, play with the keyboard directly using the previous program, but i'm more used to the controller.
tolerance = 0.8
 
def threadTime():
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    # logging.log(10,"Estoy en el thread!")
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

        # logging.log(10,str(key_state))
        time.sleep(periode)
        periodCounter+=1

def buttonsController(nButton, value):
    # A: 0
    # B: 1
    # X: 2
    # Y: 3
    # LB: 4
    # RB: 5
    # RB: 5
    # back: 6
    # start: 7
    if nButton == 0:
        # A controller = Q keyboard
        key_state[key_position['Q']] = value
    elif nButton == 1:
        # B controller = Space keyboard
        key_state[key_position['Space']] = value
    elif nButton == 2:
        # X controller = E keyboard
        key_state[key_position['E']] = value
    elif nButton == 3:
        # Y controller = Alt keyboard
        key_state[key_position['Lmenu']] = value
    elif nButton == 4:
        # LB controller = shift keyboard
        key_state[key_position['Lshift']] = value
    elif nButton == 5:
        # RB controller = H keyboard
        key_state[key_position['H']] = value
    elif nButton == 6:
        # back controller = G  keyboard
        key_state[key_position['G']] = value
    elif nButton == 7:
        # start controller = End  keyboard
        key_state[key_position['End']] = value

def axisController(i,axis):
    # Axis:
    # - Left analog: 0->horitzontal (left - ,right + ), 1 -> vertical (up - ,down +)
    # - Triggers (RT + ,LT -): 2
    # - Right analog: 3->vertical (up -, down +) , 4 -> horitzontal (left -, right +)
    # The range is always [-1,1] being the ~0 the starting position.
    # I will use a tolerance of 0.15 before count it as a key press.

    print "Axis: {}, value: {}".format(i,axis)
    # Character movement with left analogic
    if i == 0:
        if abs(axis) < tolerance:
            key_state[key_position['A']] = 0
            key_state[key_position['D']] = 0
        elif axis > tolerance:
            #Right
            key_state[key_position['D']] = 1
        else:
            #Left
            key_state[key_position['A']] = 1

    #No funciona
    elif i == 1:
        if abs(axis) < tolerance:
            key_state[key_position['S']] = 0
            key_state[key_position['W']] = 0
        elif axis > tolerance:
            #Down
            key_state[key_position['S']] = 1
        else:
           #Up
            key_state[key_position['W']] = 1

    #Triggers LT/RT
    elif i == 2:
        if abs(axis) < tolerance:
            key_state[key_position['U']] = 0
            key_state[key_position['Tab']] = 0
        elif axis > tolerance:
           #LT/Counter-attack
            key_state[key_position['Tab']] = 1
        else:
            #RT/Strong-attack
            key_state[key_position['U']] = 1

    #Camera movement with right analogic
    # Value axis:
    # <0.4 nothing
    # >0.4 gradually increment
    # Problem: I'm mapping the analog values of the controller with the discret values of the keyboard. The controller increments the velocity gradually
    # while the keyboard use the maxim value for every press. That's why, if i want to use the controller, i will have to be sure to always move the analogs all
    # the way, to make sure that the movement of the character correspond with the movement it would make using the keyboard
    elif i == 3:
        if abs(axis) < tolerance:
            key_state[key_position['K']] = 0
            key_state[key_position['I']] = 0
        elif axis > tolerance:
            #Down
            key_state[key_position['K']] = 1
        else:
           #Up
            key_state[key_position['I']] = 1
    elif i == 4:
        if abs(axis) < tolerance:
            key_state[key_position['L']] = 0
            key_state[key_position['J']] = 0
        elif axis > tolerance:
            #Down
            key_state[key_position['L']] = 1
        else:
           #Up
            key_state[key_position['J']] = 1

logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
"Opens a window and prints events to the terminal. Closes on ESC or QUIT."
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

thread= threading.Thread(target=threadTime)
# thread.deamon = True
thread.start()

axes = joystick.get_numaxes()
while 1:
        # clock.tick(60)
    try:
        for event in pygame.event.get():
                if event.type == JOYBUTTONDOWN:
                    # logging.log(10,"Down: "+str(event.button))
                    buttonsController(event.button,1)
                elif event.type == JOYBUTTONUP:
                    # logging.log(10,"Up: "+str(event.button))
                    # print "Up: "+str(event.button)
                    buttonsController(event.button,0)
                elif event.type == JOYAXISMOTION:
                    # logging.log(10,"Axis:"+str(event.axis))
                    for i in range(axes):
                        # print "Axis: {}, value: {}".format(i,axes)
                        axis = joystick.get_axis(i)
                        axisController(i,axis)
                                    
    except:
        pass

# pythoncom.PumpMessages()
