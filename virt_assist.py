import speech_recognition as sp_rec
import pyttsx3
import os, sys, time



recog = sp_rec.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def getText():
    try:
        with sp_rec.Microphone() as source:
            print('Slucham...', end='\r')
            audio = recog.listen(source)
            text = recog.recognize_google(audio, language="en-EN")
            if text == "":
                return print("no dalej")
            else:
                return text
    except:
        return None

def czy_zawiera(string, words):
    #for element in slowa:
        #if element in string.lower():
            #lista.append(element)
    #return lista
    return [element for element in words if element in string.lower()]

ACTIVATE = ["robot speak", 'bot']
BYE = ['gold', 'bye', 'goodbye', 'Hello World']
SEARCHING = ['search', 'look for', 'computer']

def main():
    print("Aby wyjsc powiedz Bye")
    while True:
        time.sleep(0.5)
        current_word = getText()
        print("      ??? "*10, end="\r")
        if current_word != None:
            print(current_word)
            if len(czy_zawiera(current_word, ACTIVATE)):
                print("hej hej hej     "*20)
                print(current_word)
                if len(czy_zawiera(current_word, BYE)):
                    speak("Bye bye, I will always love you")
                    break
                elif len(czy_zawiera(current_word, SEARCHING)):
                    print("no co chcesz wyszukac???")
                    print(current_word)
                    speak("What do you want to search for?")
                    break

if __name__ == '__main__':
    main()
