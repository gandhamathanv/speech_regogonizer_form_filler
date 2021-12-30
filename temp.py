import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import calendar

re = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)

meet = {"english meet": "https://meet.google.com/lookup/dzswe5fllg",
        "maths meet": "https://meet.google.com/lookup/euwmcjblbi",
        "physics meet": "https://meet.google.com/lookup/h4jxvmtiyi",
        "EP meet": "",
        }


def todaymeet():
    now = datetime.datetime.now()

    def findDay(date):
        born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
        return (calendar.day_name[born])

    date = now.strftime("%d %m %Y")
    day = findDay(date)
    print(day)
    todaydate = now.strftime("%H.%M")
    todaydate = float(todaydate)
    print(todaydate)
    Monday = {8.55: "physics meet", 9.55: "chemistry meet", 11.10: "EP meet", 12.10: "EP meet", 14.10: "maths meet",
              15: " "}
    Tuesday = {8.55: "drawing meet", 9.55: "maths meet",
               11.10: "plds meet", 12.10: " ", 14.10: " ", 15: " "}
    Wednesday = {8.55: "maths meet", 9.55: "english meet", 11.10: "physics meet", 12.10: "drawing meet",
                 14.10: "drawing meet", 15: " "}
    Thursday = {8.55: "chemistry meet", 9.55: "physics meet", 11.10: "maths meet", 12.10: "english meet",
                14.10: "plds meet", 15.10: " "}
    Friday = {8.55: "english meet", 9.55: "chemistry meet", 11.10: "drawing meet", 12.10: "plds meet",
              14.10: "plds meet", 15: " "}
    Saturday = {8.55: "plds meet", 9.55: "maths meet", 11.10: "chemistry meet", 12.10: "english meet",
                14.10: "physics meet", 15: " "}

    if ("Monday" in day):
        time_list = []
        for key in Monday:
            time_list.append(key)

        for i in range(0, 5):
            if (todaydate >= time_list[i]) and (todaydate < time_list[i + 1]):
                period = Monday[time_list[i]]

    elif ("Tuesday" in day):
        time_list = []
        for key in Tuesday:
            time_list.append(key)

        for i in range(0, 5):
            if (todaydate >= time_list[i]) and (todaydate < time_list[i + 1]):
                period = Tuesday[time_list[i]]

    elif ("Wednesday" in day):
        time_list = []
        for key in Wednesday:
            time_list.append(key)

        for i in range(0, 5):
            if (todaydate >= time_list[i]) and (todaydate < time_list[i + 1]):
                period = Wednesday[time_list[i]]

    elif ("Thursday" in day):
        time_list = []
        for key in Thursday:
            time_list.append(key)

        for i in range(0, 5):
            if (todaydate >= time_list[i]) and (todaydate < time_list[i + 1]):
                period = Thursday[time_list[i]]

    elif ("Friday" in day):
        time_list = []
        for key in Friday:
            time_list.append(key)

        for i in range(0, 5):
            if (todaydate >= time_list[i]) and (todaydate < time_list[i + 1]):
                period = Friday[time_list[i]]

    elif ("Saturday" in day):
        time_list = []
        for key in Saturday:
            time_list.append(key)

        for i in range(0, 5):
            if (todaydate >= time_list[i]) and (todaydate < time_list[i + 1]):
                period = Saturday[time_list[i]]

    print(period)
    if ("maths" in period) and ("meet" in period):
        pyttsx3.speak(
            "Its {} ,and Time is {} ... It's Maths period".format(day, todaydate))
        pyttsx3.speak("Opening Maths Meet....")
        webbrowser.open("https://meet.google.com/lookup/euwmcjblbi")

    if ("english" in period) and ("meet" in period):
        pyttsx3.speak(
            "Its {} ,and Time is {} ... It's English period".format(day, todaydate))
        pyttsx3.speak("Opening English Meet....")
        webbrowser.open("https://meet.google.com/lookup/dzswe5fllg")

    if ("physics" in period) and ("meet" in period):
        pyttsx3.speak(
            "Its {} ,and Time is {} ... It's Physics period".format(day, todaydate))
        pyttsx3.speak("Opening Physics Meet....")
        webbrowser.open("https://meet.google.com/lookup/h4jxvmtiyi")

    if ("plds" in period) and ("meet" in period):
        pyttsx3.speak(
            "Its {} ,and Time is {} ... It's PLDS period".format(day, todaydate))
        pyttsx3.speak("Opening P L D S Meet....")
        webbrowser.open("https://meet.google.com/lookup/heg3isf7rw")

    if ("drawing" in period) and ("meet" in period):
        pyttsx3.speak(
            "Its {} ,and Time is {} ... It's Engineering Drawing period".format(day, todaydate))
        pyttsx3.speak("Opening Engineering Drawing Meet")
        webbrowser.open("https://meet.google.com/lookup/furdt3el5r")

    if ("chemistry" in period) and ("meet" in period):
        pyttsx3.speak(
            "Its {} ,and Time is {} ... It's Chemistry period".format(day, todaydate))
        pyttsx3.speak("Opening Chemistry meet")
        webbrowser.open("https://meet.google.com/lookup/dn2ecj5pel")

    if ("EP" in period) and ("meet" in period):
        pyttsx3.speak(
            "Its {} ,and Time is {} ... It's EP period".format(day, todaydate))
        pyttsx3.speak("Opening EP lab...")
        webbrowser.open("https://meet.google.com/lookup/d6vchdea3w")


with sr.Microphone() as source:
    pyttsx3.speak("Hi Gokul!, What Can I do For U")
    print("listening....")

    message = re.record(source, duration=3)
i = re.recognize_google(message, language='en-US')

if ("mathematics" in i):
    i = i.replace("mathematics", "maths")

if ("meat" in i):
    i = i.replace("meat", "meet")

if ("P6" in i):
    i = i.replace("P6", "physics")

if ("TP" in i):
    i = i.replace("TP", "ep")
print(i)

if ("PLDS" in i):
    i.replace("PLDS", "plds")

if ("EP" in i):
    i = i.replace("EP", "ep")

if ("today" in i) or ("Today" in i) and ("meet" in i):
    pyttsx3.speak("Finding Today's meet ......")
    todaymeet()
# meet
if ("maths" in i) and ("meet" in i):
    pyttsx3.speak("Opening Maths Meet....")
    webbrowser.open("https://meet.google.com/lookup/euwmcjblbi")

if ("english" in i) or ("English" in i) and ("meet" in i):
    pyttsx3.speak("Opening English Meet....")
    webbrowser.open("https://meet.google.com/lookup/dzswe5fllg")

if ("physics" in i) and ("meet" in i):
    pyttsx3.speak("Opening Physics Meet....")
    webbrowser.open("https://meet.google.com/lookup/h4jxvmtiyi")

if ("plds" in i) and ("meet" in i):
    pyttsx3.speak("Opening P L D S Meet....")
    webbrowser.open("https://meet.google.com/lookup/heg3isf7rw")

if ("drawing" in i) and ("meet" in i):
    pyttsx3.speak("Opening Engineering Drawing Meet")
    webbrowser.open("https://meet.google.com/lookup/furdt3el5r")

if ("chemistry" in i) and ("meet" in i):
    pyttsx3.speak("Opening Chemistry meet")
    webbrowser.open("https://meet.google.com/lookup/dn2ecj5pel")

if ("ep" in i) and ("lab" in i):
    pyttsx3.speak("Opening EP lab...")
    webbrowser.open("https://meet.google.com/lookup/d6vchdea3w")

if ("yoga" in i) and ("meet" in i):
    pyttsx3.speak("Opening Yoga Meet")
    webbrowser.open("https://meet.google.com/iyi-ehhv-mvv")

if ("yoga" in i) and ("stream" in i):
    pyttsx3.speak("Opening Yoga Stream")
    webbrowser.open(
        "https://stream.meet.google.com/stream/f25eecab-f4eb-49fa-b568-622e3207aa81")

# classroom


if ("maths" in i) and ("classroom" in i):
    pyttsx3.speak("Opening Maths Classroom....")
    webbrowser.open("https://classroom.google.com/u/1/c/MjMwNDA0MzE5NDU5")

if ("english" in i) or ("English" in i) and ("classroom" in i):
    pyttsx3.speak("Opening English Classroom....")
    webbrowser.open("https://classroom.google.com/u/1/c/MjMwNDM3NzEzNzIw")

if ("physics" in i) and ("classroom" in i):
    pyttsx3.speak("Opening Physics Classroom....")
    webbrowser.open("https://classroom.google.com/u/1/c/MjA3Njg2MDA5NTY0")

if ("plds" in i) and ("classroom" in i):
    pyttsx3.speak("Opening P L D S Classroom....")
    webbrowser.open("https://classroom.google.com/u/1/c/MjQ5MTI2OTkzNDE2")

if ("drawing" in i) and ("classroom" in i):
    pyttsx3.speak("Opening Engineering Drawing Classroom")
    webbrowser.open("https://classroom.google.com/u/1/c/MzA4NzA0ODkwODg4")

if ("chemistry" in i) and ("classroom" in i):
    pyttsx3.speak("Opening Chemistry Classroom")
    webbrowser.open("https://classroom.google.com/u/1/c/MjgwOTA5OTI2NTUz")

if ("ep" in i) and ("classroom" in i):
    pyttsx3.speak("Opening EP Classroom...")
    webbrowser.open("https://classroom.google.com/u/1/c/MjgwOTc2NzQzNjA0")
