# import and set up GPIO and time packages
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN) # pin 11 input
GPIO.setup(13, GPIO.IN) # pin 13 input
GPIO.setup(15, GPIO.IN) # pin 15 input

# import and set up pygame audio
from pygame import mixer
mixer.pre_init(44100, -16, 2, 2048)
mixer.init()

# set audio channels
# acapella = mixer.Channel(0)
# melody = mixer.Channel(1)
# beat = mixer.Channel(2)

# set audio files
in_style = {
    'acapella': mixer.Sound('audio/masego-in-style/in_style-acapella.ogg'),
    'melody': mixer.Sound('audio/masego-in-style/in_style-melody.ogg'),
    'beat': mixer.Sound('audio/masego-in-style/in_style-beat.ogg')
    }

in_style['acapella'].set_volume(0)
in_style['melody'].set_volume(0)
in_style['beat'].set_volume(0)

try:
    while True: # program loop
        in_style['acapella'].play()
        in_style['melody'].play()
        in_style['beat'].play()
        if GPIO.input(11):
            if in_style['acapella'].get_volume() > 0:
                in_style['acapella'].set_volume(0)
            else: 
                in_style['acapella'].set_volume(0.5)
            sleep(0.2)
        elif GPIO.input(13):
            if in_style['melody'].get_volume() > 0:
                in_style['melody'].set_volume(0)
            else: 
                in_style['melody'].set_volume(0.5)
            sleep(0.2)
        elif GPIO.input(15):
            if in_style['beat'].get_volume() > 0:
                in_style['beat'].set_volume(0)
            else: 
                in_style['beat'].set_volume(0.5)
            sleep(0.2)
        
finally:
    GPIO.cleanup()

# def play_masego():
#     masego.play()
#     print('Playing Masego!!')

# while True:
#     inpt = input('Press enter to play:')
#     play_masego()
