import speech_recognition as sr #to recognize speech_recognition
import playsound #to play sound file
import random
from gtts import gTTS #google text to speech
import webbrowser #to open browser
import ssl
import certifi
import time
import os #remove audio files
import subprocess
from PIL import Image
import pyautogui #screenshot
import pyttsx3
import bs4 as bs
import urllib.request

class person:
    name=''
    def setName(self, name):
        self.name=name

class assis:
    name=''
    def setName(self, name):
        self.name=name

def there_exists(terms):
    for term in terms:
        if term in value_data:
            return True

def engine_speak(text):
    text=str(text)
    engine.say(text)
    engine.runAndWait()

r=sr.Recognizer() #initialize the voice recognizer

#now definition for audio to convert it to text format.
def record_audio(ask=""):
    with sr.Microphone() as source: #microphone as source
        if ask:
            engine_speak(ask)
        audio= r.listen(source, 5,5) #listen to audio via source
        print("Done Listening")
        voice_data=""
        try:
            voice_data= r.recognize_google(audio) #convert audio to text
        except sr.UnknownValueError: #recognizer dosen't understand
            engine_speak("Sorry, your voice couldn't be understood")
        except sr.UnknownValueError:
            engine_speak("Sorry, can't be found. Please check your network") #network issue
            print(">>", voice_data.lower()) #print what user said
            return voice_data.lower() 

#get string and make audio file to be played
def engine_speak(audio_string):
    audio_string= str(audio_string)
    tts= gTTS(text=audio_string, lang = "en") #text to speech
    r= random.randint(1, 200000000)
    audio.file= 'audio' +str(r) + '.mp3' 
    tts.save(audio_file) #save as mp3
    playsound.playsound(audio_file) #help us to play the audio_string
    print(asis_obj.name+ ":", audio_string)
    os.remove(audio_file) #this is for deleting those audio files which we need not to use or save but are created at the time of usage 
    
#now this is our main function
def respond(voice_data):
    asis_name="Dumble"
    #greetings command, ie. when we say hi or hello, it will also respond to us.
    if there_exists(['hellow Dumble','hey Dumble', 'Hi Dumble', 'hellow', 'hi','hey']):
        greetings=['Hi, how can I help you?']
        engine_speak(greetings)

engine_speak("May I know your name please?")
if there_exists(["My name is"]):
    person_name=voice_data.split("is")[-1].strip()
    engine_speak("okay" + person_name())
    person_obj.setName(person_name)

#greetings
if there_exists(["How are you?", "How are you doing?"]):
    engine_speak("I'm fine, thank you")

#time
if there_exists(["What's the time?", "Please tell me the time"]):
    time=ctime.split(" ")[3].split(":")[0:2]
    if time[0]=='00':
        houres= '12'
    else:
        houres= time[0]
        minutes= time[1]
        time= houres+"houres and" + minutes + "minutes"
        engine_speak(time)

#google search
if there_exists(["search for", "play the video", "play the song"]) and 'youtube' not in voice_data:
    search_terms= voice_data.split("for")[-1]
    url= "https://google.com/search?q"+ search_term
    webbrowser.get().open(url)
    engine_speak("Here is what I found for" + search_terms + "on google")

#search youtube
if there_exists(["youtube"]):
    search_term = voice_data.split("for")[-1]
    url= "https://www.youtube.com/results?search_query="+search_term
    webbrowser.get().open(url)
    engine_speak("Here is what I found for" + search_terms + "on youtube")

#get to know the stock price
if there_exists(["price of"]):
    search_term = voice_data.split("of")[-1]
    url= "https://google.com/search?q" + search_term
    webbrowser.get().open(url)
    engine_speak("Here is what I found for" + search_terms + "on google")

#play music
if there_exists(["play music", "play the song", "play"]):
    search_term = voice_data.split("play")[-1]
    url="https://open.spotify.com/search"+ search_term
    webbrowser.get().open(url)
    engine_speak("You are listening to" + search_term + "now enjoy!!")

#search from amazon
if there_exists(["amazon", "amazon.com", "online shopping"]):
    search_term = voice_data.split("for")[-1]
    url="https://www.amazon.in" + search_term
    webbrowser.get().open(url)
    engine_speak("I think I found what you were looking for" + search_term +"on amazon.com")

#search from flipkart
if there_exists(["flipkart", "flipkart.com", "online shopping"]):
    search_term = voice_data.split("for")[-1]
    url="https://www.flipkart.com" + search_term
    webbrowser.get().open(url)
    engine_speak("I think I found what you were looking for" + search_term +"on flipkart.com")

#search from myntra
if there_exists(["myntra", "myntra.com", "online outfit shopping"]):
    search_term = voice_data.split("for")[-1]
    url="https://www.myntra.com" + search_term
    webbrowser.get().open(url)
    engine_speak("I think I found what you were looking for" + search_term +"on myntra.com")

#make a note
if there_exists(["make a note"]):
    search_term = voice_data.split("for")[-1]
    url="https://keep.google.com/#home"
    webbrowser.get().open(url)
    engine_speak("Okay")

#open instagram
if there_exists(["open instagram", "insta", "social media", "ig"]):
    search_term = voice_data.split("for")[-1]
    url="https://www.instagram.com/"
    webbrowser.get().open(url)
    engine_speak("Enjoy")

#open twitter
if there_exists(["open twitter", "twitter"]):
    search_term = voice_data.split("for")[-1]
    url="https://www.twitter.com/"
    webbrowser.get().open(url)
    engine_speak("Enjoy")
    
#open facebook
if there_exists(["open facebook", "facebook"]):
    search_term = voice_data.split("for")[-1]
    url="https://www.facebook.com/"
    webbrowser.get().open(url)
    engine_speak("Enjoy")

#open gmail
if there_exists(["open gmail", "gmail", "mail", "email"]):
    search_term = voice_data.split("for")[-1]
    url="https://mail.google.com/mail/u/0/#inbox"
    webbrowser.get().open(url)
    engine_speak("here is your email")

#game(stone paper scisor)
if there_exists(["game"]):
    voice_data = record_audio("chose among rock, paper or scissor")
    moves=["rock", "paper", "scissors"]
    cmove=random.choice(moves)
    pmove=voice_data
    engine_speak("Dumble choses"+ cmove)

    if pmove==cmove:
        engine_speak("Match draw")
    elif pmove=="rock" and cmove=="paper":
        engine_speak("Okay you win this time")
    elif pmove=="rock" and cmove=="scissor":
        engine_speak("Dumble wins")
    elif pmove== "paper" and cmove=="scissors":
        engine_speak("YESSS! Dumble wins")
    elif pmove=="paper" and cmove=="rock":
        engine_speak("Player wins")
    elif pmove=="scissors" and cmove=="Paper":
        engine_speak("Player wins")
    elif pmove=="scissors" and cmove=="rock":
        engine_speak("Dumble wins")

#coin tossing
if there_exists(["toss", "flip", "coin"]):
    moves=["head", "tail"]
    cmove=random.choice(moves)
    engine_speak("The computer chose" + cmove)

#12 calc
if there_exists(["plus", "minus", "multiply", "divide", "power", "+", "-", "*", "/"]):
    opr = voice_data.split()[1]

    if opr == '+':
        engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
    elif opr == '-':
        engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
    elif opr == 'multiply':
        engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
    elif opr == 'divide':
        engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
    elif opr == 'power':
        engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
    else:
        engine_speak("wrong operator")

#screenshot
if there_exists(["capture", "screenshot", "snapshot"]):
    myScreenshot = pyautogui.screenshot()
    myscreenshot.save('C:\Users\DEBLINA DAS\OneDrive\Desktop\INT213_CA1')

if there_exists(["exit", "quit", "bye", "goodbye"]):
    engine_speak("I wish to talk to you more, but........bye. talk to you later.")
    exit()

time.sleep(1)
asis_obj = asis()
person_obj=person()
asis_obj.name="Kim"
engin = pyttsx3.init()

while(1):
    voice_data=record_("Recording") #get the voice input
    print("Done")
    print("Q: ", voice_data)
    respond(voice_data)
