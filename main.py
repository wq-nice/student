#!/usr/bin/env python

from flask import Flask
from flask import render_template

from funcs import add

app=Flask(__name__)


@app.route('/')
def  hello():
    add(9,7)
    return render_template('home.html')


if __name__ == '__main__':
    app.debug=True
    app.run()


