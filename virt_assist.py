import speech_recognition as sp_rec
import pyttsx3 as tts
import os, sys, time



recog = sp_rec.Recognizer()
engine = tts.init()
engine.setProperty('voice', engine.getProperty('voices')[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def getText():
    try:
        with sp_rec.Microphone() as source:
            print('Slucham...', end='\r')
            audio = recog.listen(source)
            text = recog.recognize_google(audio, language="pl-PL")
            if text == "":
                return print("no dalej")
            else:
                return text
    except:
        return None

def czy_zawiera(string, slowa):
    #for element in slowa:
        #if element in string.lower():
            #lista.append(element)
    #return lista
    return [element for element in slowa if element in string.lower()]

WYKRYJ = ['bot', 'lol', 'robot']
DOWIDZENIA = ['gold', 'bye', 'goodbye', 'Hello World']
SZUKAJ = ['search', 'look for', 'computer']

print("Aby wyjsc powiedz Bye")
while True:
    time.sleep(0.5)
    cur = getText()
    print("???"*10, end="\r")
    if cur != None:
        if len(czy_zawiera(cur, WYKRYJ)):
            print("hej hej hej "*20)
            if len(czy_zawiera(cur, DOWIDZENIA)):
                speak("Bye bye, NO, I will alway love you")
                break
            elif len(czy_zawiera(cur, SZUKAJ)):
                print("no co chcesz wyszukac???")
                speak("What do you want to search for?")
                break
