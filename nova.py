import operator
import pyttsx3
import requests  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime  # pip install datetime
import wikipedia  # pip install wikipedia
import webbrowser 
import os
import random  # pip install random
from requests import get
import pywhatkit as kit  # pip install pywhatkit
import pyjokes  # pip install pyjokes
from bs4 import BeautifulSoup  # pip install bs4


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):  # This function will pronounce the string which is passed to it
    engine.say(audio)
    engine.runAndWait()
    # rate = engine.getProperty('rate')   # getting details of current speaking rate
    # engine.setProperty('rate', rate-10) # setting up new voice rate

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
            sites = [["youtube", "https://www.youtube.com"], ["google", "https://google.com"], ["github", "https://github.com"], ["stackoverflow", "https://stackoverflow.com"], ["gmail", "https://mail.google.com"], ["facebook", "https://www.facebook.com"], ["twitter", "https://twitter.com"], ["instagram", "https://www.instagram.com"], ["linkedin", "https://www.linkedin.com"], ["netflix", "https://www.netflix.com"], ["spotify", "https://www.spotify.com"], ["flipkart", "https://www.flipkart.com"], ["amazon", "https://www.amazon.com"], ["myntra", "https://www.myntra.com"], ["zomato", "https://www.zomato.com"], ["college erp", "https://student.icampuserp.in/Login.aspx"], ["bird", "https://bard.google.com/chat"]]
            for site in sites:
                if f"open {site[0]}" in query:
                    speak(f"Opening {site[0]}...")
                    webbrowser.open(site[1])

        elif 'play music' in query or 'play song' in query:
            speak("playing music")
            music_dir = os.path.join(os.path.expanduser('~'), 'Music')
            songs = os.listdir(music_dir)
            # print(songs)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir, random_song))  # Playing the random song from the list

        elif 'hello nova' in query:
            speak("hello, i am nova, your personal assistant, how may i help you?")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  # Converting the time into string format
            speak(f"The time is {strTime}")

        elif 'open notepad' in query:
            speak("opening notepad")
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath) #NOT WORKING

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Address is {ip}")

        elif 'where am i' in query or 'location' in query:
            speak("Wait for a second, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"Currently We are in {city}, city of {country} country")
            except Exception as e:
                speak("Sorry, Due to network issue I am not able to find where we are.")
                pass

        elif 'temperature' in query:
            search = "temperature in prayaagraaj"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")
                
        elif 'play' in query and 'on youtube' in query:
            start = query.find('play') + len('play')
            end = query.find('song on youtube')
            song_name = query[start:end].strip()  # Extract the song name from the query
            speak(f"Playing {song_name} on YouTube")
            kit.playonyt(song_name)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'sleep system' in query:
            speak("Putting the system to sleep")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'love' in query:
            speak("I can't feel romantic love, but i think you are wonderful")

        elif 'hu r u' in query:
            speak("I am Nova, your personal assistant, i am here to make your life easier")

        elif 'how are you' in query or 'how r u' in query:
            speak("I am fine, Thank you for asking me, what about you? How are you?")

        elif 'i am fine' in query:
            speak("I am glad to hear that you are fine, how may i help you?")

        elif 'i am not fine' in query:
            speak("Don't worry, everything will be fine soon, just keep smiling and stay happy, ")

        elif 'who made you' in query or 'who created you' in query:
            speak("I was made by Harsh and Aayushi, student of computer science and engineering, they are my creators and i am very thankful to them for creating me")

        elif 'harsh' in query:
            speak("Harsh is my creator, he is a student of computer science and engineering at United College of Engineering and Research, Prayagraj.")

        elif 'ayushi' in query:
            speak("ayushi is my creator, she is a student of computer science and engineering at United College of Engineering and Research, Prayagraj.")

        elif 'what can you do' in query:
            speak("I can do many things, i can tell you the current time, i can tell you the current weather, i can tell you the current temperature, i can tell you the current location, i can tell you the current ip address, i can tell you a joke, i can play music for you, i can open any website for you, i can search anything on wikipedia for you, i can play anything on youtube for you, i can put your system to sleep, i can tell you about my creators, i can tell you about myself.")
            
        elif 'thank you' in query:
            speak("Thank you for using Nova, have a nice day!")
            exit()
        
        # speak("Sir, do you have any other work?")