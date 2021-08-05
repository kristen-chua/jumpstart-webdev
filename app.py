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
    #return title # old command
    return render_template('new_talk.html', title=talk_title) #how to pass in data into a template

# go to http://127.0.0.1:5000/talk to see this page
@app.route('/talk', methods=['POST', 'GET'])
def talk():
    if request.method == 'GET':
        return redirect(url_for('new_talk'))

    talk_title = request.form['form-title']
    talk_description = request.form['form-description']

    return render_template('talk.html', title=talk_title, description=talk_description)

if __name__ == '__main__':
    app.run(debug=True)