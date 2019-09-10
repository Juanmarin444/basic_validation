from flask import Flask, render_template, redirect, request, session, flash
import os

app = Flask(__name__)
s = os.urandom(24)
print(s)

app.secret_key='"I?S??uZ?¢?".o9?8?3`?-q"'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['name']) < 1:
        # display validation errors
        flash("Name cannot be empty.")
        print("Name cannot be empty.")
    else:
        # display success message
        flash('Success! Your name is {}'.format(request.form['name']))
        print('Success! Your name is {}'.format(request.form['name']))
    return redirect('/')

app.run(debug=True)
