import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia


engine = pyttsx3.init('sapi5')    #sapi5 =input the voice
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
    speak("i am jarvis sir,please tell me how may i help you")

def takeCommand():
    #it take microphone input from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
       # print(e)
       print("say that again please...")
       return "None"
    return query



if __name__=="__main__":
   wishMe()
   while True:
    query=takeCommand().lower()

    #logic for executing
    if 'wikipedia' in query:
        speak("searching wikipedia...")
        query=query.replace('wikipedia','')
        results=wikipedia.summary(query,sentences=1)
        speak("according to wikipedia")
        speak(results)
