from flask import Flask
from flask import render_template

#Create a flask instance
app=Flask(__name__)

"""
FIlters
safe
capitalize
lower
upper
title
trim
striptags
"""

@app.route('/')
def index():
    first_name="Sai"
    stuff="This is a <strong>Bold</Strong>Text"
    text="This is a Bold Text"
    names = ["Sai", "Srivatsa","Shiva","Krishna"]
    return render_template('index.html',
    first_name=first_name,
    stuff=stuff,
    text=text,
    names=names   
    )

@app.route('/user/<name>')

def user(name):
    return render_template('user.html',user_name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html')

