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
engine.setProperty('voice', voices[1].id)

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
    speak("I am Nova. How may I help you?")

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

        elif 'open' in query:
            sites = [["youtube", "https://www.youtube.com"], ["google", "https://google.com"], ["github", "https://github.com"], ["stackoverflow", "https://stackoverflow.com"], ["gmail", "https://mail.google.com"], ["facebook", "https://www.facebook.com"], ["twitter", "https://twitter.com"], ["instagram", "https://www.instagram.com"], ["linkedin", "https://www.linkedin.com"], ["netflix", "https://www.netflix.com"], ["spotify", "https://www.spotify.com"], ["flipkart", "https://www.flipkart.com"], ["amazon", "https://www.amazon.com"], ["myntra", "https://www.myntra.com"], ["zomato", "https://www.zomato.com"], ["swiggy", "https://www.swiggy.com"], ["bird", "https://bard.google.com/chat"], ["dominos", "https://www.dominos.com"]]
            for site in sites:
                if f"open {site[0]}" in query:
                    speak(f"Opening {site[0]}...")
                    webbrowser.open(site[1])

        elif 'play music' in query:
            music_dir = 'C:\\Users\\harsh\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir, random_song))  # Playing the first song from the list

        elif 'hello nova' in query:
            speak("hello i am nova, your personal assistant, how may i help you?")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  # Converting the time into string format
            speak(f"The time is {strTime}")

        elif 'thank you nova' in query:
            speak("Thank you for using Nova, have a nice day!")
            exit()