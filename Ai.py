from ast import main
from datetime import datetime
from email.mime import audio
from tokenize import Special
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
        
    else:
        speak("Good Evening Sir!")
        
    speak("I am Baymax,please tell me how may I help you")
     
def takeCommand():
    # takes input from microphone from the user and returns string output 
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en=in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query 

def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('gmail','pass')
    server.sendmail('gmail',to,content)
    server.close()
    

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
    # logic for executing tasks on query 
    
        if 'wikipedia' in query:
            speak("Searching Wikipedia..")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'play music' in query:
            music_dir = 'E:\\My Documents\\pendrive\\Musics'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0])) 
        
        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'send mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "gmail"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")