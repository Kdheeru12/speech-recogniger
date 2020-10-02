import pyttsx3
import speech_recognition as take
import wikipedia
import webbrowser
import datetime

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def say():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning dheeraj!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good night")
    speak("hamanth how can i help u")
def voice():
    voic = take.Recognizer()
    with take.Microphone() as source:
        print("listening....")
        voic.pause_threshold = 0.8
        voic.energy_threshold = 4000
        audio = voic.listen(source)
        print(audio)
    try :
        print("scaning")
        query = voic.recognize_google(audio,language='en-in')
        print(f"dheeraj u need: {query}\n")
        speak(query)
    except Exception as e:
        print("i am unable to listen say that again")
        return "None"
        print(e)
    return query
say()

while True:
    query =voice().lower()
    if "exit" in query:
        break
    elif "wikipedia" in query:
        print("searching in wikipedia")
        speak("searching in wikipedia")
        query.replace("wikipedia","")
        result = wikipedia.summary(query,sentences=4)
        print("according to wikipedia")
        speak("according to wikipedia")
        print(results)
        speak(results)
    elif 'youtube' in query:
        
        webbrowser.open("  youtube.com")
    elif "youtube" in query:
        webbrowser.open("youtube.com")
    elif "google" in query:
        webbrowser.open("google.com")
        speak('opening google')
        speak('if you want to quit say exit ')
    elif "netflix" in query:
        webbrowser.open("netflix.com")
    elif "time" in query:
        time = datetime.datetime.now().time("%H:%M::%S")
        speak(f"dheeraj the time is {time}")
    elif "age" in query:
        speak("my age is 18")
    elif "whatsapp" in query:
        webbrowser.open("whatsapp.com")
    
    






    






