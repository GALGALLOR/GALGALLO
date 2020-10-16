from selenium import webdriver
import pyautogui # for pressing keys off the website
from selenium.webdriver.common.keys import Keys #for pressing keys on the keyboard in chrome
import time # to bring delays in the code

#initialize the key codes for zoom
MATH ='782 191 0689'
MATH_PASS='123456'
MATH_LINK='https://zoom.us/j/7821910689?pwd=SU9LREV0UVpZWHZLWW5nMWNYdENDQT09'
MINE = '710 762 9261'
MY_LINK  = 'https://zoom.us/s/91027223074'
COMPUTER = '573 904 3667'
COMPUTER_PASS = '12345678'
COMPUTER_LINK='https://zoom.us/j/5739043667?pwd=Wm00b21PdWJxaXpLUUc5TzNyRHhLQT09'
KISWAHILI='9548478307'
KISWAHILI_PASS = '123456'
KISWAHILI_LINK='https://zoom.us/j/9548478307?pwd=TCtMSHJ2ZmRqdnU2MWtQUEc1Y1FWdz09'
ENGLISH='7563264376'
ENGLISH_PASS = '123456'
ENGLISH_LINK='https://zoom.us/j/7563264376?pwd=TFUrMlJwUXdKTlVvNmpVeUIxVHhFdz09'
BIOLOGY='6292489277'
BIOLOGY_PASS = '123456'
BIOLOGY_LINK='https://zoom.us/j/6292489277?pwd=MjNFWG81QmN3Q0FvN21NTkgraGU3QT09'
PHYSICS='9841406308'
PHYSICS_PASS='123456'
PHYSICS_LINK='https://zoom.us/j/9841406308?pwd=NXNQVmszWUFScGU1bkZtTTBoWDJQdz09'
CHEMISTRY='7651793624'
CHEMISTRY_PASS = '123456'
CHEMISTRY_LINK='https://zoom.us/j/7651793624?pwd=N1lFUmM0aUZ5anB5WitOMVk1TEFydz09'
HISTORY='9049924850'
HISTORY_PASS = '12345678'
HISTORY_LINK='https://zoom.us/j/9049924850?pwd=TWh5N0NwZUhFQkZMWjZvelNHdExUZz09'
PATH ="C:/Program Files/chromedriver.exe"
driver = webdriver.Chrome(PATH)

import datetime # to know the time so that the code can act
now = datetime.datetime.now()
from gtts  import gTTS
import random
import playsound
import os
def aspeak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')  # text to speech(voice)
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # play the audio file
    print('ALIE' + ":", audio_string)  # print what app said
    os.remove(audio_file)  # remove audio file

def login():
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    email = driver.find_element_by_xpath('//*[@id="identifierId"]')
    email.send_keys('ga.roba@lightacademy.ac.ke')
    email.send_keys(Keys.ENTER)
    time.sleep(10)
    password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password.send_keys('GALGALLO')
    password.send_keys(Keys.ENTER)
    time.sleep(10)
    sign_in = driver.find_element_by_xpath('//*[@id="navbar"]/ul[2]/li[5]/a')
    sign_in.click()

    time.sleep(3)
    email = driver.find_element_by_xpath('//*[@id="login"]/div/div[2]/div/div[4]/a[2]')
    email.click()

    time.sleep(5)
    joinx = driver.find_element_by_xpath('//*[@id="btnJoinMeeting"]')
    joinx.click()
    time.sleep(3)



firstlessonhour = int(input('what is the first lesson hour'))
firstlessonminute = int(input('what is the minute'))
day = input('what day is it')

hour_duration = firstlessonhour-now.hour
minute_duration= firstlessonminute-now.minute
seconds = hour_duration*60*60
seconds=seconds+minute_duration*60
while 1==1:
    seconds = seconds-1
    print(seconds)
    time.sleep(1)
    pyautogui.press('shift')
    if seconds==0:
        print('time is upppppp')
        break

if 'ednesday' in day:
    #LESSON1
    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    join = driver.find_element_by_xpath('//*[@id="join-confno"]')
    join.send_keys(KISWAHILI)
    join.send_keys(Keys.ENTER)
    time.sleep(5)

    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(KISWAHILI_PASS)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()
    hour_duration=2
    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        print(seconds)
        time.sleep(1)
        pyautogui.press('shift')

        if seconds == 0:
            print('time is upppppp')
            break
    #LESSON2
    PATH ="C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get('https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    driver.get(CHEMISTRY_LINK)
    time.sleep(5)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()

    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        print(seconds)
        time.sleep(1)
        pyautogui.press('shift')

        if seconds == 0:
            print('time is upppppp')
            break
    #LESSON3
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    driver.get(PHYSICS_LINK)
    time.sleep(5)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()
    hour_duration=2
    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        print(seconds)
        time.sleep(1)
        pyautogui.press('shift')

        if seconds == 0:
            print('time is upppppp')
            break
    #LESSON4
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    driver.get(HISTORY_LINK)
    time.sleep(5)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()
    hour_duration=1
    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        print(seconds)
        time.sleep(1)
        pyautogui.press('shift')

        if seconds == 0:
            print('time is upppppp')
            break


if 'hursday' in day:
    #LESSON1
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    join = driver.find_element_by_xpath('//*[@id="join-confno"]')
    join.send_keys(KISWAHILI)
    join.send_keys(Keys.ENTER)
    time.sleep(5)

    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(KISWAHILI_PASS)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()
    hour_duration=1
    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        print(seconds)
        time.sleep(1)
        pyautogui.press('shift')

        if seconds == 0:
            print('time is upppppp')
            break
    #LESSON2
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    driver.get(PHYSICS_LINK)
    time.sleep(5)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()

    hour_duration=1
    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        print(seconds)
        time.sleep(1)
        pyautogui.press('shift')

        if seconds == 0:
            print('time is upppppp')
            break
    #LESSON3
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    driver.get(BIOLOGY_LINK)
    time.sleep(5)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    driver.quit()


    hour_duration=1
    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        print(seconds)
        time.sleep(1)
        pyautogui.press('shift')

        if seconds == 0:
            print('time is upppppp')
            break
    #LESSON4
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    driver.get(CHEMISTRY_LINK)
    time.sleep(5)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()

    #LESSON5
    hour_duration=1
    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        print(seconds)
        time.sleep(1)
        pyautogui.press('shift')

        if seconds == 0:
            print('time is upppppp')
            break
    #LESSON4
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    driver.get(ENGLISH_LINK)
    time.sleep(5)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()

if 'onday' in day:
    #LESSON1
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    join = driver.find_element_by_xpath('//*[@id="join-confno"]')
    join.send_keys(BIOLOGY)
    join.send_keys(Keys.ENTER)
    time.sleep(5)

    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(BIOLOGY_PASS)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()
    hour_duration=2
    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        print(seconds)
        time.sleep(1)
        pyautogui.press('shift')

        if seconds == 0:
            print('time is upppppp')
            break
    #LESSON2
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    driver.get(CHEMISTRY_LINK)
    time.sleep(5)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()
    hour_duration=1
    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        print(seconds)
        pyautogui.press('shift')

        time.sleep(1)
        if seconds == 0:
            print('time is upppppp')
            break
    #LESSON3
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    driver.get(MATH_LINK)
    time.sleep(5)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()
    hour_duration=1
    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        print(seconds)
        pyautogui.press('shift')

        time.sleep(1)
        if seconds == 0:
            print('time is upppppp')
            break
    #LESSON4
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    driver.get(ENGLISH_LINK)
    time.sleep(5)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()
if 'uesday' in day:
    #LESSON1
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    join = driver.find_element_by_xpath('//*[@id="join-confno"]')
    join.send_keys(KISWAHILI)
    join.send_keys(Keys.ENTER)
    time.sleep(5)

    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(KISWAHILI_PASS)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()

    hour_duration=1
    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        print(seconds)
        time.sleep(1)
        pyautogui.press('shift')

        if seconds == 0:
            print('time is upppppp')
            break
    #LESSON2
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    driver.get(MATH_LINK)
    time.sleep(5)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()
    for num in range(1):
        aspeak('WAKE UP FOR YOUR MATH LESSON')

    hour_duration=1
    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        print(seconds)
        time.sleep(1)
        pyautogui.press('shift')

        if seconds == 0:
            print('time is upppppp')
            break
    #LESSON3
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    driver.get(HISTORY_LINK)
    time.sleep(5)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()
    hour_duration=1
    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        print(seconds)
        time.sleep(1)
        pyautogui.press('shift')

        if seconds == 0:
            print('time is upppppp')
            break
    #LESSON4
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    driver.get(COMPUTER_LINK)
    time.sleep(5)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()
    hour_duration=1
    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        print(seconds)
        time.sleep(1)
        pyautogui.press('shift')

        if seconds == 0:
            print('time is upppppp')
            break
    #LESSON5
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    driver.get(PHYSICS_LINK)
    time.sleep(5)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()

if 'riday' in day:
    #LESSON1
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    join = driver.find_element_by_xpath('//*[@id="join-confno"]')
    join.send_keys(MATH)
    join.send_keys(Keys.ENTER)
    time.sleep(5)

    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(MATH_PASS)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()
    for num in range(1):
        aspeak('WAKE UP FOR YOUR math LESSON')
    hour_duration=2
    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        print(seconds)
        time.sleep(1)
        pyautogui.press('shift')

        if seconds == 0:
            print('time is upppppp')
            break
    #LESSON2
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    driver.get(BIOLOGY_LINK)
    time.sleep(5)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()
    for num in range(1):
        aspeak('WAKE UP FOR YOUR BIOLOGY LESSON')

    hour_duration=1
    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        print(seconds)
        time.sleep(1)
        pyautogui.press('shift')

        if seconds == 0:
            print('time is upppppp')
            break
    #LESSON3
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    driver.get(ENGLISH_LINK)
    time.sleep(5)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()

    hour_duration=1
    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        print(seconds)
        time.sleep(1)
        pyautogui.press('shift')

        if seconds == 0:
            print('time is upppppp')
            break
    #LESSON4
    PATH = "C:/Program Files/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(
        'https://accounts.google.com/o/oauth2/v2/auth/identifier?response_type=code&access_type=offline&client_id=849883241272-ed6lnodi1grnoomiuknqkq2rbvd2udku.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fzoom.us%2Fgoogle%2Foauth&state=cW1iekN4WXNTZGlld2FtWnBLZmVmUSxnb29nbGVfc2lnbmlu&_x_zm_rtaid=PBSSE6IzSFmWLIBYzoDnBQ.1602634392303.a2f80d3ef8f253874608754a34e86efc&_x_zm_rhtaid=179&flowName=GeneralOAuthFlow')

    login()
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(7)
    driver.get(COMPUTER_LINK)
    time.sleep(5)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('v')
    pyautogui.press('a')
    pyautogui.keyUp('alt')
    driver.quit()
