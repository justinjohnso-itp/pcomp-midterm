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

pixels = neopixel.NeoPixel(board.D10, 144 + 7, brightness=0.1, auto_write=True)

led_strip = PixelSubset(pixels, 8, 151)
star = PixelSubset(pixels, 0, 7)

animations = AnimationSequence(
    AnimationGroup(
        Pulse(star, speed=0.05, color=PURPLE, period=2),
        Comet(led_strip, speed=0.01, color=AMBER, tail_length=20),
        sync=True,
    )
)

while True:
    animations.animate()