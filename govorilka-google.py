from gtts import gTTS

text = input()
voice = gTTS(text, lang='uk')

voice.save('voice.mp3')
