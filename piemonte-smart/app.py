import json
import time
import os
from json import JSONEncoder
#from firebase import firebase
# from firebase import Firebase
#
# config = {
#     'apiKey': "AIzaSyBHTXrVO9Ua9NwzefhIuJK5larGiIaApNM",
#     'authDomain': "piemonte-smart-a7115.firebaseapp.com",
#     'databaseURL': "https://piemonte-smart-a7115.firebaseio.com",
#     'projectId': "piemonte-smart-a7115",
#     'storageBucket': "piemonte-smart-a7115.appspot.com",
#     'messagingSenderId': "807365094983",
#     'appId': "1:807365094983:web:301ddeba25815327810b62",
#     'measurementId': "G-479SGQWB6D"
# }
#
# firebase = Firebase(config)
#
# db = firebase.database()
from flask import Flask, render_template, redirect, url_for, Response, jsonify, request, flash, make_response
import MySQLdb

app = Flask(__name__, template_folder='templates')

app.secret_key = 'secretkey'


# def getConnection ():
#     return mysql.connection (
#         host = '127.0.0.1',
#         db = 'sqlcomune',
#         user = 'root',
#         password = '~',
#         charset = 'utf8',
#         cursorclass = mysql.cursors.DictCursor
#     )

class User:
    def __init__(self, comune, email):
        self.comune = comune
        self.email = email


# user=User("Torino", "torino@gmail.com")

@app.route("/")
def home():
    return render_template('index1.html')


@app.route("/", methods=['GET', 'POST'])
def insert():
    db = MySQLdb.connect(user='root',
                         password='',
                         host='127.0.0.1',
                         database='sqlcomune')
    cur = db.cursor()

    if 'comune' in request.form and 'email' in request.form and request.method == 'POST':
        comune = request.form['comune']
        email = request.form['email']
        sql = 'INSERT IGNORE INTO comunedelpiemonte(comune, email) VALUES (%s,%s)'
        cur.execute(sql, [comune, email])
        db.commit()
        print('passato')
        return render_template('index2.html', email=email)
    elif 'comuneLed' in request.form and 'emailLed' in request.form and request.method == 'POST':
        comune = request.form['comuneLed']
        email = request.form['emailLed']
        sql = "SELECT comune, email FROM comunedelpiemonte WHERE comune = %s AND email = %s"
        cur.execute(sql, [comune, email])
        rows = cur.fetchall()
        print(rows)
        comune1 = ''
        email1 = ''
        for row in rows:
            comune1 = row[0]
            email1 = row[1]
        db.close()
        #print('passato')
        return render_template('index3.html', comune=comune1, email=email1)
    elif 'comuneRisorse' in request.form and 'emailRisorse' in request.form and request.method == 'POST':
        comune = request.form['comuneRisorse']
        email = request.form['emailRisorse']
        sql = "SELECT comune, email FROM comunedelpiemonte WHERE comune = %s AND email = %s"
        cur.execute(sql, [comune, email])
        rows = cur.fetchall()
        print(rows)
        comune1 = ''
        email1 = ''
        for row in rows:
            comune1 = row[0]
            email1 = row[1]
        db.close()
        #print('passato')
        return render_template('index4.html', comune=comune1, email=email1)
    else:
        print("Error insert")


@app.route("/", methods=['GET', 'POST'])
def output():
    db = MySQLdb.connect(user='root',
                         password='',
                         host='127.0.0.1',
                         database='sqlcomune')
    cur = db.cursor()

    if 'comuneLed' in request.form and 'emailLed' in request.form and request.method == 'POST':
        comune = request.form['comuneLed']
        email = request.form['emailLed']
        sql = "SELECT comune, email FROM comunedelpiemonte WHERE comune = %s AND email = %s"
        cur.execute(sql, [comune, email])
        rows = cur.fetchall()
        print(rows)
        comune1 = ''
        email1 = ''
        for row in rows:
            comune1 = row[0]
            email1 = row[1]
        db.close()
        return render_template('output.html', comune=comune1, email=email1)
    else:
        print("Error output")
        return 'error'


# @app.route('/')
# def comune():
#      cur = mysql.connection.cursor()
#      cur.execute("SELECT * FROM comunedelpiemonte")
#      fetchdata= cur.fetchall()
#      cur.close()
#      return render_template('index2.html', data=fetchdata)

@app.route('/RIDUZIONE DEI CONSUMI DEL 50%', methods=['GET', 'POST'])
def index2():
    return render_template('registration.html')


@app.route('/TUTTO LED', methods=['GET', 'POST'])
def index3():
    return render_template('regisTuttoLed.html')


@app.route('/QUANTE RISORSE HAI?', methods=['GET', 'POST'])
def index4():
    # if request.method == 'GET':
    #     return redirect(url_for('index1'))/
    return render_template('regisQuanteRisorse.html')


# @app.route('/CONTATTO', methods=['GET', 'POST'])
# def contatto():
#     # if request.method == 'GET':
#     #     return redirect(url_for('index1'))/
#     return render_template('Contact.html')


if __name__ == "__main__":
    #app.debug = True
    #app.run()
    if os.environ.get('APP_LOCATION') == 'heroku':
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        app.run( debug=True)
    #app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
