# pip install gtts
from gtts import gTTS

text = input()
voice = gTTS(text)

voice.save('voice.mp3')
