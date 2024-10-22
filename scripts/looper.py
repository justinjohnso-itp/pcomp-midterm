# import and set up GPIO and time packages
import RPi.GPIO as GPIO
from time import sleep
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN) # GPIO 4 input
GPIO.setup(17, GPIO.IN) # GPIO 17 input
GPIO.setup(27, GPIO.IN) # GPIO 27 input
GPIO.setup(22, GPIO.IN) # GPIO 22 input
GPIO.setup(23, GPIO.IN) # GPIO 23 input
GPIO.setup(24, GPIO.IN) # GPIO 24 input
GPIO.setup(25, GPIO.IN) # GPIO 25 input

# import and set up pygame audio
from pygame import mixer
mixer.pre_init(44100, -16, 2, 2048)
mixer.init()

# init audio channels
# acapella = mixer.Channel(0)
# melody = mixer.Channel(1)
# beat = mixer.Channel(2)

# acapella.set_volume(1)
# melody.set_volume(1)
# beat.set_volume(1)

# init audio files
# in_style = {
#     'acapella': mixer.Sound('./audio/masego-in-style/in_style-acapella.ogg'),
#     'melody': mixer.Sound('./audio/masego-in-style/in_style-melody.ogg'),
#     'beat': mixer.Sound('./audio/masego-in-style/in_style-beat.ogg')
#     }
monalisa = {
    'acapella': mixer.Sound('./audio/monalisa-acapella.ogg'),
    'melody': mixer.Sound('./audio/monalisa-melody.ogg'),
    'beat': mixer.Sound('./audio/monalisa-beat.ogg')
    }

one_two_step = {
    'acapella': mixer.Sound('./audio/one_two_step-acapella.ogg'),
    'melody': mixer.Sound('./audio/one_two_step-melody.ogg'),
    'beat': mixer.Sound('./audio/one_two_step-beat.ogg')
    }

cant_stop = {
    'acapella': mixer.Sound('./audio/cant_stop-acapella.ogg')
    }

# acapella.play(griz['acapella'], -1)
# melody.play(griz['melody'], -1)
# beat.play(griz['beat'], -1)
# acapella.play(one_two_step['acapella'], -1)
# melody.play(one_two_step['melody'], -1)
# beat.play(one_two_step['beat'], -1)
# melody.play(rain_dance, -1)

monalisa['acapella'].play(-1)
monalisa['melody'].play(-1)
monalisa['beat'].play(-1)
one_two_step['acapella'].play(-1)
one_two_step['melody'].play(-1)
one_two_step['beat'].play(-1)
cant_stop['acapella'].play(-1)


# LIGHTING
import board
import neopixel

from adafruit_led_animation.helper import PixelSubset
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.group import AnimationGroup
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import *

pixels = neopixel.NeoPixel(board.D10, 144 + 49, brightness=1, auto_write=True)

star_1 = PixelSubset(pixels, 0, 6)
star_2 = PixelSubset(pixels, 7, 13)
star_3 = PixelSubset(pixels, 14, 20)
star_4 = PixelSubset(pixels, 21, 27)
star_5 = PixelSubset(pixels, 28, 34)
star_6 = PixelSubset(pixels, 35, 41)
star_7 = PixelSubset(pixels, 42, 48)
led_strip = PixelSubset(pixels, 49, 151)

# def idle_animation(target):
#     idle = AnimationSequence(
#         AnimationGroup(
#             Pulse(target, speed=0.1, color=PURPLE, period=4),
#         )
#     )
#     while True:
#         idle.animate()

# def play_animation(target):
#     play = AnimationSequence(
#         AnimationGroup(
#             Comet(target, speed=0.01, color=BLUE, tail_length=10),
#         )   
#     )
#     while True:
#         play.animate()

colors = [BLUE, RED, GREEN, PURPLE, ORANGE, AMBER]

animations = AnimationSequence(
    AnimationGroup(
        Comet(star_1, speed=0.01, color=random.choice(colors), tail_length=10),
        Comet(star_2, speed=0.01, color=random.choice(colors), tail_length=10),
        Comet(star_3, speed=0.01, color=random.choice(colors), tail_length=10),
        Comet(star_4, speed=0.01, color=random.choice(colors), tail_length=10),
        Comet(star_5, speed=0.01, color=random.choice(colors), tail_length=10),
        Comet(star_6, speed=0.01, color=random.choice(colors), tail_length=10),
        Comet(star_7, speed=0.01, color=random.choice(colors), tail_length=10),
        Comet(led_strip, speed=0.01, color=AMBER, tail_length=20),
        sync=True,
    )
)

try:
    while True : # program loop
        animations.animate()
        # program state
        # status = 'idle'
        # while status == 'idle':
        #     idle_animation.animate()
        # play_animation('idle')
        # set default state for each pin to 0
        region_1 = not GPIO.input(4)
        region_2 = not GPIO.input(17)
        region_3 = not GPIO.input(27)
        region_4 = not GPIO.input(22)
        region_5 = not GPIO.input(23)
        region_6 = not GPIO.input(24)
        region_7 = not GPIO.input(25)
        
        # play music on sensor returning 1
        if region_1:
            # print('r1')
            monalisa['acapella'].set_volume(.65)
        else:
            monalisa['acapella'].set_volume(0)
            
        if region_2:
            # print('r3')
            monalisa['melody'].set_volume(1)
        else:
            monalisa['melody'].set_volume(0)
        
        if region_3:
            # print('r3')
            monalisa['beat'].set_volume(1)
        else:
            monalisa['beat'].set_volume(0)
            
        if region_4:
            # print('r4')
            one_two_step['acapella'].set_volume(.75)
        else:
            one_two_step['acapella'].set_volume(0)
            
        if region_5:
            # print('r5')
            one_two_step['melody'].set_volume(.75)
        else:
            one_two_step['melody'].set_volume(0)
        
        if region_6:
            # print('r6')
            one_two_step['beat'].set_volume(1)
        else:
            one_two_step['beat'].set_volume(0)
            
        if region_7:
            # print('r7')
            cant_stop['acapella'].set_volume(.6)
        else:
            cant_stop['acapella'].set_volume(0) 
        
finally:
    GPIO.cleanup()