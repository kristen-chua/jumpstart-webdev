# app.py

from flask import Flask, render_template, redirect, url_for, jsonify, request
from talk_mashup_bot import talk_mashup_bot

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world!"

# go to http://127.0.0.1:5000/talk/new to see this page
@app.route('/talk/new')
def new_talk():
    talk_title = talk_mashup_bot.generateTitle()
    return talk_title

if __name__ == '__main__':
    app.run(debug=True)