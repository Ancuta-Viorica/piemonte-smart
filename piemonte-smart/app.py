import json
import time
import os
from numpy import mean
from json import JSONEncoder
# from firebase import firebase
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
# import query as query
from flask import Flask, render_template, redirect, url_for, Response, jsonify, request, flash, make_response, session
import MySQLdb
import sys
import csv
import pandas as pd

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

# dbQuery = 'SELECT * FROM comunedelpiemonte;'
# db = MySQLdb.connect(user='root',
#                      password='',
#                      host='127.0.0.1',
#                      database='sqlcomune')
# cur = db.cursor()
# cur.execute(dbQuery)
# # result = cur.fetchall()
# db.close


# df=pd.DataFrame(list(all_rows),columns=["Comune.email"])
# df.to_csv("comunedelpiemonte.csv")
# c = csv.writer(open("comunedelpiemonte.csv","wb"))
# c.writerow(result)


class User:
    def __init__(self, comune, email):
        self.comune = comune
        self.email = email


# user=User("Torino", "torino@gmail.com")

@app.route("/")
def home():
    try:
        return render_template('Scenario3.html')
    except:
        return render_template('errore.html')


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
        session['username'] = comune
        session['email'] = email
        sql = 'INSERT IGNORE INTO comunedelpiemonte(comune, email) VALUES (%s,%s) '
        cur.execute(sql, [comune, email])
        db.commit()
        return render_template('index15-16.html', comune=comune)
            # return render_template('index15-16.html', comune=comune, msg=msg)
        # else :
        #     msg = 'Incorrect username / password !'
        # #return render_template('registration.html', msg=msg)
    elif 'comuneLed' in request.form and 'emailLed' in request.form and request.method == 'POST':
        comune = request.form['comuneLed']
        email = request.form['emailLed']
        session['username'] = comune
        session['emailed'] = email
        sql = 'INSERT IGNORE INTO comunedelpiemonte(comune, email) VALUES (%s,%s)'
        cur.execute(sql, [comune, email])
        rows = cur.fetchall()
        print(rows)
        comune1 = ''
        email1 = ''
        for row in rows:
            comune1 = row[0]
            email1 = row[1]
        db.close()
        return render_template('indexLed.html', comuneled=comune)
    elif 'comuneRisorse' in request.form and 'emailRisorse' in request.form and request.method == 'POST':
        comune = request.form['comuneRisorse']
        email = request.form['emailRisorse']
        session['username'] = comune
        session['emaiRisorse'] = email
        sql = 'INSERT IGNORE INTO comunedelpiemonte(comune, email) VALUES (%s,%s)'
        cur.execute(sql, [comune, email])
        rows = cur.fetchall()
        print(rows)
        comune1 = ''
        email1 = ''
        for row in rows:
            comune1 = row[0]
            email1 = row[1]
        db.close()
        # print('passato')
        return render_template('indexRisorse.html', comunerisorse=comune)

    elif 'consumoAnnuale2015' in request.form and request.method == 'POST':
        comune = session['username']
        email = session['email']
        print(comune, email)
        sql = 'SELECT id FROM comunedelpiemonte WHERE comune = %s AND email = %s'
        cur.execute(sql, [comune, email])
        rows = cur.fetchall()
        for row in rows:
            id = row[0]
        consumoAnnuale2015 = request.form['consumoAnnuale2015']
        costoAnnuale2015 = request.form['costoAnnuale2015']
        totPuntiLuce2015 = request.form['puntiLuce2015']
        totIncandescenza2015 = request.form['incandescenza2015']
        totMercurio2015 = request.form['mercurio2015']
        totAlogenuri2015 = request.form['alogenuriIoduriMetallici2015']
        totSodioBassa2015 = request.form['sodio2015']
        totSodioAlta2015 = request.form['sodio22015']
        totLed2015 = request.form['led2015']

        consumoAnnuale2016 = request.form['consumoAnnuale2016']
        costoAnnuale2016 = request.form['costoAnnuale2016']
        totPuntiLuce2016 = request.form['puntiLuce2016']
        totIncandescenza2016 = request.form['incandescenza2016']
        totMercurio2016 = request.form['mercurio2016']
        totAlogenuri2016 = request.form['alogenuriIoduriMetallici2016']
        totSodioBassa2016 = request.form['sodio2016']
        totSodioAlta2016 = request.form['sodio22016']
        totLed2016 = request.form['led2016']
        totPuntiLuceDivisi2015 = int(totIncandescenza2015) + int(totMercurio2015) + int(totAlogenuri2015) + int(totSodioBassa2015) + int(
            totSodioAlta2015) + int(totLed2015)
        totPuntiLuceDivisi2016 = int(totIncandescenza2016) + int(totMercurio2016) + int(totAlogenuri2016) + int(
            totSodioBassa2016) + int(
            totSodioAlta2016) + int(totLed2016)
        lista2015 = [totIncandescenza2015,totMercurio2015,totAlogenuri2015,totSodioBassa2015,totSodioAlta2015,totLed2015]
        lista2016 = [totIncandescenza2016,totMercurio2016,totAlogenuri2016,totSodioBassa2016,totSodioAlta2016,totLed2016]
        print(lista2015,lista2016,'entrato 15+16')
        if int(totPuntiLuce2015) == totPuntiLuceDivisi2015 and int(totPuntiLuce2016) == totPuntiLuceDivisi2016:
            sql2015 = 'INSERT IGNORE INTO dati2015(idComune, ConsumoAnnuale, CostoAnnuale, PuntiLuce, Led, Incandescenza, Mercurio, Ioduri, sodioAlta, sodioBassa) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            sql2016 = 'INSERT IGNORE INTO dati2016(idComune, ConsumoAnnuale, CostoAnnuale, PuntiLuce, Led, Incandescenza, Mercurio, Ioduri, sodioAlta, sodioBassa) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

            cur.execute(sql2015, [id, consumoAnnuale2015, costoAnnuale2015, totPuntiLuce2015, totIncandescenza2015, totMercurio2015, totAlogenuri2015,
                          totSodioBassa2015, totSodioAlta2015, totLed2015])
            cur.execute(sql2016, [id, consumoAnnuale2016, costoAnnuale2016, totPuntiLuce2016, totIncandescenza2016,
                                  totMercurio2016, totAlogenuri2016,
                                  totSodioBassa2016, totSodioAlta2016, totLed2016])
            db.commit()
            lista = media(lista2015, lista2016)
            print(lista, 'Media')
            return render_template('output.html', comune=comune, email=email, puntiLuce=totPuntiLuce2015,
                               incandescenza=lista[0], mercurio=lista[1], ioduri=lista[2],
                               sodioAlta=lista[3], sodioBassa=lista[4], led=lista[5])
        return render_template('errore.html')

    elif 'consumoAnnuale2019' in request.form and request.method == 'POST':
        comune = session['username']
        email = session['email']
        print(comune, email)
        sql = 'SELECT id FROM comunedelpiemonte WHERE comune = %s AND email = %s'
        cur.execute(sql, [comune, email])
        rows = cur.fetchall()
        for row in rows:
            id = row[0]
        consumoAnnuale = request.form['consumoAnnuale2019']
        costoAnnuale = request.form['costoAnnuale2019']
        totPuntiLuce = request.form['puntiLuce2019']
        totIncandescenza = request.form['incandescenza2019']
        totMercurio = request.form['mercurio2019']
        totAlogenuri = request.form['alogenuriIoduriMetallici2019']
        totSodioBassa = request.form['sodio2019']
        totSodioAlta = request.form['sodio22019']
        totLed = request.form['led2019']
        totPuntiLuceDivisi = int(totIncandescenza)+int(totMercurio)+int(totAlogenuri)+int(totSodioBassa)+int(totSodioAlta)+int(totLed)
        print(totPuntiLuce,totPuntiLuceDivisi)
        if int(totPuntiLuce) == totPuntiLuceDivisi:
            print('enter 50')
            sql = 'INSERT IGNORE INTO dati2019(idComune, ConsumoAnnuale, CostoAnnuale, PuntiLuce, Led, Incandescenza, Mercurio, Ioduri, sodioAlta, sodioBassa) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(sql, [id, consumoAnnuale, costoAnnuale, totPuntiLuce, totIncandescenza, totMercurio, totAlogenuri,
                          totSodioBassa, totSodioAlta, totLed])
            db.commit()
            lista = calcoli(float(consumoAnnuale),int(costoAnnuale),float(totIncandescenza), float(totMercurio), float(totAlogenuri), float(totSodioAlta), float(totSodioBassa), float(totLed))
            return render_template('output.html', comune=comune, email=email, puntiLuce=totPuntiLuce,
                               incandescenza=lista[0], mercurio=lista[1], ioduri=lista[2],
                               sodioAlta=lista[3], sodioBassa=lista[4], led=lista[5])
        else:
            print('exit')
            return render_template('errore.html')

    elif 'consumoAnnuale2019' in request.form and request.method == 'POST':
        comune = session['username']
        email = session['emailLed']
        print(comune, email)
        sql = 'SELECT id FROM comunedelpiemonte WHERE comune = %s AND email = %s'
        cur.execute(sql, [comune, email])
        rows = cur.fetchall()
        for row in rows:
            id = row[0]
        consumoAnnuale = request.form['consumoAnnuale2019']
        costoAnnuale = request.form['costoAnnuale2019']
        totPuntiLuce = request.form['puntiLuce2019']
        totIncandescenza = request.form['incandescenza2019']
        totMercurio = request.form['mercurio2019']
        totAlogenuri = request.form['alogenuriIoduriMetallici2019']
        totSodioBassa = request.form['sodio2019']
        totSodioAlta = request.form['sodio22019']
        totLed = request.form['led2019']
        totInvestimento = request.form['investimento']
        totPuntiLuceDivisi = int(totIncandescenza) + int(totMercurio) + int(totAlogenuri) + int(totSodioBassa) + int(
            totSodioAlta) + int(totLed)
        print(totPuntiLuce, totPuntiLuceDivisi)
        if int(totPuntiLuce) == totPuntiLuceDivisi:
            print('enter led')
            sql = 'INSERT IGNORE INTO dati2019(idComune, ConsumoAnnuale, CostoAnnuale, PuntiLuce, Led, Incandescenza, Mercurio, Ioduri, sodioAlta, sodioBassa) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(sql,[id, consumoAnnuale, costoAnnuale, totPuntiLuce, totIncandescenza, totMercurio, totAlogenuri,
                         totSodioBassa, totSodioAlta, totLed, totInvestimento])
            db.commit()
            lista = calcoli(float(consumoAnnuale), float(totIncandescenza), float(totMercurio), float(totAlogenuri),
                            float(totSodioAlta), float(totSodioBassa), float(totLed), float(totInvestimento))
            return render_template('output.html', comune=comune, email=email, puntiLuce=totPuntiLuce,
                                   incandescenza=lista[0], mercurio=lista[1], ioduri=lista[2],
                                   sodioAlta=lista[3], sodioBassa=lista[4], led=lista[5], investimento=totInvestimento)
        else:
            print('exit')
            return render_template('errore.html')

    elif 'consumoAnnuale2019' in request.form and request.method == 'POST':
        comune = session['username']
        email = session['emailRisorse']
        print(comune, email)
        sql = 'SELECT id FROM comunedelpiemonte WHERE comune = %s AND email = %s'
        cur.execute(sql, [comune, email])
        rows = cur.fetchall()
        for row in rows:
            id = row[0]
        consumoAnnuale = request.form['consumoAnnuale2019']
        costoAnnuale = request.form['costoAnnuale2019']
        totPuntiLuce = request.form['puntiLuce2019']
        totIncandescenza = request.form['incandescenza2019']
        totMercurio = request.form['mercurio2019']
        totAlogenuri = request.form['alogenuriIoduriMetallici2019']
        totSodioBassa = request.form['sodio2019']
        totSodioAlta = request.form['sodio22019']
        totLed = request.form['led2019']
        totPuntiLuceDivisi = int(totIncandescenza) + int(totMercurio) + int(totAlogenuri) + int(totSodioBassa) + int(
            totSodioAlta) + int(totLed)
        print(totPuntiLuce, totPuntiLuceDivisi)
        if int(totPuntiLuce) == totPuntiLuceDivisi:
            print('enter Risorse')
            sql = 'INSERT IGNORE INTO dati2019(idComune, ConsumoAnnuale, CostoAnnuale, PuntiLuce, Led, Incandescenza, Mercurio, Ioduri, sodioAlta, sodioBassa) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(sql,[id, consumoAnnuale, costoAnnuale, totPuntiLuce, totIncandescenza, totMercurio, totAlogenuri,
                         totSodioBassa, totSodioAlta, totLed])
            db.commit()
            lista = calcoli(float(consumoAnnuale), float(totIncandescenza), float(totMercurio), float(totAlogenuri),
                            float(totSodioAlta), float(totSodioBassa), float(totLed))
            return render_template('output.html', comune=comune, email=email, puntiLuce=totPuntiLuce,
                                   incandescenza=lista[0], mercurio=lista[1], ioduri=lista[2],
                                   sodioAlta=lista[3], sodioBassa=lista[4], led=lista[5])
        else:
            print('exit')
            return render_template('errore.html')
    else:
        return render_template('errore.html')


@app.route('/RIDUZIONE DEI CONSUMI DEL 50%', methods=['GET', 'POST'])
def index2():
    try:
        return render_template('registration.html')
    except:
        return render_template('errore.html')


@app.route('/TUTTO LED', methods=['GET', 'POST'])
def index3():
    try:
        return render_template('regisTuttoLed.html')
    except:
        return render_template('errore.html')


@app.route('/QUANTE RISORSE HAI?', methods=['GET', 'POST'])
def index4():
    try:
        return render_template('regisQuanteRisorse.html')
    except:
        return render_template('errore.html')


@app.route('/index1516', methods=['GET', 'POST'])
def index1516():
    try:
        return render_template('index15-16.html')
    except:
        return render_template('errore.html')


@app.route('/index2019', methods=['GET', 'POST'])
def index2019():
    try:
        return render_template('index2019.html')
    except:
        return render_template('errore.html')


def media(a,b):
    i = 0
    listamedia = []
    while(i<6):
        c = (int(a[i])+int(b[i]))/2
        listamedia.insert(i, c)
        i+1
    print(listamedia)
    return listamedia


def calcoli(energiaAnnua,consumoA,incandescenza, mercurio, ioduri , sodioAlta, sodioBassa, led):
    niI = 1 / 3.9
    niMerc = 1 / 11.48
    niMH = 1 / 18.37
    niSAP = 1 / 21.82
    niSBP = 1 / 32.16
    niLED = 1 / 53.84
    #ore_esercizio = 4200

    val = []
    wI = (incandescenza * float(niI)) / ((incandescenza * float(niI)) + (mercurio * float(niMerc)) + (ioduri * float(niMH)) + (sodioAlta * float(niSAP)) + (sodioBassa * float(niSBP)) + (led * float(niLED)))
    val.insert(0,wI)
    wMerc = (mercurio * float(niMerc)) / ((incandescenza * float(niI)) + (mercurio * float(niMerc)) + (ioduri * float(niMH)) + (sodioAlta * float(niSAP)) + (sodioBassa * float(niSBP)) + (led * float(niLED)))
    val.insert(1,wMerc)
    wMH = (ioduri * float(niMH)) / ((incandescenza * float(niI)) + (mercurio * float(niMerc)) + (ioduri * float(niMH)) + (sodioAlta * float(niSAP)) + (sodioBassa * float(niSBP)) + (led * float(niLED)))
    val.insert(2,wMH)
    wSAP = (sodioAlta * float(niSAP)) / ((incandescenza * float(niI)) + (mercurio * float(niMerc)) + (ioduri * float(niMH)) + (sodioAlta * float(niSAP)) + (sodioBassa * float(niSBP)) + (led * float(niLED)))
    val.insert(3,wSAP)
    wSBP = (sodioBassa * float(niSBP)) / ((incandescenza * float(niI)) + (mercurio * float(niMerc)) + (ioduri * float(niMH)) + (sodioAlta * float(niSAP)) + (sodioBassa * float(niSBP)) + (led * float(niLED)))
    val.insert(4,wSBP)
    wLED = (led * float(niLED)) / ((incandescenza * float(niI)) + (mercurio * float(niMerc)) + (ioduri * float(niMH)) + (sodioAlta * float(niSAP)) + (sodioBassa * float(niSBP)) + (led * float(niLED)))
    val.insert(5,wLED)
    print(val)

# Punto 3  energia
    e = []
    EI = energiaAnnua*wI
    e.insert(0,EI)
    EMerc = energiaAnnua*wMerc
    e.insert(1,EMerc)
    EMH = energiaAnnua*wMH
    e.insert(2, EMH)
    ESAP = energiaAnnua*wSAP
    e.insert(3, ESAP)
    ESBP = energiaAnnua*wSBP
    e.insert(4, ESBP)
    ELED = energiaAnnua*wLED
    e.insert(5, ELED)
    print('Consumo Annua:', energiaAnnua)
    print(e)


# Punto 4  potenza media
    p = []
    PI = EI/(4200*incandescenza)
    p.insert(0,PI)
    PMerc = EMerc/(4200*mercurio)
    p.insert(1, PMerc)
    PMH = EMH/(4200*ioduri)
    p.insert(2, PMH)
    PSAP = ESAP/(4200*sodioAlta)
    p.insert(3, PSAP)
    PSBP = ESBP/(4200*sodioBassa)
    p.insert(4, PSBP)
    PLED = ELED/(4200*led)
    p.insert(5, PLED)
    print('Stima della potenza media dei singoli punti luce per ogni tecnologia ')
    print(p)

# punto 5
    energiaAnnuaSenzaLed = energiaAnnua-ELED
    print(energiaAnnuaSenzaLed, 'senza LED')



    # wI = (incandescenza * (1 / niI) / (
    #             incandescenza * (1 / niI) + mercurio * (1 / niMerc) + ioduri * (1 / niMH) + sodioAlta * (
    #                 1 / niSAP) + sodioBassa * (1 / niSBP) + Led * (1 / niLED)))
    # wMerc = (mercurio * (1 / niMerc) / (
    #             incandescenza * (1 / niI) + mercurio * (1 / niMerc) + ioduri * (1 / niMH) + sodioAlta * (
    #                 1 / niSAP) + sodioBassa * (1 / niSBP) + Led * (1 / niLED)))
    # wMH = (ioduri * (1 / niMH) / (
    #             incandescenza * (1 / niI) + mercurio * (1 / niMerc) + ioduri * (1 / niMH) + sodioAlta * (
    #                 1 / niSAP) + sodioBassa * (1 / niSBP) + Led * (1 / niLED)))
    # wSAP = (sodioAlta * (1 / niSAP) / (
    #             incandescenza * (1 / niI) + mercurio * (1 / niMerc) + ioduri * (1 / niMH) + sodioAlta * (
    #                 1 / niSAP) + sodioBassa * (1 / niSBP) + Led * (1 / niLED)))
    # wSBP = (sodioBassa * (1 / niSBP) / (
    #             incandescenza * (1 / niI) + mercurio * (1 / niMerc) + ioduri * (1 / niMH) + sodioAlta * (
    #                 1 / niSAP) + sodioBassa * (1 / niSBP) + Led * (1 / niLED)))
    # wLED = (Led * (1 / niLED) / (
    #         incandescenza * (1 / niI) + mercurio * (1 / niMerc) + ioduri * (1 / niMH) + sodioAlta * (
    #         1 / niSAP) + sodioBassa * (1 / niSBP) + Led * (1 / niLED)))
    return p


if __name__ == "__main__":
    # app.debug = True
    # app.run()
    if os.environ.get('APP_LOCATION') == 'heroku':
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        app.run(debug=True)
    # app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))

