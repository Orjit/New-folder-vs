import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('heyy! I am here ')
engine.say('How can I help you ')
engine.runAndWait()
try:
    with sr.Microphone() as source:
        print('tell me sir...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            print(command)
except:
    pass        
