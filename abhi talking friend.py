import pyttsx3
Aft = pyttsx3.init()

def Aft_speak(text):
    print('speaking....')
    Aft.say(text)
    Aft.runAndWait()

txt = ("Hello friend")
Aft_speak(txt)

while txt != 'bye':
    txt = input('what i have to say : ')
    if txt != 'bye':
        txt = txt.lower()
        Aft_speak(txt)
    else:
        Aft_speak("see you again,love you")












