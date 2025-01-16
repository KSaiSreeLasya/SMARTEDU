from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data for authentication
USER_DATA = {
    "email": "user@example.com",
    "password": "password123"
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/menu')
def menu():
    return "<h1>Welcome to the Menu Page</h1>"

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if email == USER_DATA['email'] and password == USER_DATA['password']:
        return redirect(url_for('menu'))
    else:
        return "<h1>Login Failed: Invalid Credentials</h1>"

if __name__ == "__main__":
    app.run(debug=True)
