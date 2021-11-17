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
    url= ""

    