# pip install pyttsx3, gtts
import pyttsx3

app = pyttsx3.init()
voices = app.getProperty('voices')

print('Available Voices:')
for i in range(len(voices)):
    print(f'{i + 1}. {voices[i].name}')


def speak(voice, text):
    app.setProperty('voice', voices[voice - 1].id)
    app.say(text)
    app.runAndWait()


voice, text = int(input('Enter the voice number: ')), input('Enter text: ')

while text != '0':
    speak(voice, text)
    text = input('Enter text: ')
1