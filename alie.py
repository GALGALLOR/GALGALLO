import datetime

from pygame import *
import random
d = datetime.datetime
dob = d(year=2020,month=8,day=13)
t = datetime.datetime.now()
leo = t.year, t.month, t.day
sai = (t.hour, t.minute)
songsTogether=['y2mate.com - KSI – Cap (feat. Offset) [Official Music Video]_y8AOvb-Iy60.mp3','y2mate.com - KSI - Poppin (feat. Lil Pump & Smokepurpp) [Official Music Video]_xa0qshcRhDQ.mp3','y2mate.com - Nathan Dawe x KSI – Lighter [Official Video]_Di0nAk2_Tpw.mp3','thewaylifegoes.mp3' ,'y2mate.com - Garfield - I feel good_J0_VUJdzHos.mp3','y2mate.com - Cardi B - WAP feat. Megan Thee Stallion [Official Audio]_Wc5IbN4xw70.mp3',"y2mate.com - Cochise - Hatchback (Lyrics) - in tokyo i'm with my ghouls_7Y5Mya_uSHk.mp3","y2mate.com - Fetty Wap  - Trap Queen (Official Video) Prod. By Tony Fadd_i_kF4zLNKio.mp3","y2mate.com - Fetty Wap 679 feat. Remy Boyz [Official Video]_Pzz4Z-O7710.mp3"]
song=random.choice(songsTogether)
import speech_recognition as sr
r = sr.Recognizer()






while 1==1:
    with sr.Microphone() as mic:
        try:
            print('say sth')
            audio = r.listen(mic)
            x = r.recognize_google(audio)
            print(x)
        except:
            print('try again')

    if x ==('stop') :
        mixer.init()
        mixer.music.load('bye.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(5)
        break

    if ('quiet') in x:
        print('ok')

    if ('your name')  in x:
        print('my name is JAMES ')
        mixer.init()
        mixer.music.load('name.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(5)
        mixer.init()
        mixer.music.load('yourname.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(5)
        with sr.Microphone() as mic:
            try:
                print('and your name is =')
                audio = r.listen(mic)
                yourname = r.recognize_google(audio)
            except:
                mixer.init()
                mixer.music.load('understand.mp3')
                mixer.music.play()
                while mixer.music.get_busy():
                    time.Clock().tick(5)
        if 'gal' in yourname:
            print('Hey Boss')
            mixer.init()
            mixer.music.load('hey boss.mp3')
            mixer.music.play()
            while mixer.music.get_busy():
                time.Clock().tick(5)
        else:
            print('Hey',yourname)
            mixer.init()
            mixer.music.load('hey.mp3')
            mixer.music.play()
            while mixer.music.get_busy():
                time.Clock().tick(5)


    if ('time') in x:
        mixer.init()
        mixer.music.load('text.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(5)
        print(sai)
 
        if sai >(7, 0) <(19,0):
            print('Day ☀')
        elif sai <(7,0) >(19,0):
            print('Good night ☽')
    if ('day' or 'date') in x:
        print(t.day , t.strftime('%A'))


    if ('month') in x:
        print(t.strftime('%B'))
        mixer.init()
        mixer.music.load('text.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(5)
    if ('year') in x:
        print(t.year)
        mixer.init()
        mixer.music.load('text.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(5)
    if ('how old are you') in x:
        print('I am', t-dob, 'old')
        mixer.init()
        mixer.music.load('text.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(5)

        mixer.init()
        mixer.music.load('yourage.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(5)
        yourage=int(input('you are of age='))
        if yourage>=10:
            print('you are so young')
        if yourage>10 <15:
            print('wait till you enter puberty  |^_^| ')
        if yourage>15<30:
            print('youre getting old mate!', yourage)
        if yourage>30:
            print('Hey sir/madam')



    if ('how') and ('feel') in x:
        mixer.init()
        mixer.music.load('C:/Users/galga/Downloads/y2mate.com - Garfield - I feel good_J0_VUJdzHos.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(5)
        print('I am doing great...as an AI if you say|^_^|')

        mixer.init()
        mixer.music.load('howaboutyou.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(5)
        feeling = input('how are you feeling')
        if 'good' in feeling:
            print('Good to hear')
            mixer.init()
            mixer.music.load('ok.mp3')
            mixer.music.play()
            while mixer.music.get_busy():
                time.Clock().tick(5)
        if 'bad' in feeling:
            print('why')
            mixer.init()
            mixer.music.load('understand.mp3')
            mixer.music.play()
            while mixer.music.get_busy():
                time.Clock().tick(5)
            understand=input('wanna listen to some music to brighten your mood?')
            if 'yes' in understand:
                mixer.init()
                mixer.music.load(song)
                mixer.music.play()
                while mixer.music.get_busy():
                    time.Clock().tick(5)
            if 'no' in understand:
                break

    if 'song' in x:
        mixer.init()
        mixer.music.load(song)
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(5)
    if ('you' or 'wanna')  and ('joke') in x:

        mixer.init()
        mixer.music.load('ok.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(5)

        joke=input('say the joke')
        if 'what' in joke:
            mixer.init()
            mixer.music.load('haha.mp3')
            mixer.music.play()
            while mixer.music.get_busy():
                time.Clock().tick(5)

        else:
            mixer.init()
            mixer.music.load('C:/Users/galga/Downloads/bad (online-audio-converter.com).mp3')
            mixer.music.play()
            while mixer.music.get_busy():
                time.Clock().tick(5)

    if ('tell me something') in x:
        print('ok')
        mixer.init()
        mixer.music.load('brothers.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(5)

            #print out good and bad or interesting

    if ('tell me a fact') in x:
        print('why was 6 afraid of 7?')
        print('because 7 8(ate) 9 ')
        mixer.init()
        mixer.music.load('lonely.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(5)
        lonely=input('are  you lonely?')
        if 'yes' in lonely:
            print('me too')
        elif 'yup' in lonely:
            print('me too')
        else:
            print('ok')
            mixer.init()
            mixer.music.load('ok.mp3')
            mixer.music.play()
            while mixer.music.get_busy():
                time.Clock().tick(5)



    if ('wanna hear a fact') in x:
        print('ok')
        mixer.init()
        mixer.music.load('ok.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(5)

        fact=input('tell me your fact = ')
        if 'did you know' in fact:
            mixer.init()
            mixer.music.load('wow.mp3')
            mixer.music.play()
            while mixer.music.get_busy():
                time.Clock().tick(5)
            print('wooooooow')
        else:
            mixer.init()
            mixer.music.load('iKnowThat.mp3')
            mixer.music.play()
            while mixer.music.get_busy():
                time.Clock().tick(5)
            print('I already knew that')
    if ('he') in x:
        print('hi too')
        mixer.init()
        mixer.music.load('hey.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(5)

























        





















            


