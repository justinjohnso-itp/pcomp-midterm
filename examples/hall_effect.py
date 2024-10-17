# import and set up GPIO and time packages
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN) # pin 11 input
GPIO.setup(13, GPIO.IN) # pin 13 input
GPIO.setup(15, GPIO.IN) # pin 15 input

while True:
  print(GPIO.input(11))