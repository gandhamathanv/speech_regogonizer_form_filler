from gtts import gTTS
import speech_recognition as sr
import playsound
import os
mytext = "i am gokul"
lange = "en"
output = gTTS(text=mytext, lang=lange, slow=False)
output.save("output.mp3")
playsound.playsound("output.mp3")
r = sr.Recognizer()
t = r.recognize_google("output.mp3")
print(t)
