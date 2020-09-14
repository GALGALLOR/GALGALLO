
import pandas as pd
import time
while 1 == 1:
    print('DO YOU HAVE AN ACCOUNT?')
    print('y/n')
    print('say stop to quit the loop')
    x = input()
    if ('stop') in x:
        exit()
    if ('n') in x:
       username = input('get yourself a username ')
       email = input('put an email ')
       password = input('choose a reasonable password ')
       df = pd.DataFrame(columns=['email','password'])
       for i in range(1):
           df.loc[i]=[email,password]
       df.to_excel(username+'.xlsx',sheet_name='Sheet1')
       df = pd.read_excel(username+'.xlsx')
       print(df)
       print('now log in')

    if ('y') in x:
        username = input('what is your username? ')
        df = pd.read_excel(username+'.xlsx')
        email = input('what is your email? ')
        passw = input('what is your password  a password ')
        for index,col in df.iterrows():
            if email in col['email'] and passw in col['password']:
                print('success')
                time.sleep(5)
                print('give us a few seconds')
                time.sleep(5)

            else:
                print('fail')
                time.sleep(5)
