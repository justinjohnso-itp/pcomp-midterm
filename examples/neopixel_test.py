# init libraries
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


animations = AnimationSequence(
    AnimationGroup(
        Pulse(star_1, speed=0.05, color=PURPLE, period=2),
        Pulse(star_2, speed=0.05, color=PURPLE, period=2),
        Pulse(star_3, speed=0.05, color=PURPLE, period=2),
        Pulse(star_4, speed=0.05, color=PURPLE, period=2),
        Pulse(star_5, speed=0.05, color=PURPLE, period=2),
        Pulse(star_6, speed=0.05, color=PURPLE, period=2),
        Pulse(star_7, speed=0.05, color=PURPLE, period=2),
        Comet(led_strip, speed=0.01, color=AMBER, tail_length=20),
        sync=True,
    )
)

while True:
    animations.animate()