import speech_recognition as sr

listener = sr.Recognizer()
va_name = 'Abhi'

try:
    with sr.Recognizer()as source:
        print('listening....')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if va_name in command:
            print(command)


except:
    print('Check your Microphone')

