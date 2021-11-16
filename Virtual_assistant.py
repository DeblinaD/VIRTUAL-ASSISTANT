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
    