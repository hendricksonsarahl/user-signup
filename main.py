from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/home")
def index():
    return render_template('home.html')

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', name=username)


app.run()