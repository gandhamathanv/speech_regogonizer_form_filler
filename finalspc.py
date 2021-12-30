import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import time
# sr.energy_threshold = 300
r = sr.Recognizer()
r1 = sr.Recognizer()
r2 = sr.Recognizer()

pyttsx3.speak(
    "this is a form to get informations about your name and age ")
time.sleep(1)

with sr.Microphone() as source:
    try:
        pyttsx3.speak("what's your name")
        message = r.record(source, duration=3)
        Name = r.recognize_google(message, language="en-US")
        print(Name)
    except:
        Name = "Abhi"
        print("ERROR")

with sr.Microphone() as source:
    try:
        pyttsx3.speak("whats your age")
        message2 = r1.record(source, duration=3)
        Age = r1.recognize_google(message2, language="en-US")
        print(Age)
    except:
        print("ERROR")
        Age = "18"  # default

with sr.Microphone() as source:
    try:
        pyttsx3.speak("whats your gender")
        message3 = r2.record(source, duration=3)
        Gender = r2.recognize_google(message3, language="en-US")
        print(Gender)
    except:
        Gender = "male"  # default
        print("ERROR")
