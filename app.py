from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

@app.route('/')
def home():
    return redirect(url_for('register'))  # Redirect to registration page

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username  # Save user session
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username:  # Basic check, you can add proper authentication
            session['username'] = username
            return redirect(url_for('welcome'))
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/resume')
def resume():
    if 'username' in session:
        return render_template('resume.html')
    return redirect(url_for('login'))

@app.route('/projects')
def projects():
    if 'username' in session:
        return render_template('projects.html')
    return redirect(url_for('login'))

@app.route('/exit')
def exit():
    session.pop('username', None)  # Clear session
    return render_template('exit.html')

if __name__ == '__main__':
    app.run(debug=True)
