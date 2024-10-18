import board
import neopixel

DATA_PIN = board.D10
pixel = neopixel.NeoPixel(DATA_PIN, ...)
# pixels = neopixel.NeoPixel(board.D10, 7)
# pixels[1] = (255, 0, 0)
# print(pixels)