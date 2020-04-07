import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from playsound import playsound



engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def  speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good afternoon sir!  ")

    else:
        speak("Good Evening sir!")

    speak("This is our Artificial intelligent project, please tell me hom may i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1

        audio = r.listen(source, phrase_time_limit = 5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

       
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'how are you doing' in query or 'hows going on' in query or 'how are you' in query:
            speak("oh! i am doing great and always ready to help you...")

        elif 'search' in query:
            speak('searching it...')
            query=query.replace("search","")
            if query=='search':
                continue
            webbrowser.open(query)
            speak("showing result from google")


        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open u m s' in query or 'login u m s' in query:
            webbrowser.open("https://ums.lpu.in/lpuums/")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")


        elif 'harish soni' in query:
            speak("Founder of silveradda.com")
        
        elif 'open silveradda' in query:
            webbrowser.open("https://silveradda.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
