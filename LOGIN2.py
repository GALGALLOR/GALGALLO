from flask import Flask, render_template, request, redirect

import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="GALGALLO10",
    db="login_data")
#HACKED ==== bankare	liban123	libanwario81@gmail.com


@app.route("/")
def index():
    return render_template("login.html", title="SignUP")


@app.route("/signUp", methods=["POST"])
def signUp():
    username = str(request.form["username"])
    password = str(request.form["password"])
    email = str(request.form["email"])
    global cursor
    cursor = mydb.cursor()

    cursor.execute("INSERT INTO user (username,password,email)VALUES(%s,%s,%s)", (username, password, email))
    mydb.commit()

    if 'galgallo' in username and 'GALGALLO10' in password and 'ga.roba@lightacademy.ac.ke' in email:
        return redirect('/usersthatshouldonlybeseenbygalgallo')
    return redirect('https://www.google.com/search?sxsrf=ALeKk026Guv_2udqOA6vod7ofb5z8ir8_Q%3A1600880677537&source=hp&ei=JYBrX4XbHaKJlwST7Le4Bw&q=how+to+spot+a+dumb+person&oq=how+to+spot+a+dumb+person&gs_lcp=CgZwc3ktYWIQAzoHCCMQ6gIQJzoECCMQJzoFCAAQkQI6BQguEJECOgUIABCxAzoICAAQsQMQgwE6CAguEMcBEKMCOgQIABBDOgcIABAUEIcCOggILhCxAxCDAToFCC4QsQM6AggAOgYIABAWEB46AgguUKEgWOxXYJlbaARwAHgAgAHSBIgBsTmSAQwwLjQuMTcuMy4xLjKYAQCgAQGqAQdnd3Mtd2l6sAEK&sclient=psy-ab&ved=0ahUKEwjFgfCg4f_rAhWixIUKHRP2DXcQ4dUDCAw&uact=5')

@app.route('/usersthatshouldonlybeseenbygalgallo')
def users():
    resultValue = cursor.execute("SELECT * FROM user")
    userDetails = cursor.fetchall()
    return render_template('users.html',userDetails=userDetails)




if __name__ == "__main__":
    app.run(debug=True)