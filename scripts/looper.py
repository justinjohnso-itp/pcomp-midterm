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

# plays each stem in an infinite loop so they all line up
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

# https://learn.adafruit.com/circuitpython-led-animations/overview
from adafruit_led_animation.helper import PixelSubset
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.group import AnimationGroup
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import *

pixels = neopixel.NeoPixel(board.D10, 144 + 49, brightness=1, auto_write=True)

star_2 = PixelSubset(pixels, 0, 6)
star_5 = PixelSubset(pixels, 7, 13)
star_7 = PixelSubset(pixels, 14, 20)
star_6 = PixelSubset(pixels, 21, 27)
star_3 = PixelSubset(pixels, 28, 34)
star_1 = PixelSubset(pixels, 35, 41)
star_4 = PixelSubset(pixels, 42, 48)

animations = AnimationSequence(
    AnimationGroup(
        Comet(star_1, speed=0.1045, color=BLUE, tail_length=13),
        Comet(star_2, speed=0.1045, color=BLUE, tail_length=13),
        Comet(star_3, speed=0.1045, color=AMBER, tail_length=13),
        Comet(star_4, speed=0.1045, color=AMBER, tail_length=13),
        Comet(star_5, speed=0.1045, color=AMBER, tail_length=13),
        Comet(star_6, speed=0.1045, color=RED, tail_length=13),
        Comet(star_7, speed=0.1045, color=RED, tail_length=13)
    )
)

try:
    while True : # program loop
        animations.animate()
    
        region_1 = not GPIO.input(4)
        region_2 = not GPIO.input(25)
        region_3 = not GPIO.input(24)
        region_4 = not GPIO.input(17)
        region_5 = not GPIO.input(23)
        region_6 = not GPIO.input(27)
        region_7 = not GPIO.input(22)
        
        # play music on sensor returning 1
        if region_1:
            monalisa['melody'].set_volume(.85)
        else:
            monalisa['melody'].set_volume(0)
            
        if region_2:
            one_two_step['melody'].set_volume(1)
        else:
            one_two_step['melody'].set_volume(0)
        
        if region_3:
            monalisa['acapella'].set_volume(.25)
        else:
            monalisa['acapella'].set_volume(0)
            
        if region_4:
            cant_stop['acapella'].set_volume(.45)
            
        else:
            cant_stop['acapella'].set_volume(0)
            
        if region_5:
            one_two_step['acapella'].set_volume(.75)
        else:
            one_two_step['acapella'].set_volume(0)
        
        if region_6:
            monalisa['beat'].set_volume(.65)
        else:
            monalisa['beat'].set_volume(0)
            
        if region_7:
            one_two_step['beat'].set_volume(.55)
        else:
            one_two_step['beat'].set_volume(0) 
        
finally:
    GPIO.cleanup()