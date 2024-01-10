import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

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

def takeCommand():  # This function will take the command from the microphone(user) and return the string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
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
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")  # Removing the word wikipedia from the query
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube...")
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("google.com")

        elif 'open github' in query:
            speak("Opening GitHub...")
            webbrowser.open("github.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\harsh\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir, random_song))  # Playing the first song from the list

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  # Converting the time into string format
            speak(f"The time is {strTime}")

        elif 'quit' in query:
            speak("Quitting... Thank you for using Jarvis, have a nice day!")
            exit()