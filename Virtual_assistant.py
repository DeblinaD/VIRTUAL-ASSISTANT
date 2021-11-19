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

def there_exists(terms, voice_data:str):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text=str(text)
    gTTS.say(text)
    gTTS.runAndWait()

r=sr.Recognizer() #initialize the voice recognizer

#now definition for audio to convert it to text format.
def record_audio(ask=""):
    with sr.Microphone() as source: #microphone as source
        if ask:
            engine_speak(ask)
        r.adjust_for_ambient_noise(source, duration = 1)
        audio= r.listen(source, timeout=20) #listen to audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data= r.recognize_google(audio) #convert audio to text
        except sr.UnknownValueError: #recognizer dosen't understand
            engine_speak("Sorry, your voice couldn't be understood")
            engine_speak("Sorry, can't be found. Please check your network") #network issue
            print(">>", voice_data.lower()) #print what user said
            # return voice_data.lower() 
        return voice_data.lower()

#get string and make audio file to be played
def engine_speak(audio_string):
    audio_string= str(audio_string)
    tts= gTTS(text=audio_string, lang = "en") #text to speech
    r= random.randint(1, 200000000)
    audio_file= 'audio' +str(r) + '.mp3' 
    tts.save(audio_file) #save as mp3
    playsound.playsound(audio_file) #help us to play the audio_string
    print(asis_obj.name+ ":", audio_string)
    os.remove(audio_file) #this is for deleting those audio files which we need not to use or save but are created at the time of usage 
    
first_time = True
#now this is our main function
def respond(voice_data):
    global first_time
    asis_name="Dumble"
    #greetings command, ie. when we say hi or hello, it will also respond to us.
    if there_exists(['hellow Dumble','hey Dumble', 'Hi Dumble', 'hellow', 'hi','hey'], voice_data):
        greetings=['Hi, how can I help you']
        engine_speak(greetings)

    if first_time:
        engine_speak("May I know your name please")
        if there_exists(["My name is"], voice_data):
            person_name=voice_data.split("is")[-1].strip()
            engine_speak("okay" + person_name())
            person_obj.setName(person_name)
        first_time = False

    #greetings
    if there_exists(["How are you", "How are you doing"],voice_data):
        engine_speak("I'm fine, thank you")

    #time
    if there_exists(["What's the time", "Please tell me the time"],voice_data):
        tym=time.ctime.split(" ")[3].split(":")[0:2]
        if tym[0]=='00':
            houres= '12'
        else:
            houres= tym[0]
            minutes= tym[1]
            tym= houres+"houres and" + minutes + "minutes"
            engine_speak(tym)

    #google search
    if there_exists(["search for", "play the video", "play the song"],voice_data) and 'youtube' not in voice_data:
        search_terms= voice_data.split("for")[-1]
        url= "https://google.com/search?q="+ search_terms
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_terms)

    #search youtube
    if there_exists(["youtube"],voice_data):
        search_terms = voice_data.split("for")[-1]
        url= "https://www.youtube.com/results?search_query="+ search_terms
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_terms + "on youtube")

    #get to know the stock price
    if there_exists(["price of"],voice_data):
        search_terms = voice_data.split("of")[-1]
        url= "https://google.com/search?q=" + search_terms
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_terms + "on google")

    #play music
    # if there_exists(["play music", "play the song", "play"],voice_data):
    #     search_terms = voice_data.split("play")[-1]
    #     url="https://open.spotify.com/search"+ search_terms
    #     webbrowser.get().open(url)
    #     engine_speak("You are listening to" + search_terms + "now enjoy")

    #search from amazon
    if there_exists(["amazon", "amazon.com", "online shopping"],voice_data):
        search_terms = voice_data.split("for")[-1]
        url="https://www.amazon.in/l/27269828031/?pf_rd_r=JEJSPJFS32YD7X1CYD78&pf_rd_p=5667f596-ebcf-4146-a49c-cf2bc9033422&pd_rd_r=727b9922-47fa-4808-8eb7-838bb42987ed&pd_rd_w=rkVUC&pd_rd_wg=cSLfz&ref_=pd_gw_unk" + search_terms
        webbrowser.get().open(url)
        engine_speak("I think I found what you were looking for" + search_terms +"on amazon.com")

    #search from flipkart
    if there_exists(["flipkart", "flipkart.com", "online shopping"], voice_data):
        search_terms = voice_data.split("for")[-1]
        url="https://www.flipkart.com/?ef_id=3e50925f1add1647992ff3c85bb9d51e:G:s&s_kwcid=AL!739!10!76347474199614!76347484024120&semcmpid=sem_F1167BY7_Brand_adcenter" + search_terms
        webbrowser.get().open(url)
        engine_speak("I think I found what you were looking for" + search_terms +"on flipkart.com")

    #search from myntra
    if there_exists(["myntra", "myntra.com", "online outfit shopping"], voice_data):
        search_terms = voice_data.split("for")[-1]
        url="https://www.myntra.com"
        webbrowser.get().open(url)
        engine_speak("I think I found what you were looking for" + search_terms +"on myntra.com")

    #make a note
    if there_exists(["make a note"],voice_data):
        search_terms = voice_data.split("for")[-1]
        url="https://keep.google.com/#home"
        webbrowser.get().open(url)
        engine_speak("Okay")

    #open instagram
    if there_exists(["open instagram", "insta", "social media", "ig"],voice_data):
        search_terms = voice_data.split("for")[-1]
        url="https://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("Enjoy")

    #open twitter
    if there_exists(["open twitter", "twitter"],voice_data):
        search_terms = voice_data.split("for")[-1]
        url="https://www.twitter.com/"
        webbrowser.get().open(url)
        engine_speak("Enjoy")
        
    #open facebook
    if there_exists(["open facebook", "facebook"],voice_data):
        search_terms = voice_data.split("for")[-1]
        url="https://www.facebook.com/"
        webbrowser.get().open(url)
        engine_speak("Enjoy")

    #open gmail
    if there_exists(["open gmail", "gmail", "mail", "email"],voice_data):
        search_terms = voice_data.split("for")[-1]
        url="https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        engine_speak("here is your email")

    #game(stone paper scisor)
    if there_exists(["game"],voice_data):
        voice_data = record_audio("chose among rock, paper or scissor")
        moves=["rock", "paper", "scissor"]
        cmove=random.choice(moves)
        pmove=voice_data
        # print(voice_data)
        engine_speak("Dumble choses"+ cmove)

        if pmove==cmove:
            engine_speak("Match draw")
        elif pmove=="rock" and cmove=="paper":
            engine_speak("Okay you win this time")
        elif pmove=="rock" and cmove=="scissor" or 's' in cmove :
            engine_speak("Dumble wins")
        elif pmove== "paper" and cmove=="scissors":
            engine_speak("YESSS Dumble wins")
        elif pmove=="paper" and cmove=="rock":
            engine_speak("Player wins")
        elif pmove=="scissors" and cmove=="Paper":
            engine_speak("Player wins")
        elif pmove=="scissors" and cmove=="rock":
            engine_speak("Dumble wins")
        else:
            engine_speak("I could not understand")

    #coin tossing
    if there_exists(["toss", "flip", "coin"],voice_data):
        moves=["head", "tail"]
        cmove=random.choice(moves)
        engine_speak("The computer chose" + cmove)

    #12 calc
    if there_exists(["plus", "minus", "multiply", "divide", "power", "+", "-", "*", "/"],voice_data):
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
    if there_exists(["capture", "screenshot", "snapshot"],voice_data):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('./screenshot.jpg')

    if there_exists(["exit", "quit", "bye", "goodbye", "okay bye"],voice_data):
        engine_speak("I wish to talk to you more, but it seems that you are not willing to talk any more. So talk to you later")
        exit()

time.sleep(1)
asis_obj = assis()
person_obj=person()
asis_obj.name="Dumble"
engin = pyttsx3.init()

while(1):
    voice_data=record_audio("Recording") #get the voice input
    print("Done")
    print("Q: ", voice_data)
    respond(voice_data)
