from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Simple example authentication
        if username == 'admin' and password == 'admin':
            return f"<h1>Welcome, {username}! 🚀</h1>"
        else:
            return "<h3>Invalid credentials. Please try again.</h3>"

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
