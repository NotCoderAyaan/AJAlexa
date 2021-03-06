import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from GoogleNews import GoogleNews

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except:
        pass
    return command

def run_AJAlexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.wikipedia.summary(person, 3)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

    elif 'owner of Alexa' in command:
        talk('Ayaan Jain is the owner of AJAlexa')

    elif 'Google' in command:
        import wikipedia as googleScrap
        command = command.replace('goole', '')
        command = command.replace('Alexa', '')
        command = command.replace('google search', '')
        talk('Sir here it is what you looking for ')
        pywhatkit.search(command)

        try:
            result = googleScrap.summary(command,3)
            talk(result)
            print(result)

        except:
            talk("You are on the page")

    else:
        print('SORRY SIR ITS NOT IN MY DICTIONARY I AM UPDATING DAY BY DAY')
        talk('SORRY SIR ITS NOT IN MY DICTIONARY I AM UPDATING DAY BY DAY')


run_AJAlexa()