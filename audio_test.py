# Thank you stack overflow: https://stackoverflow.com/questions/43758408/how-to-play-a-sound-using-pygame-in-all-operating-system

from pygame import mixer
mixer.pre_init(44100, -16, 2, 2048)
mixer.init()

masego = mixer.Sound('audio/masego-in-style.wav')

def play_masego():
    masego.play()
    print('Playing Masego!!')

while True:
    inpt = input('Press enter to play:')
    play_masego()