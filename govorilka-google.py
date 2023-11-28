# pip install gtts pygame
from gtts import gTTS
import pygame
from time import sleep

print('Введіть текст:')
text = open(0, encoding='utf8').read()
print(text)
voice = gTTS(text, lang='uk')

filename = 'voice.wav'
voice.save(filename)

pygame.init()
sound = pygame.mixer.Sound(filename)
duration_seconds = sound.get_length()

sound.play()
sleep(duration_seconds)
