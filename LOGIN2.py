from flask import Flask, render_template, request, redirect,url_for,flash

from flask_mysqldb import MySQL

app = Flask(__name__)

mydb = MySQL(app)

app.config['MYSQL_HOST']='galgallo.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER']='galgallo'
app.config['MYSQL_PASSWORD']='Ronaldinho1'
app.config['MYSQL_DB']='galgallo$exampledatabase'


@app.route("/")
def index():

    return render_template('home.html')


@app.route("/signup", methods=['POST','GET'])
def signup():
    if request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']

        cursor=mydb.connection.cursor()
        cursor.execute("INSERT INTO example_table (names,email,password)VALUES(%s,%s,%s)", (username, email, password))
        mydb.connection.commit()

        return redirect('https://www.google.com')
    else:

        return render_template('login.html')








