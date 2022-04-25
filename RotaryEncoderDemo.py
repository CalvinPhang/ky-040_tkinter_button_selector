import sys
import time
import RPi.GPIO as GPIO
from RotaryEncoder import RotaryEncoder

# (!) use BOARD NRs for PINs
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
counter = 0
LEDS = [11,13,15]

def main_loop():
    while True:
        time.sleep(0.5)

def callback(direction, btn_pressed):
	global counter
	if direction == RotaryEncoder.DIRECTION_CLOCKWISE and not btn_pressed:
		GPIO.output(LEDS[counter], GPIO.LOW)
		counter = (counter+1) % 3
		print('CLOCKWISE')
	elif direction == RotaryEncoder.DIRECTION_COUNTERCLOCKWISE and not btn_pressed:
		GPIO.output(LEDS[counter], GPIO.LOW)
		counter = (counter - 1) % 3
		print ('COUNTERCLOCKWISE')
	elif direction == RotaryEncoder.DIRECTION_CLOCKWISE and btn_pressed:
		print ('CLOCKWISE + BUTTON')
	elif direction == RotaryEncoder.DIRECTION_COUNTERCLOCKWISE and btn_pressed:
		print ('COUNTERCLOCKWISE + BUTTON')
	GPIO.output(LEDS[counter], GPIO.HIGH)
if __name__ == '__main__':
	try:
		enc = RotaryEncoder(18, 16, 12, callback)
		print ("listening...")
		main_loop()
	except KeyboardInterrupt:
		print >> sys.stderr, '\nExiting by user request.\n'
		GPIO.cleanup()
		sys.exit(0)
