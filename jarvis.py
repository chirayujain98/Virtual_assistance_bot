# -*- coding: utf-8 -*-
"""
Created on Wed May 15 13:00:23 2019

@author: chirayu jain
"""

import pyttsx3
import datetime
engine  = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
import datetime
import pyaudio
import wikipedia
import webbrowser
import smtplib
import os
import speech_recognition as sr

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("Jarvis activated sir. Please tell me how may I help you")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en-id")
        print("User said :",query)
    except Exception as e:
        #print(e)
        print("Say that again please")
        
        return "None"
    return query
def sendEmail(to, content):
    server  = smtplib.SMTP("smtp.gmail.com",535)
    server.ehlo()
    server.starttls()
    server.login("chirayujain.cse20@jecrc.ac.in","ryanite@16")
    server.sendemail("chirayujain.cse20@jecrc.ac.in",to,content)
    server.close()
if __name__ == "__main__":
    wishme()
    i = 0
    while(i==0):
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia on your command..")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia")
            speak(results)
        elif 'how are you' in query:
            speak("I am fine sir..always up for your queries")
        elif 'youtube' in query:
            speak("Opening youtube on your command Cheeerayu Sir..")
            webbrowser.open("www.youtube.com")
        elif 'google' in query:
            speak("Opening google on your command Cheeerayu Sir..")
            webbrowser.open("www.google.com")
        elif 'stackoverflow' in query:
            speak("Opening stackoverflow on your command Cheeerayu sir..")
            webbrowser.open("www.stackoverflow.com")
        elif 'codechef' in query:
            speak("Opening codechef on your command cheeerayu sir..")
            webbrowser.open("www.codechef.com")
        elif 'codeforces' in query:
            speak("Opening  codeforces on your command Cheerayu Sir..")
            webbrowser.open("www.codeforces.com")
        elif 'geeksforgeeks' in query:
            speak("Opening geeksforgeeks on your command cheeerayu sir..")
            webbrowser.open("www.geeksforgeeks.org")
        elif 'time' in query:
            strtime  = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir the time is")
            speak(strtime)
        elif 'sublime' in query:
            speak("opening sublime on your command sir")
            codepath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codepath)
        elif 'email to gaurav' in query:
            try:
                speak('what should I say to gaurav sir?')
                content  = takeCommand()
                to = "gaurav.sahu34@gmail.com"
                sendEmail(to, content)
                speak('Sir your email has been sent sir')
            except Exception as e:
                print(e)
                speak("Sorry sir due to unavoidable reasons this email cannot be sent")
        elif 'exit' in query:
            speak("Thank you so much cheerayu sir.. Have a nice day")
            i= 1