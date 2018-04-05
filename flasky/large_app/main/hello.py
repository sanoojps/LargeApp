# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 01:59:29 2018

@author: sanooj
"""

from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return "<h1> Hello world </h1>"
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)



    
if __name__ =='__main__':
    app.run(debug=True)
