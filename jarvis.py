import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):  # This function will pronounce the string which is passed to it
    engine.say(audio)
    engine.runAndWait()

def wishMe():  # This function will wish the user according to the time
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How may I help you?")

def takeCommand():  # This function will take the command from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"  # None string will be returned
    return query

if __name__ == "__main__":
    wishMe()
    speak("I can perform day to day life activities feel free to ask me anything")