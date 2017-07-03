from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    username = request.args.get('username')
    email = request.args.get('email')
    username_error = request.args.get('username_error')
    password_error = request.args.get('password_error')
    verify_error = request.args.get('verify_error')
    email_error = request.args.get('email_error')
    return render_template('home.html', username=username, email=email, username_error=username_error,
        password_error=password_error, verify_error=verify_error, email_error=email_error)

def invalid_string_length(string):
    return (len(string) < 3 or len(string) > 20)


@app.route("/home", methods=['POST'])
@app.route("/user-signup", methods=["POST"])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    error_msg = ''
    if not username:
        error_msg += "username_error=please enter a username&"
    elif re.search('\s', username):
        error_msg += "username_error=username can't have spaces&"
        username = re.sub('\s', '', username)
    elif invalid_string_length(username):
        error_msg += "username_error=username must be between 3 and 20 characters&"
    if not password:
        error_msg += "password_error=please create a password&"
    elif re.search('\s', password):
        error_msg += "password_error=password can't have spaces&"
    elif invalid_string_length(password):
        error_msg += "password_error=password must be between 3 and 20 characters&"
    elif not verify:
        error_msg += "verify_error=please re-enter your password&"
    elif re.search('\s', verify):
        error_msg += "verify_error=password can't have spaces&"
    elif invalid_string_length(verify):
        error_msg += "verify_error=verify password must be between 3 and 20 characters&"
    elif password != verify:
        error_msg += "verify_error=verify password does not match password&"
    if email:
        if len(email.split('@')) != 2:
            error_msg += "email_error=email is missing the @ symbol&"
        elif len(email.split('.')) != 2:
            error_msg += "email_error=email is missing the period&"
        elif re.search('\s', email):
            error_msg += "email_error=email can't have spaces&"
        elif invalid_string_length(email):
            error_msg += "email_error=please enter an email between 3 and 20 characters&"
            
    if not (error_msg):
        return render_template('welcome.html', username = username)
    else:
        return redirect('/?' + error_msg + 'username=' + username + '&email=' + email)

app.run()