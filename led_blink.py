# import the GPIO and time packages
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT) # pin 16 output

# loop 10 times, on/off for 1 second
for i in range(10):
    GPIO.output(16, True)
    time.sleep(.5)
    GPIO.output(16, False)
    time.sleep(.5)
GPIO.cleanup()