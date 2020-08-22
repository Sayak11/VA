# importing the pyttsx library 
import pyttsx3 
# importing date-time
import datetime
#importing speec-recognition
import speech_recognition as sr
#importing wikipedia
import wikipedia
#for email
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import subprocess


# initialisation 
engine = pyttsx3.init() 

# testing 

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() 
 
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date() :
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)

def wishme() :
    speak("Hey there , Welcome back !!")
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12 :
        speak("Good morning")
    elif hour>=12 and hour<18 :
        speak("Good afternoon")
    elif hour>=18 and hour<24 :
        speak("Good evening")
    else :
        speak("Good night")
    speak("Synonym at your service , please tell me how can i help you")
wishme()
def takeCommand() :
    r=sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening..")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e :
        print(e)
        speak("Say that again please")
        return "None"
    return query
def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sayakroychowdhury1398@gmail.com','sayaksrc11')
    server.sendmail('sayakroychowdhury1398@gmail.com', to,content)
    server.close()

def screenshot() :
    img=pyautogui.screenshot()
    img.save("D:\\Recommender system\\screen.png")

   

   
    
    


if __name__ == "__main__":
   
    while True :
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'calculator' in query :
            speak("Opening Calculator")
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        elif 'control panel' in query :
           speak("Opening control panel")
           subprocess.Popen('C:\\Windows\\System32\\control') 
            
        elif 'open' and 'google chrome' in query :
           speak("Opening google chrome")
           subprocess.Popen('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome')
      
            
        elif 'date' in query :
            date()
        elif 'wikipedia' in query :
            print("Searching")
            query = query.replace("wikipedia"," ")
            result = wikipedia.summary(query , sentences=2)
            print(result)
            speak(result)
        elif 'send' and 'email' in query :
            try :
                   speak("What should I send ?")
                   content = takeCommand()
                   to = 'sirsha.cse@gmail.com'
                   sendEmail(to,content)
                   speak("Email has been successfully sent!!")
            except Exception as e :
                    print(e)
                    speak("Unable to send the email")
        elif  'search' and 'chrome' and 'in' in query:
            speak("What should I search ?")
            urL='https://www.google.com'
            chromepath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome"
            search=takeCommand().lower()
            wb.register('chrome', None,wb.BackgroundBrowser(chromepath))
            wb.get('chrome').open_new_tab(search+'.com')
        
        elif  'remember' in query:
            speak("What should I remember ?")
            data=takeCommand()
            speak("You asked me to remember"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        elif  'remember' and 'asked' and 'you'and 'what' in query:
            remember=open('data.txt','r')
            speak("You asked me to remember"+remember.read())
        elif 'screenshot' in query :
            screenshot()
            speak("Screenshot taken")           
        elif 'bye' or 'exit' in query :
            quit()








