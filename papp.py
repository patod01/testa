import os, json, time
from flask import (
     Flask, request, render_template,
     url_for, redirect, jsonify,
)
from sys import argv
import sqlite3, time


app = Flask(__name__)

data_base = 'db/base.db'

if not os.path.isfile(data_base):
     with open('table.sql') as query:
          query = ''.join(query.readlines())
          print(query)
          with sqlite3.connect(data_base) as con:
               con.execute(query)


@app.route('/')
def home():
     return render_template('index.html')

@app.route('/<int:efe>/') # inserta una fecha
def crea_id(efe: int):
     with sqlite3.connect(data_base) as con:
          query = con.execute(
               "INSERT INTO sample (number, date) VALUES (?, ?)",
               ( efe**2, round(time.time()) )
          )
     return jsonify(['numero agregado', efe**2])

@app.route('/id/<int:nid>/') # devuelve la informacion a un id asociado
def getFecha(nid):
     with sqlite3.connect(data_base) as con:
          print('asdf')
          hora = []
          query = con.execute(
               "SELECT * FROM sample WHERE id = ?",
               (nid,)
          )

     hora = [row for row in query]

     if hora:
          return jsonify({
               '0_mensaje': 'se ha recuperado la siguiente informacion en base al ID.',
               '1_id': hora[0][0],
               '2_numero': hora[0][1],
               '3_fecha': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hora[0][2])),
          })
     else:
          return jsonify('you suck.')

if __name__ == '__main__':
     app.run(debug=True, host="0.0.0.0", port=int(os.getenv("PORT", 10011)))

#ned
