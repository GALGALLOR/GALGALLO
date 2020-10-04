import speech_recognition as sr  # recognise speech
import playsound  # to play an audio file
from gtts import gTTS  # google text to speech
import random
import datetime  # get time details
import webbrowser  # open browser
import time
import re
import mysql.connector
import os  # to remove created audio files
from PIL import Image
import pyautogui
import bs4 as bs
import urllib.request
import requests
import pandas as pd




r = sr.Recognizer()  # initialise a recogniser


# listen for audio and convert it to text:

def record_audio():
    with sr.Microphone() as source:  # microphone as source
        audio = r.listen(source)  # listen for the audio via source
        print("Done Listening")
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text

            print(voice_data)
        except :  # error: recognizer does not understand
            record_audio()
        return  voice_data

# get string and make a audio file to be played
def aspeak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')  # text to speech(voice)
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # play the audio file
    print('ALIE' + ":", audio_string)  # print what app said
    os.remove(audio_file)  # remove audio file

print('what is your name')
names = input()
print('welcome '+names)
pattern = '[a-zA-Z]'
'''first_letter = names[0]
other_letters = names[1:]
first_letter = first_letter.upper()
other_letters  = other_letters.lower()
names = first_letter+other_letters'''
'''if len(names)<14:
    print('welcome '+ names)
else:
    print('ERROR! Your name is too long')
    exit()'''


class alie:
    def __init__(self,date_of_creation,age,time_of_creation):
        self.date_of_creation = date_of_creation
        self.age = age
        self.time_of_creation = time_of_creation

    def time_of_creation(self):
        hour = 10
        minute = 30
        ampm = 'pm'
        time_of_creation = str(hour) + ':' + str(minute) + ampm
        print(time_of_creation)

    def day_of_creation(self):
        month = 'September'
        date = 25
        year = 2020
        day_of_creation = str(date )+' '+ str(month )+','+ str(year)
        print('i was born on ' + day_of_creation)

    def age(self):
        month_of_creation = 9
        year_of_creation = 2020
        day_of_creation = 25
        hour_of_creation = 10
        minute_of_creation = 30
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year
        day = datetime.datetime.now().day
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute

        year_age = year-year_of_creation
        month_age = month-month_of_creation
        day_age = day-day_of_creation
        hour_age = hour-hour_of_creation
        minute_age = minute-minute_of_creation

        print('i am '+str(year_age)+' years old,'+str(month_age)+ ' months old , '+ str(day_age)+' days old '+'at ' + str(10)+':'+str(30)+'pm')


'''class human:
    def __init__(self, names, age):
        self.names = names
        self.age = age

    def age(self):
        f = open('aliebrain/' + names + '.xlsx', 'a')

        f = str(f)
        df = pd.read_excel('C:/Users/LENOVO/Desktop/programming/machine learning/alie/aliebrain/' + names + '.xlsx')

        if names in f:
            try:
                df = pd.read_excel(
                    'C:/Users/LENOVO/Desktop/programming/machine learning/alie/aliebrain/' + names + '.xlsx')
                print('yes I know your age...', names)
                age = df['age']

                for bla in age:
                    print('you are ' + str(bla) + ' years old')

                print('i hope i get to live that long')
            except:

                print(' no i dont know your age... tell me because i am listening ... ')
                age = input()
                df = pd.DataFrame(columns=['age'])
                for i in range(1):
                    df.loc[i] = [age]
                df.to_excel('C:/Users/LENOVO/Desktop/programming/machine learning/alie/aliebrain/' + names + '.xlsx',
                            sheet_name=names)
                df = pd.read_excel(
                    'C:/Users/LENOVO/Desktop/programming/machine learning/alie/aliebrain/' + names + '.xlsx',
                    sheet_name=names)

                print('now i know your age ', names)'''



def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

mydb =  mysql.connector.connect(
    host="localhost",
    user="root",
    password="GALGALLO10",
    db="aliebrain")
cursor = mydb.cursor()

def find_age():
    try:
        cursor.execute('SELECT age FROM user WHERE names = "' + names + '"')
        f = cursor.fetchall()
        print('i know your age ')
        for x in f:
            for i in x:
                pass
        print('you are ' + i + ' years old')

    except:
        print('no i dont know your age')
        print('state your age in years')
        age = print()
        cursor.execute('INSERT INTO user(names,age) VALUES(%s,%s)', (names, age))
        mydb.commit()
        print('now i know your age ')

def respond(voice_data):
    #your names
    if there_exists(['my name']):
        print('You are '+names)
    # 1: greeting
    if there_exists(['hey', 'hi', 'hello','sup',"what's up"]):
        greetings = ["hey, how can I help you" , "hey, what's up?" ,
                     "I'm listening" , "how can I help you?" ,
                     "hello"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        print(greet)

    # 2: name
    if there_exists(["your name"]):

        print("My name is alie")  # gets users name from voice input





    if there_exists(["your name should be"]):
        global asis_name
        asis_name = voice_data.split("be")[-1].strip()
        print('do you want that to be my name? yes or no')

        naming_poll = input()
        if 'yes' in naming_poll:
            print('that could be a really nice name . thanks')
        else:
            pass
    # 3: greeting
    if there_exists(["how are you", "how are you doing"]):
        print("I'm very well, thanks for asking " + names + 'how are you doing? ')
        how = input()

        def ikiwa(terms):
            for term in terms:
                if term in how:
                    return True
        if ikiwa(['good','fine','great','okay','ok']):
            print('nice to hear ')
        else:
            print('would you like to hear some music? ')
            song = input()
            if 'ye' in song:
                print('what genre of music or name would you like to hear? ')
                song = input()
                url = 'https://www.youtube.com/results?search_query'+song
                webbrowser.get().open(url)
            elif 'no' in song:
                pass
                print('i hope you end up feeling better ')

        ''' ASK THE PERSON ABOUT HOW THEY ARE DOING THEN PLAY THEM A SONG'''



    # 4: time
    if there_exists(["what's the time", "tell me the time", "what time is it", "what is the time"]):

        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        if hour > 12:
            hour = hour - 12
            print(str(hour) + ':' + str(minute) + ' PM')
        elif hour <= 12:
            print(str(hour) + ':' + str(minute) + ' AM')







    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        print("Here is what I found for" + search_term + "on google")

    if there_exists(["search"]) and 'youtube' not in voice_data:
        search_term = voice_data.replace("search", "")
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        print("Here is what I found for" + search_term + "on google")

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        search_term = search_term.replace("on youtube", "").replace("search", "")
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        print("Here is what I found for " + search_term + "on youtube")

    '''    # 7: get stock price
        if there_exists(["price of"]):
            search_term = voice_data.split("for")[-1]
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            print("Here is what I found for " + search_term + " on google")'''

    # 8 time table
    if there_exists(["show my time table"]):
        im = Image.open(r"D:\WhatsApp Image 2019-12-26 at 10.51.10 AM.jpeg")
        im.show()

    # 9 weather
    if there_exists(["weather"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        print("Here is what I found for on google")

    if there_exists(['game']):
        print('online or offline? ')
        x=input()
        if 'offline' in x:
            print('if you would like rock,paper,scissors game say any of the words')
        if 'online' in x:
            print('what game would you like? ')
            f = input()
            webbrowser.get().open('https://www.google.com/search?q='+f)
            print('click on the game that impresses you')

    # 10 rock paper scisorrs
    if there_exists(["rock",'paper','scissors']):
        print('welcome to the rock,paper,scissors game')
        while 1==1:
            print("choose among rock paper or scissor")
            voice_data = input()
            moves = ["rock", "paper", "scissor"]

            cmove = random.choice(moves)
            pmove = voice_data

            print("The computer chose " + cmove)
            print("You chose " + pmove)
            # print("hi")
            if pmove == cmove:
                print("the match is draw")
            elif pmove == "rock" and cmove == "scissor":
                print("Player wins")
            elif pmove == "rock" and cmove == "paper":
                print("Computer wins")
            elif pmove == "paper" and cmove == "rock":
                print("Player wins")
            elif pmove == "paper" and cmove == "scissor":
                print("Computer wins")
            elif pmove == "scissor" and cmove == "paper":
                print("Player wins")
            elif pmove == "scissor" and cmove == "rock":
                print("Computer wins")
            elif pmove =='exit':
                break
            elif pmove == 'break':
                break
            elif pmove == 'stop':
                break
    # 11 toss a coin
    if there_exists(["toss", "flip", "coin"]):
        moves = ["head", "tails"]
        cmove = random.choice(moves)
        print("The computer chose " + cmove)

    # 12 calc
    if there_exists(["plus", "minus", "multiply", "divide", "power", "+", "-", "*", "/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            print(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            print(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply' or 'x':
            print(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            print(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            print(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            print("Wrong Operator")

    # 13 screenshot
    if there_exists(["capture", "my screen", "screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('D:/screenshot/screen.png')

    # 14 to search wikipedia for definition
    if there_exists(["definition of",'define']):
        print("what do you need the definition of")
        definition = input()
        url = urllib.request.urlopen('https://en.wikipedia.org/wiki/' + definition)
        soup = bs.BeautifulSoup(url, 'lxml')
        definitions = []
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                print('im sorry i could not find that definition, please try a web search')
            elif definitions[1]:
                print('here is what i found ' + definitions[1])
            else:
                print('Here is what i found ' + definitions[2])
        else:
            print("im sorry i could not find the definition for " + definition)

    if there_exists(["exit", "quit", "bye"]):
        print("bye")
        exit()

    # Current city or region

        # Current location as per Google maps
    if there_exists(["what is my exact location",'where am i','location']):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        print("You must be somewhere near here, as per Google maps")

    if there_exists(['old are you','your age']):
        alie.age('')
        alie.day_of_creation('')
    if there_exists(['your birthday']):
        print('i was not born... but i was created on: ')
        alie.day_of_creation('')

    if there_exists(['when where you made','when where you created','when were you initiated']):
        alie.day_of_creation('')

    if there_exists(['do you know me','do you know about me']):
        try:

            cursor.execute('SELECT age FROM user WHERE names = "' + names + '"')
            f = cursor.fetchall()
            print('i know your age ')
            for x in f:
                for i in x:
                    pass
            print('you are ' + i + ' years old')

        except:
            print('no i do not know your age , state them in years... ')
            age = input()
            cursor.execute('INSERT INTO user(names,age) VALUES(%s,%s)', (names, age))
            mydb.commit()
            print('now i know your age ')

    if there_exists(['who made','who created','who initiated']):
        if 'alga' in names:
            print('you boss ')
        else:
            print('Galgallo... but i will keep his identity concealed... ')

    if there_exists(['what made','what created','who iniated']):
        print('I prefer who... come again')

    if there_exists(['How do you know']):
        print(' I learn... like right now i can tell that you have little information about machine learning')


    if there_exists(['music','song']):
        print('what music would you like ')
        search = input()
        webbrowser.get().open('https://www.youtube.com/results?search_query='+search)
        print('now it is up to you to choose')

    if there_exists(['download']):
        print('would you like to install music,applicaton or other? ')
        item  = input()
        if ('music' or 'song') in item:
            print('what music would you like to download ')
            x= input()
            webbrowser.get().open('https://www.y2mate.com/search/'+x)
        else:
            print('what would you like? ')
            x = input()
            webbrowser.get().open('https://www.google.com/search=?'+x)

    if there_exists(['what can you do','what do you do','what can you do for me']):
        x=list(['greet','i can remember your name and age','i can google for you some things','i can play you some music...','i can flip a coin with you ','i can play rock paper and scissors game with you','i can tell you where you are','i can search a place','i can tell you the time','i can calculate things for you','i can predict the weather'])
        for x in x:
            print(x)
    if there_exists(['old am i', 'old i am', 'my age']):
        try:
            cursor.execute('SELECT age FROM user WHERE names = "' + names + '"')
            f = cursor.fetchall()
            print('i know your age ')
            for x in f:
                for i in x:
                    pass
            print('you are ' + i + ' years old')

        except:
            print('no i do not know your age , state your age in years... ')
            age =input()
            cursor.execute('INSERT INTO user(names,age) VALUES(%s,%s)', (names, age))
            mydb.commit()
            print('now i know your age ')
time.sleep(1)



while (1):
    voice_data = input("im listening... ")  # get the voice input
    respond(voice_data)  # respond
    print(' ')
