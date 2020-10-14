from selenium import webdriver
import pyautogui # for pressing keys off the website
from selenium.webdriver.common.keys import Keys #for pressing keys on the keyboard in chrome
import time # to bring delays in the code

#initialize the key codes for zoom
MATH ='782 191 0689'
MATH_PASS='123456'
MINE = '710 762 9261'
COMPUTER = '573 904 3667'
COMPUTER_PASS = '12345678'
KISWAHILI='9548478307'
KISWAHILI_PASS = '123456'
ENGLISH='7563264376'
ENGLISH_PASS = '123456'
BIOLOGY='6292489277'
BIOLOGY_PASS = '123456'
PHYSICS='9841406308'
PHYSICS_PASS='123456'
CHEMISTRY='7651793624'
CHEMISTRY_PASS = '123456'
HISTORY='9049924850'
HISTORY_PASS = '12345678'
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

def join_class():
    try:
        if now.minute > 45:
            driver.quit()
            pyautogui.press('left')
        elif now.minute <= 45:
            time.sleep(7)
            pyautogui.press('enter')
            time.sleep(10)
            pyautogui.keyDown('alt')
            pyautogui.press('v')
            pyautogui.keyUp('alt')
            time.sleep(1800)
            pyautogui.keyDown('tab')
            pyautogui.press('esc')
            pyautogui.keyUp('tab')

    except:
        pyautogui.press('left')

while 1==1:
    if now.strftime('%A')=='Wednesday':
        if now.hour==9:
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
            for num in range(1):
                aspeak('WAKE UP FOR YOUR KISWAHILI LESSON')

            join_class()
        elif now.hour==11:
            login()
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(7)
            join = driver.find_element_by_xpath('//*[@id="join-confno"]')
            join.send_keys(CHEMISTRY)
            join.send_keys(Keys.ENTER)
            time.sleep(5)
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.typewrite(CHEMISTRY_PASS)
            pyautogui.press('enter')
            for num in range(1):
                aspeak('WAKE UP FOR YOUR CHEMISTRY LESSON')

            join_class()
        elif now.hour == 12:
            login()
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(7)
            join = driver.find_element_by_xpath('//*[@id="join-confno"]')
            join.send_keys(PHYSICS)
            join.send_keys(Keys.ENTER)
            time.sleep(5)
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.typewrite(PHYSICS_PASS)
            pyautogui.press('enter')
            for num in range(1):
                aspeak('WAKE UP FOR YOUR PHYSICS LESSON')

            join_class()
        elif now.hour == 13:
            login()
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(7)
            join = driver.find_element_by_xpath('//*[@id="join-confno"]')
            join.send_keys(HISTORY)
            join.send_keys(Keys.ENTER)
            time.sleep(5)
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.typewrite(HISTORY_PASS)
            pyautogui.press('enter')
            for num in range(1):
                aspeak('WAKE UP FOR YOUR HISTORY LESSON')

            join_class()
        else:
            pyautogui.press('left')
    elif now.strftime('%A')=='Thursday':
        if now.hour==9:
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
            for num in range(1):
                aspeak('WAKE UP FOR YOUR KISWAHILI LESSON')

            join_class()
        elif now.hour==10:
            login()
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(7)
            join = driver.find_element_by_xpath('//*[@id="join-confno"]')
            join.send_keys(PHYSICS)
            join.send_keys(Keys.ENTER)
            time.sleep(5)
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.typewrite(PHYSICS_PASS)
            pyautogui.press('enter')
            for num in range(1):
                aspeak('WAKE UP FOR YOUR PHYSICS LESSON')

            join_class()
        elif now.hour==11:
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
            for num in range(1):
                aspeak('WAKE UP FOR YOUR BIOLOGY LESSON')

            join_class()
        elif now.hour == 12:
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
            for num in range(1):
                aspeak('WAKE UP FOR YOUR BIOLOGY LESSON')

            join_class()
        elif now.hour == 13:
            login()
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(7)
            join = driver.find_element_by_xpath('//*[@id="join-confno"]')
            join.send_keys(ENGLISH)
            join.send_keys(Keys.ENTER)
            time.sleep(5)
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.typewrite(ENGLISH_PASS)
            pyautogui.press('enter')
            for num in range(1):
                aspeak('WAKE UP FOR YOUR ENGLISH LESSON')

            join_class()

        else:
            pyautogui.press('left')
    elif now.strftime('%A')=='Monday':
        if now.hour==9:
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
            for num in range(1):
                aspeak('WAKE UP FOR YOUR BIOLOGY LESSON')

            join_class()
        elif now.hour==11:
            login()
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(7)
            join = driver.find_element_by_xpath('//*[@id="join-confno"]')
            join.send_keys(CHEMISTRY)
            join.send_keys(Keys.ENTER)
            time.sleep(5)
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.typewrite(CHEMISTRY_PASS)
            pyautogui.press('enter')
            for num in range(1):
                aspeak('WAKE UP FOR YOUR CHEMISTRY LESSON')

            join_class()
        elif now.hour == 12:
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
            for num in range(1):
                aspeak('WAKE UP FOR YOUR MATHEMATICS LESSON')

            join_class()
        elif now.hour == 13:
            login()
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(7)
            join = driver.find_element_by_xpath('//*[@id="join-confno"]')
            join.send_keys(ENGLISH)
            join.send_keys(Keys.ENTER)
            time.sleep(5)
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.typewrite(ENGLISH_PASS)
            pyautogui.press('enter')
            for num in range(1):
                aspeak('WAKE UP FOR YOUR ENGLISH LESSON')

            join_class()
        else:
            pyautogui.press('left')
    elif now.strftime('%A')=='Tuesday':
        if now.hour==9:
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
            for num in range(1):
                aspeak('WAKE UP FOR YOUR KISWAHILI LESSON')

            join_class()
        elif now.hour==10:
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
            for num in range(1):
                aspeak('WAKE UP FOR YOUR MATHEMATICS LESSON')

            join_class()
        elif now.hour==11:
            login()
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(7)
            join = driver.find_element_by_xpath('//*[@id="join-confno"]')
            join.send_keys(HISTORY)
            join.send_keys(Keys.ENTER)
            time.sleep(5)
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.typewrite(HISTORY_PASS)
            pyautogui.press('enter')
            for num in range(1):
                aspeak('WAKE UP FOR YOUR HISTORY LESSON')

            join_class()
        elif now.hour == 12:
            login()
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(7)
            join = driver.find_element_by_xpath('//*[@id="join-confno"]')
            join.send_keys(COMPUTER)
            join.send_keys(Keys.ENTER)
            time.sleep(5)
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.typewrite(COMPUTER_PASS)
            pyautogui.press('enter')
            for num in range(1):
                aspeak('WAKE UP FOR YOUR COMPUTER LESSON')

            join_class()
        elif now.hour == 13:
            login()
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(7)
            join = driver.find_element_by_xpath('//*[@id="join-confno"]')
            join.send_keys(PHYSICS)
            join.send_keys(Keys.ENTER)
            time.sleep(5)
            pyautogui.press('left')
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.typewrite(PHYSICS_PASS)
            pyautogui.press('enter')
            for num in range(1):
                aspeak('WAKE UP FOR YOUR PHYSICS LESSON')

            join_class()
        else:
            pyautogui.press('left')
    else:
        pyautogui.press('left')
