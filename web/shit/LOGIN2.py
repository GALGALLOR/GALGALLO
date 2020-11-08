from flask import Flask,redirect,render_template,request,session,url_for,flash
app=Flask(__name__)

app.secret_key='mimi'

@app.route('/')
def base():
    return redirect(url_for('login'))



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        names=request.form['names']
        password=request.form['password']
        session['names']=names
        session['password']=password
        return redirect(url_for('user',names=names))
    else:
        return render_template('login.html')

@app.route('/home')
def user():
    if 'names' in session:
        names=session['names']
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)





