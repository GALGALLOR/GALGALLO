
from flask_mysqldb import MySQL
from flask import  get_flashed_messages, session,Flask,render_template,redirect,request,flash,url_for
app=Flask(__name__)

mydb=MySQL(app)

app.config['MYSQL_HOST']=''
app.config['MYSQL_USER']=''
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='gang_database'

app.secret_key='mimi'


@app.route('/')
def base():
    return redirect(url_for('login'))

@app.route('/options')
def settings():
    return render_template('settings.html')

@app.route('/settingstext/<text>')
def settingstext(text):
    session['text']=text
    return redirect(url_for('settings'))

@app.route('/settingsmode/<mode>')
def settingsmode(mode):
    session['mode']=mode
    return redirect(url_for('settings'))

@app.route('/settingsheading/<heading>')
def settingsheading(heading):

    session['heading']=heading

    return redirect(url_for('settings'))

@app.route('/settingslist/<list>')
def settingslist(list):

    session['list']=list

    return redirect(url_for('settings'))


@app.route('/create_new',methods=['POST','GET'])
def signup():

    if request.method == 'POST':

        session.permanent= True
        username=request.form['username']
        password=request.form['password']

        cursor=mydb.connection.cursor()
        cursor.execute('SELECT * FROM USERDETAILS WHERE USERNAME="'+username+'" AND PASSWORD="'+password+'"')
        l=cursor.fetchall()
        global L
        for L in l:
            print(L)
        details=L
        if username==details[0] and password==details[1]:
            flash('ACCOUNT ALREADY EXISTS')
            return render_template('signup.html')
        elif username==details[0] and password!=details[1]:
            flash('Username is taken')
            return render_template('signup.html')
        else:
            session['username'] = username
            session['password'] = password
            cursor.execute('INSERT INTO USERDETAILS(USERNAME,PASSWORD)VALUES(%s,%s)',(username,password))
            mydb.connection.commit()
            return redirect(url_for('profile'))
    else:

        if 'username' in session:
            return redirect(url_for('profile'))
        else:

            return render_template('signup.html')



@app.route('/login',methods=['POST','GET'])
def login():

    if request.method == 'POST':
        session.permanent=True

        username=request.form['username']
        password=request.form['password']
        cursor = mydb.connection.cursor()

        session['username']=username
        session['password']=password

        cursor.execute('SELECT * FROM USERDETAILS WHERE USERNAME="'+username+'" AND PASSWORD="'+password+'"')
        f=cursor.fetchall()
        global r
        for r in f:
            print(r)
        F=r
        if username == F[0] and password==F[1]:
            flash('welcome back')
            return redirect(url_for('profile'))
        elif username == F[0] and password !=F[1]:
            flash('wrong password!')
            return render_template('login.html')
        else:
            flash('account does not exist')
            return render_template('login.html')

    else:
        if 'username' in session:
            return redirect(url_for('profile'))
        else:

            return render_template('login.html')

@app.route('/profile')
def profile():
    if 'username' in session:
        username=session['username']
        cursor = mydb.connection.cursor()
        cursor.execute('SELECT USERNAME FROM USERDETAILS ')
        f=cursor.fetchall()
        f1=[]
        for items in f:

            for x in items:
                f1.append(x)


        return render_template('profile.html',user=f1,username=username)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username',None)
    flash('logged out successfully')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)

