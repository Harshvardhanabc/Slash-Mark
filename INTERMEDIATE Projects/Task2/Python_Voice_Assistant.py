import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import psutil
import pyautogui
import time
from keyboard import press

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

def open():
    pyautogui.press("win")
    time.sleep(.5)
    pyautogui.write(query)
    time.sleep(.5)
    pyautogui.press("enter")

def close():
    pyautogui.keyDown("alt")
    pyautogui.hotkey("f4")
    pyautogui.keyUp("alt")

def write():
    pyautogui.write(query)

def save():
    pyautogui.keyDown("ctrl")
    pyautogui.press("s")
    pyautogui.keyUp("ctrl")
    time.sleep(2)
    pyautogui.press("enter")


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
        return "None"
    return query

if __name__ == '__main__':
    speak("Slash Mark Assistant Activated")
    speak("How can i help you")
    while True:
        query = take_command().lower()
        if('wikipedia' in query):
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia",'')
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            speak(results)
        elif('hello' in query):
            speak("Hello Boss")
        elif("google" in query):
            speak("Ok sir, opening google")
            wb.open_new_tab("www.google.com")
        elif("youtube" in query):
            speak("Ok sir, opening youtube")
            wb.open_new_tab("www.youtube.com")
        elif("github" in query):
            speak("Ok sir, opening github")
            wb.open_new_tab("www.github.com")
        elif("stackoverflow" in query):
            speak("Ok sir, opeing stackoverflow")
            wb.open_new_tab("https://stackoverflow.com/")
        elif("spotify" in query):
            speak("Ok sir, opening spotify")
            wb.open_new_tab("https://open.spotify.com/")
        elif("whatsapp" in query):
            speak("Ok sir, opening whatsapp")
            wb.open_new_tab("https://web.whatsapp.com/")
        elif("play music" in query):
            speak("Ok sir, playing music")
            wb.open_new_tab("https://open.spotify.com/")
        elif("local disk d" in query):
            speak("ok sir opening local disk d")
            wb.open("D://")
        elif("local disk c" in query):
            speak("ok sir opening local disk c")
            wb.open("C://")
        elif("male" in query or "female" in query):
            if("female" in query):
                voice_change(1)
            elif("male" in query):
                voice_change(0)
        elif("close" in query):
            close()
        elif("type" in query):
            query = query.replace("type",'')
            write()
        elif("click" in query):
            press("enter")
        elif("open" in query):
            query = query.replace("open",'')
            open()
        elif("protect" in query,"save" in query):
            save()
        # close terminal
        elif('sleep' in query):
            exit(0)
        else:
            speak("I dont understand")

