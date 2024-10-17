# import and set up GPIO and time packages
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN) # pin 3 input
GPIO.setup(5, GPIO.IN) # pin 5 input
GPIO.setup(7, GPIO.IN) # pin 7 input
GPIO.setup(11, GPIO.IN) # pin 11 input
GPIO.setup(13, GPIO.IN) # pin 13 input
GPIO.setup(15, GPIO.IN) # pin 15 input
GPIO.setup(19, GPIO.IN) # pin 19 input

# import and set up pygame audio
from pygame import mixer
mixer.pre_init(44100, -16, 2, 2048)
mixer.init()

# init audio channels
acapella = mixer.Channel(0)
melody = mixer.Channel(1)
beat = mixer.Channel(2)

acapella.set_volume(1)
melody.set_volume(1)
beat.set_volume(1)

# init audio files
in_style = {
    'acapella': mixer.Sound('./audio/masego-in-style/in_style-acapella.ogg'),
    'melody': mixer.Sound('./audio/masego-in-style/in_style-melody.ogg'),
    'beat': mixer.Sound('./audio/masego-in-style/in_style-beat.ogg')
    }

acapella.play(in_style['acapella'], -1)
melody.play(in_style['melody'], -1)
beat.play(in_style['beat'], -1)

try:
    while True: # program loop
        # set default state for each pin to 0
        pin_11 = not GPIO.input(11)
        pin_13 = not GPIO.input(13)
        pin_15 = not GPIO.input(15)
        
        # play music on sensor returning 1
        if pin_11:
            in_style['acapella'].set_volume(1)
        else:
            in_style['acapella'].set_volume(0)
            
        if pin_13:
            in_style['melody'].set_volume(.75)
        else:
            in_style['melody'].set_volume(0)
        
        if pin_15:
            in_style['beat'].set_volume(.75)
        else:
            in_style['beat'].set_volume(0)
        
finally:
    GPIO.cleanup()