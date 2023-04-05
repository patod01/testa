import os, json, time
from flask import (
     Flask
)
from sys import argv
import sqlite3, time

app = Flask(__name__)

@app.route('/')
def home():
     return "render_template('index.html')"

if __name__ == '__main__':
     print('i\'m the world')
     app.run()

#ned
