import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import psutil
import pyautogui
import time

# Set Voice properties using pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)

# Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Voice change function to Male or Female and vice-versa
def voice_change(v):
    x = int(v)
    engine.setProperty('voice',voices[x].id)
    speak("done sir")

# Take command Function using speech_recognition
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: "+query+"\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query

if __name__ == '__main__':
    speak("Slash Mark Assistant Activated")
    speak("How can i help you")
    while True:
        query = take_command().lower()
        if("hello" in query):
            speak("Hello")
        elif("open google" in query):
            speak("Ok sir, opening google")
            wb.open_new_tab("www.google.com")
        else:
            speak("I dont understand")
