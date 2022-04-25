from tkinter import *
import threading
import sys
import time
from turtle import bgcolor
import RPi.GPIO as GPIO
from RotaryEncoder import RotaryEncoder

# (!) use BOARD NRs for PINs
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

counter = 0

def main_loop():
    while True:
        if GPIO.input(12) == GPIO.LOW:
            buttons[counter].invoke()
            buttons[counter].config(relief=SUNKEN)
            print(f'BUTTON {counter + 1}')
            time.sleep(0.1)
            buttons[counter].config(relief=RAISED)
#         time.sleep(0.5)
        

def callback(direction, btn_pressed):
    global counter
    if direction == RotaryEncoder.DIRECTION_CLOCKWISE and not btn_pressed:
        buttons[counter].config(bg='blue')
        counter = (counter + 1) % 3 
        buttons[counter].config(bg='red')
        print('CLOCKWISE')
    elif direction == RotaryEncoder.DIRECTION_COUNTERCLOCKWISE and not btn_pressed:
        buttons[counter].config(bg='blue')
        counter = (counter - 1) % 3
        buttons[counter].config(bg='red')
        print('COUNTER CLOCKWISE')
    
def run_rotary():
    enc = RotaryEncoder(18, 16, 12, callback)
    print ("listening...")
    main_loop()
 
if __name__ == '__main__':
       
    root = Tk()
    button1 = Button(root, text = "Button 1", bg = 'blue')
    button2 = Button(root, text = "Button 2", bg = 'blue')
    button3 = Button(root, text = "Button 3", bg = 'blue')

    buttons = {0: button1, 1: button2, 2: button3}
    
    button1.grid(row = 0,column = 0)
    button2.grid(row = 0,column = 1)
    button3.grid(row = 0,column = 2)

    threading.Thread(target = run_rotary).start()

    root.mainloop() 
    print >> sys.stderr, '\nExiting by user request.\n'
    GPIO.cleanup()
    sys.exit(0)
