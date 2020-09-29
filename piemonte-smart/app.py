import json
import time
import os
import numpy as np
import math, numpy
math.isnan(numpy.nan)


from flask import Flask, render_template, redirect, url_for, Response, jsonify, request, flash, make_response, session
import MySQLdb
import pandas as pd
import copy
from IPython.display import clear_output

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

#conection to database
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# db = SQLAlchemy(app)

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
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    # db = SQLAlchemy(app)

    if os.environ.get('APP_LOCATION') == 'heroku':
        db = MySQLdb.connect(user='tifalwvetzrmls',
                             password='fff92d7f221799f27cccfea3bccde5e96a8806441ca4884afaeb2b658defc004',
                             host='ec2-18-203-62-227.eu-west-1.compute.amazonaws.com:5432',
                             database='dbthqgdql3bkk')
    else:
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

        consumoAnnuale2019 = request.form['consumoAnnuale2019']
        costoAnnuale2019 = request.form['costoAnnuale2019']
        totPuntiLuce2019 = request.form['puntiLuce2019']
        totIncandescenza2019 = request.form['incandescenza2019']
        totMercurio2019 = request.form['mercurio2019']
        totAlogenuri2019 = request.form['alogenuriIoduriMetallici2019']
        totSodioBassa2019 = request.form['sodio2019']
        totSodioAlta2019 = request.form['sodio22019']
        totLed2019= request.form['led2019']
        totPuntiLuceDivisi2015 = int(totIncandescenza2015) + int(totMercurio2015) + int(totAlogenuri2015) + int(totSodioBassa2015) + int(
            totSodioAlta2015) + int(totLed2015)
        totPuntiLuceDivisi2016 = int(totIncandescenza2016) + int(totMercurio2016) + int(totAlogenuri2016) + int(
            totSodioBassa2016) + int(
            totSodioAlta2016) + int(totLed2016)
        totPuntiLuceDivisi2019 = int(totIncandescenza2019) + int(totMercurio2019) + int(totAlogenuri2019) + int(
            totSodioBassa2019) + int(totSodioAlta2019) + int(totLed2019)
        lista2015 = [totIncandescenza2015,totMercurio2015,totAlogenuri2015,totSodioBassa2015,totSodioAlta2015,totLed2015]
        lista2016 = [totIncandescenza2016,totMercurio2016,totAlogenuri2016,totSodioBassa2016,totSodioAlta2016,totLed2016]
        lista2019 = [totIncandescenza2019,totMercurio2019,totAlogenuri2019,totSodioBassa2019,totSodioAlta2019,totLed2019]

        print(lista2015,lista2016,lista2019,'entrato 15+16+19')
        if int(totPuntiLuce2015) == totPuntiLuceDivisi2015 and int(totPuntiLuce2016) == totPuntiLuceDivisi2016 and int(totPuntiLuce2019) == totPuntiLuceDivisi2019:
            sql2015 = 'INSERT IGNORE INTO dati(idComune, ConsumoAnnuale15, CostoAnnuale15, PuntiLuce15, Incandescenza15, Mercurio15, Ioduri15, sodioAlta15, sodioBassa15, Led15, ConsumoAnnuale16, CostoAnnuale16, PuntiLuce16, Incandescenza16, Mercurio16, Ioduri16, sodioAlta16, sodioBassa16, Led16, ConsumoAnnuale19, CostoAnnuale19, PuntiLuce19, Incandescenza19, Mercurio19, Ioduri19, sodioAlta19, sodioBassa19, Led19) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'


            cur.execute(sql2015, [id, consumoAnnuale2015, costoAnnuale2015, totPuntiLuce2015, totIncandescenza2015, totMercurio2015, totAlogenuri2015,totSodioBassa2015, totSodioAlta2015, totLed2015,
                                      consumoAnnuale2016, costoAnnuale2016, totPuntiLuce2016, totIncandescenza2016, totMercurio2016, totAlogenuri2016,totSodioBassa2016, totSodioAlta2016, totLed2016,
                                      consumoAnnuale2019, costoAnnuale2019, totPuntiLuce2019, totIncandescenza2019,totMercurio2019, totAlogenuri2019,totSodioBassa2019, totSodioAlta2019, totLed2019])

            db.commit()

            ##Davide##
            tecnologie = ['Incandescenza ', 'Mercurio alta pressione ', 'Ioduri e Alogenuri Metallici (MH) ',
                          'Sodio ad alta pressione (SAP) ', 'Sodio a bassa pressione (SBP) ', 'LED']
            eta_ = [[3.90456, 11.484, 18.3744, 21.8196, 32.1552, 53.8384]]
            eta = pd.DataFrame(data=eta_, columns=tecnologie)
            anni = [2015, 2016, 2019]
            ore_esercizio = 4200

            # 1 - Ricezione dati di input
            consumi, puntiluce, spesa = input_dati(anni, tecnologie,consumoAnnuale2015,costoAnnuale2015,totPuntiLuce2015,lista2015,consumoAnnuale2016,costoAnnuale2016,totPuntiLuce2016,lista2016,consumoAnnuale2019,costoAnnuale2019,totPuntiLuce2019,lista2019)
            print('consumi',consumi)
            print('puntiluce', puntiluce)
            print('spesa', spesa)

            # 2 - Calcolo pesi
            Pesi = calcola_pesi(anni, tecnologie, eta, puntiluce)

            # 3 - Calcolo ripartizione consumi
            ripartizione_consumi = calcola_ripartizione_consumi(tecnologie, Pesi, consumi)

            # 4 - Calcolo potenza media
            potenza_media = calcola_potenza_media(ripartizione_consumi, puntiluce)

            # 5 CALCOLO RIDUZIONE CONSUMI FRA MEDIA 205-2016 E 2019
            riduzione_consumi = calcola_riduzione_consumi(ripartizione_consumi)
            if riduzione_consumi >= 50:
                print("\nLa tua Città ha già raggiunto la riduzione del 50% dei consumi nel 2019! Complimenti!")
            else:
                # 6 - CALCOLO PUNTI LUCE DA SOSTITUIRE PER ARRIVARE A RISPARMIO = 50%
                puntiluce['TOT_no_led'] = 0;
                puntiluce['TOT_no_led'] = puntiluce.sum(axis=1) - puntiluce[
                    'LED']  # aggiungo colonna con somma dei punti luce non led

                puntiluce_2020, ripartizione_consumi_, riduzione_consumi_, flag_puntiluceinsufficienti = calcola_riduzione_50(
                    puntiluce, anni, tecnologie, eta, consumi)

                if flag_puntiluceinsufficienti == 1: print(
                    "ATTENZIONE!!!\nNumero punti luce da sostituire risulta insufficiente per poter raggiungere il risparmio energetico del 50%.\n")

                investimento, risparmioenergia, risparmio_economico_annuo, tee, spbt = print_risultati_riduzione50(
                    puntiluce,
                    puntiluce_2020,
                    ripartizione_consumi,
                    ripartizione_consumi_,
                    riduzione_consumi,
                    riduzione_consumi_)
            return render_template('output.html', comune=comune, email=email, puntiLuce=totPuntiLuce2015,
                               incandescenza=totIncandescenza2015, mercurio=totMercurio2015, ioduri=totAlogenuri2015,
                               sodioAlta=totSodioAlta2015, sodioBassa=totSodioBassa2015, led=totLed2015)
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


def calcoli(energiaAnnua,consumiA,incandescenza, mercurio, ioduri , sodioAlta, sodioBassa, led):
    niI = 1 / 3.9
    niMerc = 1 / 11.48
    niMH = 1 / 18.37
    niSAP = 1 / 21.82
    niSBP = 1 / 32.16
    niLED = 1 / 53.84
    ore_esercizio = 4200
    costo_puntoluce=700
   # costo_energia= spesa / consumiA

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
    PI = EI/(ore_esercizio*incandescenza)
    p.insert(0,PI)
    PMerc = EMerc/(ore_esercizio*mercurio)
    p.insert(1, PMerc)
    PMH = EMH/(ore_esercizio*ioduri)
    p.insert(2, PMH)
    PSAP = ESAP/(ore_esercizio*sodioAlta)
    p.insert(3, PSAP)
    PSBP = ESBP/(ore_esercizio*sodioBassa)
    p.insert(4, PSBP)
    PLED = ELED/(ore_esercizio*led)
    p.insert(5, PLED)
    print('Stima della potenza media dei singoli punti luce per ogni tecnologia ')
    print(p)

# punto 5
    energiaAnnuaSenzaLed = energiaAnnua-ELED
    print(energiaAnnuaSenzaLed, 'senza LED')

    # CALCOLO INVESTIMENTI
    led20=0
    investimento=(led20-led) * costo_puntoluce

    # # CALCOLO RISPARMIO ECONOMICO ANNUALE
    # risparmioenergia=(val - ripartizione_consumi20)
    # risparmio_economico_annuo=round(val - ripartizione_consumi20)* costo_energia
    #
    # # CALCOLO TEE (TITOLI DI EFFICIENZA ENERGETICA)
    # ripartizione_consumi20=0
    # tee=round((val-ripartizione_consumi20)*0.187 * 0.001)*200 * 5
    #
    # # CALCOLO SPBT (SIMPLE PAYBACK TIME)
    # if investimento > tee:
    #     spbt=round(investimento-tee)/costo_energia

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


####################################################                                      FUNZIONI                                     ####################################################


####################################################                             FUNZIONI PER TUTTI GLI SCENARI                               ####################################################
# def scelta_scenario():  # 1 = risparmio 50% | 2 = tutto led | 3 = risorse disponibili
#     print(
#         "CALCOLA IL TUO RISPARMIO SULL'ILLUMINAZIONE PUBBLICA\nQuesto tool ti aiuterà a stimare il risparmio energetico ed economico derivante dalla sostituzione dei vecchi punti luce dell'illuminazione pubblica con LED nonchè le risorse economiche necessarie ad effettuare la sostituzione.")
#     print("Puoi simulare 3 diversi scenari relativamente alle esigenze della tua Città:")
#     print(
#         "\nSCENARIO 1: Calcolo del numero di punti luce da sostituire a LED e le risorse economiche necessarie per ridurre i consumi della tua Città del 50%.")
#     print(
#         "SCENARIO 2: Calcolo delle risorse economiche necessarie, del risparmio energetico ed economico ottenibile convertendo a LED tutti i punti luce della tua città.")
#     print(
#         "SCENARIO 3: Partendo dalle risorse economiche che la tua Città può dedicarvi, viene calcolato il numero di punti luce che puoi convertire a LED,il risparmio energetico ed economico ottenibile per la tua Città.")
#     while True:
#         try:
#             scenario = int(input("\nInserisci il numero dello scenario che vuoi simulare:"))
#             if scenario < 1 or scenario > 3:
#                 print("Input errato, si prega di inserire un valore numerico fra 1 e 3")
#                 continue
#         except ValueError:
#             print("Input errato, si prega di inserire un valore numerico fra 1 e 3")
#             continue
#         break
#
#     return scenario


def input_dati(anni, tecnologie,consumoAnnuale2015,costoAnnuale2015,totPuntiLuce2015,lista2015,consumoAnnuale2016,costoAnnuale2016,totPuntiLuce2016,lista2016,consumoAnnuale2019,costoAnnuale2019,totPuntiLuce2019,lista2019):
    consumi = pd.DataFrame(index=anni, columns=['kWh'])
    spesa_annua = pd.DataFrame(index=anni, columns=['€'])
    puntiluce = pd.DataFrame(index=anni, columns=tecnologie)
    print(lista2015,lista2016,lista2019)
    # RICEZIONE DATI DI INPUT
    for riga, r in puntiluce.iterrows():
        i = 0
        while True:
            try:
                if riga == '2015':
                    consumi['kWh'][riga] = (float(consumoAnnuale2015.format(str(riga))))
                    spesa_annua['€'][riga] = float(costoAnnuale2015)
                    print('consumi',consumi.dtypes,'spesa',spesa_annua.dtypes)
                elif riga == '2016':
                    consumi['kWh'][riga] = float(consumoAnnuale2016)
                    spesa_annua['€'][riga] = float(costoAnnuale2016)
                    print('consumi',consumi,'spesa',spesa_annua)
                elif riga == '2019':
                    consumi['kWh'][riga] = float(consumoAnnuale2019)
                    spesa_annua['€'][riga] = float(costoAnnuale2019)
                    print('consumi',consumi,'spesa',spesa_annua)
            except ValueError:
                clear_output(wait=True)
                print("Input errato, si prega di inserire valori numerici")
                continue
            break
        for columns in puntiluce:
            while True:
                try:
                    if riga == '2015':
                        puntiluce[columns][riga] = float(lista2015[i])
                        print('puntiluce',puntiluce)
                        i+=1
                    elif riga == '2016':
                        puntiluce[columns][riga] = float(lista2016[i])
                        print('puntiluce',puntiluce)
                        i+=1
                    elif riga == '2019':
                        puntiluce[columns][riga] = float(lista2019[i])
                        print('puntiluce',puntiluce)
                        i+=1
                except ValueError:
                    print("Input errato, si prega di inserire valori numerici")
                    continue
                break
    return consumi, puntiluce, spesa_annua


# CALCOLO PESI
def calcola_pesi(anni, tecnologie, eta, puntiluce):
    pesi = 1 / eta
    Pesi = ripartizione_consumi = pd.DataFrame(index=anni, columns=tecnologie)

    for riga, r in Pesi.iterrows():
        for columns in Pesi:
            Pesi[columns][riga] = int(puntiluce[columns][riga]) * pesi[columns][0]
    Pesi["somma"] = Pesi.sum(axis=1)
    return Pesi


def calcola_ripartizione_consumi(tecnologie, Pesi, consumi):
    # CALCOLO RIPARTIZIONE CONSUMI
    ripartizione_consumi = pd.DataFrame(index=[2015, 2016, 20152016, 2019], columns=tecnologie)
    for riga, r in ripartizione_consumi.iterrows():
        for columns in ripartizione_consumi:
            if riga == 2015 or riga == 2016 or riga == 2019:
                ripartizione_consumi[columns][riga] = (Pesi[columns][riga] * float(consumi['kWh'][riga])) / \
                                                      Pesi['somma'][riga]
            elif riga == 20152016:
                ripartizione_consumi[columns][riga] = (ripartizione_consumi[columns][2015] +
                                                       ripartizione_consumi[columns][2016]) / 2
    # CALCOLO SOMMA RIPARTIZIONE CONSUMI
    ripartizione_consumi['TOT_no_led'] = 0
    ripartizione_consumi['TOT_no_led'] = ripartizione_consumi.sum(axis=1) - ripartizione_consumi['LED']
    return ripartizione_consumi


def calcola_potenza_media(ripartizione_consumi, puntiluce):
    # CALCOLO POTENZA MEDIA
    potenza_media = pd.DataFrame(index=anni, columns=tecnologie)
    for riga, r in potenza_media.iterrows():
        for columns in potenza_media:
            if int(puntiluce[columns][riga]) > 0:
                potenza_media[columns][riga] = ripartizione_consumi[columns][riga] / ore_esercizio / 1000 / int(
                    puntiluce[columns][riga]) * 1000000
            else:
                potenza_media[columns][riga] = 0
    return potenza_media


####################################################                             FUNZIONI PER SCENARIO 1                             ####################################################
def calcola_ripartizione_consumi_2020(tecnologie, Pesi, consumi, puntiluce, potenza_media):
    # CALCOLO RIPARTIZIONE CONSUMI
    ripartizione_consumi = pd.DataFrame(index=[2015, 2016, 20152016, 2019], columns=tecnologie)
    for riga, r in ripartizione_consumi.iterrows():
        for columns in ripartizione_consumi:
            if riga == 2015 or riga == 2016 or riga == 2019:
                ripartizione_consumi[columns][riga] = (Pesi[columns][riga] * float(consumi['kWh'][riga])) / \
                                                      Pesi['somma'][riga]
            elif riga == 20152016:
                ripartizione_consumi[columns][riga] = (ripartizione_consumi[columns][2015] +
                                                       ripartizione_consumi[columns][2016]) / 2
    for riga, r in ripartizione_consumi.iterrows():
        if riga == 2019:
            for columns in ripartizione_consumi:
                ripartizione_consumi[columns][riga] = puntiluce[columns][riga] * potenza_media[columns][
                    riga] * ore_esercizio / 1000

    # CALCOLO SOMMA RIPARTIZIONE CONSUMI
    ripartizione_consumi['TOT_no_led'] = 0
    ripartizione_consumi['TOT_no_led'] = ripartizione_consumi.sum(axis=1) - ripartizione_consumi['LED']
    return ripartizione_consumi


def calcola_riduzione_consumi(ripartizione_consumi):
    riduzione_consumi = (1 - (
                ripartizione_consumi['TOT_no_led'][2019] / ripartizione_consumi['TOT_no_led'][20152016])) * 100
    return round(riduzione_consumi, 3)


def calcola_riduzione_50(puntiluce, anni, tecnologie, eta, consumi):
    puntiluce_2020 = copy.deepcopy(puntiluce)
    puntiluce_2020.drop(columns='TOT_no_led', inplace=True)
    riduzione_consumi_ = 0
    flag_puntiluceinsufficienti = 0

    for i in range(1, int(puntiluce['TOT_no_led'][
                              2019]) + 1):  # possono essere sostituiti al massimo il numero di lampioni non led presenti al 2019
        for columns in puntiluce_2020:
            if columns == 'LED': break
            for j in range(1, int(puntiluce[columns][
                                      2019]) + 1):  # per ogni tecnologia posso sostituire al massimo in numero di lampioni presenti al 2019
                puntiluce_2020[columns][2019] -= 1
                puntiluce_2020['LED'][2019] += 1
                Pesi_ = calcola_pesi(anni, tecnologie, eta, puntiluce_2020)
                ripartizione_consumi_ = calcola_ripartizione_consumi_2020(tecnologie, Pesi_, consumi, puntiluce_2020,
                                                                          potenza_media)
                riduzione_consumi_ = calcola_riduzione_consumi(ripartizione_consumi_)
                if riduzione_consumi_ > 50: break
            if riduzione_consumi_ > 50: break
        if riduzione_consumi_ > 50: break

    if i == int(puntiluce['TOT_no_led'][
                    2019]) and riduzione_consumi_ < 50: flag_puntiluceinsufficienti = 1  # SE SI ARRIVA ALLA FINE DEL CICLO E LA RIDUZIONE CONSUMI è < 50% > ATTIVO FLAG

    return puntiluce_2020, ripartizione_consumi_, riduzione_consumi_, flag_puntiluceinsufficienti


def print_risultati_riduzione50(puntiluce, puntiluce_2020, ripartizione_consumi, ripartizione_consumi_,
                                riduzione_consumi, riduzione_consumi_):
    # CALCOLO PARAMETRI DELLO SCENARIO
    costo_puntoluce = 700
    # costo_energia = 0.2
    costo_energia = spesa['€'][2019] / consumi['kWh'][2019]

    # CALCOLO INVESTIMENTI
    investimento = costo_puntoluce * int(puntiluce_2020['LED'][2019] - puntiluce['LED'][2019])
    # CALCOLO RISPARMIO ECONOMICO ANNUALE
    ripartizione_consumi['TOT'] = 0;
    ripartizione_consumi_['TOT'] = 0
    ripartizione_consumi['TOT'] = ripartizione_consumi.sum(axis=1) - ripartizione_consumi['TOT_no_led']
    ripartizione_consumi_['TOT'] = ripartizione_consumi_.sum(axis=1) - ripartizione_consumi_['TOT_no_led']

    risparmioenergia = round(ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019])
    risparmio_economico_annuo = round(
        (ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019]) * costo_energia)
    # CALCOLO TEE (TITOLI DI EFFICIENZA ENERGETICA)
    tee = round(((ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019]) * 0.187 * 0.001)) * 200 * 5
    # CALCOLO SPBT (SIMPLE PAYBACK TIME)
    if investimento > tee:
        spbt = round((investimento - tee) / risparmio_economico_annuo, 2)

    # PRINT
    print("\nRiduzione consumi fra media 2015-2016 e 2019: {0} %".format(riduzione_consumi))
    print("Per arrivare ad un risparmio del 50% occorre sostituire:")
    for columns in puntiluce_2020:
        if puntiluce_2020[columns][2019] < puntiluce[columns][2019]:
            print("{0} punti luce con tecnologia {1}".format(
                int((puntiluce[columns][2019] - puntiluce_2020[columns][2019])), columns))
    print("\nRiduzione consumo energetico: {0} %".format(riduzione_consumi_))
    print("Investimento necessario: {0} €".format(investimento))
    print("Risparmio energetico: {0} kWh".format(risparmioenergia))
    print("Risparmio economico annuo: {0} €".format(risparmio_economico_annuo))
    print("TEE: {0} €".format(tee))
    print("Simple Pay Back Time: {0} anni".format(spbt))

    return investimento, risparmioenergia, risparmio_economico_annuo, tee, spbt


####################################################                             FUNZIONI PER SCENARIO 2                             ####################################################
def calcola_ripartizione_consumi_tuttoled(anni, tecnologie, Pesi, consumi):
    # CALCOLO RIPARTIZIONE CONSUMI
    ripartizione_consumi = pd.DataFrame(index=anni, columns=tecnologie)
    for riga, r in ripartizione_consumi.iterrows():
        for columns in ripartizione_consumi:
            ripartizione_consumi[columns][riga] = (Pesi[columns][riga] * float(consumi['kWh'][riga])) / Pesi['somma'][
                riga]
    # CALCOLO SOMMA RIPARTIZIONE CONSUMI
    ripartizione_consumi['TOT'] = 0
    ripartizione_consumi['TOT'] = ripartizione_consumi.sum(axis=1)
    return ripartizione_consumi


def calcola_ripartizione_consumi_tuttoled_2020(anni, tecnologie, Pesi, consumi, puntiluce, potenza_media):
    # CALCOLO RIPARTIZIONE CONSUMI
    ripartizione_consumi = pd.DataFrame(index=anni, columns=tecnologie)

    for riga, r in ripartizione_consumi.iterrows():
        for columns in ripartizione_consumi:
            ripartizione_consumi[columns][riga] = puntiluce[columns][riga] * potenza_media[columns][
                riga] * ore_esercizio / 1000

    # CALCOLO SOMMA RIPARTIZIONE CONSUMI
    ripartizione_consumi['TOT'] = 0
    ripartizione_consumi['TOT'] = ripartizione_consumi.sum(axis=1)
    return ripartizione_consumi


def calcola_riduzione_tuttoled(puntiluce, anni, tecnologie, eta, consumi):
    puntiluce_2020 = copy.deepcopy(puntiluce)
    for columns in puntiluce_2020:
        if columns == 'LED':
            puntiluce_2020[columns][2019] += puntiluce_2020['TOT_no_led'][2019]
        elif columns == 'TOT_no_led':
            continue
        else:
            puntiluce_2020[columns][2019] = 0
    puntiluce_2020.drop(columns='TOT_no_led', inplace=True)

    Pesi_ = calcola_pesi(anni, tecnologie, eta, puntiluce_2020)
    ripartizione_consumi_ = calcola_ripartizione_consumi_tuttoled_2020(anni, tecnologie, Pesi_, consumi, puntiluce_2020,
                                                                       potenza_media)
    return puntiluce_2020, ripartizione_consumi_


def calcola_riduzione_consumi_tuttoled(ripartizione_consumi, ripartizione_consumi_):
    riduzione_consumi = (1 - (ripartizione_consumi_['TOT'][2019] / ripartizione_consumi['TOT'][2019])) * 100
    return round(riduzione_consumi, 3)


def print_risultati_tuttoled(puntiluce, puntiluce_2020, ripartizione_consumi, ripartizione_consumi_, riduzione_consumi):
    # CALCOLO PARAMETRI DELLO SCENARIO
    costo_puntoluce = 700
    # costo_energia = 0.2
    costo_energia = spesa['€'][2019] / consumi['kWh'][2019]

    # CALCOLO INVESTIMENTI
    investimento = costo_puntoluce * int(puntiluce_2020['LED'][2019] - puntiluce['LED'][2019])
    # CALCOLO RISPARMIO ECONOMICO ANNUALE
    risparmioenergia = round(ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019])
    risparmio_economico_annuo = round(
        (ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019]) * costo_energia)
    # CALCOLO TEE (TITOLI DI EFFICIENZA ENERGETICA)
    tee = round(((ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019]) * 0.187 * 0.001)) * 200 * 5
    # CALCOLO SPBT (SIMPLE PAYBACK TIME)
    if investimento > tee:
        spbt = round((investimento - tee) / risparmio_economico_annuo, 2)
    else:
        spbt = 0

    # PRINT
    print(
        "\nRiduzione consumo energetico  ottenibile convertendo a LED tutti i punti luce della tua città: {0} %".format(
            riduzione_consumi))
    print("I punti luce da convertire sono {}".format(int(puntiluce['TOT_no_led'][2019])))
    print("Investimento necessario: {0} €".format(investimento))
    print("Risparmio energetico: {0} kWh".format(int(risparmioenergia)))
    print("Risparmio economico annuo: {0} €".format(int(risparmio_economico_annuo)))
    print("TEE: {0} €".format(int(tee)))
    print("Simple Pay Back Time: {0} anni".format(spbt))

    return investimento, risparmioenergia, risparmio_economico_annuo, tee, spbt


####################################################                             FUNZIONI PER SCENARIO 3                             ####################################################
def calcola_ripartizione_consumi_rd(anni, tecnologie, Pesi, consumi):
    # CALCOLO RIPARTIZIONE CONSUMI
    ripartizione_consumi = pd.DataFrame(index=anni, columns=tecnologie)
    for riga, r in ripartizione_consumi.iterrows():
        for columns in ripartizione_consumi:
            ripartizione_consumi[columns][riga] = (Pesi[columns][riga] * float(consumi['kWh'][riga])) / Pesi['somma'][
                riga]
    # CALCOLO SOMMA RIPARTIZIONE CONSUMI
    ripartizione_consumi['TOT'] = 0
    ripartizione_consumi['TOT'] = ripartizione_consumi.sum(axis=1)
    return ripartizione_consumi


def calcola_ripartizione_consumi_rd_2020(anni, tecnologie, Pesi, consumi, puntiluce, potenza_media):
    # CALCOLO RIPARTIZIONE CONSUMI
    ripartizione_consumi = pd.DataFrame(index=anni, columns=tecnologie)

    for riga, r in ripartizione_consumi.iterrows():
        for columns in ripartizione_consumi:
            ripartizione_consumi[columns][riga] = puntiluce[columns][riga] * potenza_media[columns][
                riga] * ore_esercizio / 1000

    # CALCOLO SOMMA RIPARTIZIONE CONSUMI
    ripartizione_consumi['TOT'] = 0
    ripartizione_consumi['TOT'] = ripartizione_consumi.sum(axis=1)
    return ripartizione_consumi


def calcola_puntiluce_da_sostituire_rd(puntiluce, anni, tecnologie, eta, consumi, puntiluce_sostituibili):
    puntiluce_sostituiti = 0
    puntiluce_2020 = copy.deepcopy(puntiluce)
    puntiluce_2020.drop(columns='TOT_no_led', inplace=True)

    while True:
        for columns in puntiluce_2020:
            if columns == 'LED': break
            for j in range(1, int(puntiluce[columns][
                                      2019]) + 1):  # per ogni tecnologia posso sostituire al massimo in numero di lampioni presenti al 2019
                puntiluce_2020[columns][2019] -= 1
                puntiluce_2020['LED'][2019] += 1
                puntiluce_sostituiti += 1
                if puntiluce_sostituiti == puntiluce_sostituibili: break  # possono essere sostituiti al massimo il numero di lampioni pari a "puntiluce_sostituibili"
            if puntiluce_sostituiti == puntiluce_sostituibili: break
        if puntiluce_sostituiti == puntiluce_sostituibili: break

    Pesi_ = calcola_pesi(anni, tecnologie, eta, puntiluce_2020)
    ripartizione_consumi_ = calcola_ripartizione_consumi_rd_2020(anni, tecnologie, Pesi_, consumi, puntiluce_2020,
                                                                 potenza_media)
    riduzione_consumi = calcola_riduzione_consumi_tuttoled(ripartizione_consumi, ripartizione_consumi_)

    return puntiluce_2020, ripartizione_consumi_, riduzione_consumi


def print_risultati_rd(puntiluce, puntiluce_2020, ripartizione_consumi, ripartizione_consumi_, riduzione_consumi,
                       risorse_usate, puntiluce_sostituibili):
    # CALCOLO PARAMETRI DELLO SCENARIO
    # costo_energia = 0.2
    costo_energia = spesa['€'][2019] / consumi['kWh'][2019]

    # CALCOLO RISPARMIO ECONOMICO ANNUALE
    risparmioenergia = round(ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019])
    risparmio_economico_annuo = round(
        (ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019]) * costo_energia)
    # CALCOLO TEE (TITOLI DI EFFICIENZA ENERGETICA)
    tee = round(((ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019]) * 0.187 * 0.001)) * 200 * 5
    # CALCOLO SPBT (SIMPLE PAYBACK TIME)
    if risorse_usate > tee:
        spbt = round((risorse_usate - tee) / risparmio_economico_annuo, 2)
    else:
        spbt = 0

    # PRINT
    print("I punti luce LED acquistabili sono {}".format(int(puntiluce_sostituibili)))
    print("I punti luce da sostituire sono:")
    for columns in puntiluce_2020:
        if puntiluce_2020[columns][2019] < puntiluce[columns][2019]:
            print("     {0} con tecnologia {1}".format(int((puntiluce[columns][2019] - puntiluce_2020[columns][2019])),
                                                       columns))
    print("Riduzione consumo energetico: {0} %".format(riduzione_consumi))
    print("Investimento: {0} €".format(risorse_usate))
    print("Risparmio energetico: {0} kWh".format(int(risparmioenergia)))
    print("Risparmio economico annuo: {0} €".format(int(risparmio_economico_annuo)))
    print("TEE: {0} €".format(int(tee)))
    print("Simple Pay Back Time: {0} anni".format(spbt))

    return risparmioenergia, risparmio_economico_annuo, tee, spbt


########################################################################################################################################################################################
####################################################                                      MAIN                                      ####################################################

##########################                   DATI                   ##########################
tecnologie = ['Incandescenza ', 'Mercurio alta pressione ', 'Ioduri e Alogenuri Metallici (MH) ',
              'Sodio ad alta pressione (SAP) ', 'Sodio a bassa pressione (SBP) ', 'LED']
eta_ = [[3.90456, 11.484, 18.3744, 21.8196, 32.1552, 53.8384]]
eta = pd.DataFrame(data=eta_, columns=tecnologie)
anni = [2015, 2016, 2019]
ore_esercizio = 4200

##########################                   SCELTA SCENARIO DA SIMULARE                   ##########################
#scenario = scelta_scenario()

# if scenario == 1:
#     ####################################################                                      SCENARIO RISPARMIO 50 %                                      ####################################################
#
#     ##########################                   MAIN                   ##########################
#     tecnologie = ['Incandescenza ', 'Mercurio alta pressione ', 'Ioduri e Alogenuri Metallici (MH) ',
#                   'Sodio ad alta pressione (SAP) ', 'Sodio a bassa pressione (SBP) ', 'LED']
#     eta_ = [[3.90456, 11.484, 18.3744, 21.8196, 32.1552, 53.8384]]
#     eta = pd.DataFrame(data=eta_, columns=tecnologie)
#     anni = [2015, 2016, 2019]
#     ore_esercizio = 4200
#
#     # 1 - Ricezione dati di input
#     consumi, puntiluce, spesa = input_dati(anni, tecnologie)
#
#     # 2 - Calcolo pesi
#     Pesi = calcola_pesi(anni, tecnologie, eta, puntiluce)
#
#     # 3 - Calcolo ripartizione consumi
#     ripartizione_consumi = calcola_ripartizione_consumi(tecnologie, Pesi, consumi)
#
#     # 4 - Calcolo potenza media
#     potenza_media = calcola_potenza_media(ripartizione_consumi, puntiluce)
#
#     # 5 CALCOLO RIDUZIONE CONSUMI FRA MEDIA 205-2016 E 2019
#     riduzione_consumi = calcola_riduzione_consumi(ripartizione_consumi)
#     if riduzione_consumi >= 50:
#         print("\nLa tua Città ha già raggiunto la riduzione del 50% dei consumi nel 2019! Complimenti!")
#     else:
#         # 6 - CALCOLO PUNTI LUCE DA SOSTITUIRE PER ARRIVARE A RISPARMIO = 50%
#         puntiluce['TOT_no_led'] = 0;
#         puntiluce['TOT_no_led'] = puntiluce.sum(axis=1) - puntiluce[
#             'LED']  # aggiungo colonna con somma dei punti luce non led
#
#         puntiluce_2020, ripartizione_consumi_, riduzione_consumi_, flag_puntiluceinsufficienti = calcola_riduzione_50(
#             puntiluce, anni, tecnologie, eta, consumi)
#
#         if flag_puntiluceinsufficienti == 1: print(
#             "ATTENZIONE!!!\nNumero punti luce da sostituire risulta insufficiente per poter raggiungere il risparmio energetico del 50%.\n")
#
#         investimento, risparmioenergia, risparmio_economico_annuo, tee, spbt = print_risultati_riduzione50(puntiluce,
#                                                                                                            puntiluce_2020,
#                                                                                                            ripartizione_consumi,
#                                                                                                            ripartizione_consumi_,
#                                                                                                            riduzione_consumi,
#                                                                                                            riduzione_consumi_)
#
# if scenario == 2:
#     ####################################################                                      SCENARIO TUTTO LED                                     ####################################################
#     anni = [2019]
#
#     # 1 - Ricezione dati di input
#     consumi, puntiluce, spesa = input_dati(anni, tecnologie)
#
#     # 2 - Calcolo pesi
#     Pesi = calcola_pesi(anni, tecnologie, eta, puntiluce)
#
#     # 3 - Calcolo ripartizione consumi
#     ripartizione_consumi = calcola_ripartizione_consumi_tuttoled(anni, tecnologie, Pesi, consumi)
#
#     # 4 - Calcolo potenza media
#     potenza_media = calcola_potenza_media(ripartizione_consumi, puntiluce)
#
#     # 5 CONVERTO I PUNTI LUCE IN TUTTO LED E CALCOLO I CONSUMI
#     puntiluce['TOT_no_led'] = 0;
#     puntiluce['TOT_no_led'] = puntiluce.sum(axis=1) - puntiluce[
#         'LED']  # aggiungo colonna con somma dei punti luce non led
#
#     puntiluce_2020, ripartizione_consumi_ = calcola_riduzione_tuttoled(puntiluce, anni, tecnologie, eta, consumi)
#
#     # CALCOLO RISPARMIO %
#     riduzione_consumi = calcola_riduzione_consumi_tuttoled(ripartizione_consumi, ripartizione_consumi_)
#
#     investimento, risparmioenergia, risparmio_economico_annuo, tee, spbt = print_risultati_tuttoled(puntiluce,
#                                                                                                     puntiluce_2020,
#                                                                                                     ripartizione_consumi,
#                                                                                                     ripartizione_consumi_,
#                                                                                                     riduzione_consumi)
#
# if scenario == 3:
#     ####################################################                                      SCENARIO RISORSE DISPONIBILI                                    ####################################################
#     anni = [2019]
#     costo_puntoluce = 700
#
#     # 1 - Ricezione dati di input
#     consumi, puntiluce, spesa = input_dati(anni, tecnologie)
#     while True:
#         risorse = (float(input("Risorse disponibili [€] : ")))
#         if risorse < costo_puntoluce:
#             print("Risorse insufficienti, inserire valore valido")
#             continue
#         else:
#             break
#
#     puntiluce_sostituibili = int(
#         risorse / costo_puntoluce)  # CALCOLO NUMERO DI PUNTI LUCE ACQUISTABILI CON LE RISORSE DATE
#     investimento = puntiluce_sostituibili * costo_puntoluce  # CALCOLO DELLA SPESA EFFETTIVA, CONSIDERATO L'ARROTONDAMENTO PER DIFETTO APPLICATO ALLA DIVISIONE risorse/costo_puntoluce
#
#     # 2 - Calcolo pesi
#     Pesi = calcola_pesi(anni, tecnologie, eta, puntiluce)
#
#     # 3 - Calcolo ripartizione consumi
#     ripartizione_consumi = calcola_ripartizione_consumi_rd(anni, tecnologie, Pesi, consumi)
#
#     # 4 - Calcolo potenza media
#     potenza_media = calcola_potenza_media(ripartizione_consumi, puntiluce)
#
#     # 5 - CALCOLO PUNTI LUCE DA SOSTITUIRE
#     puntiluce['TOT_no_led'] = 0;
#     puntiluce['TOT_no_led'] = puntiluce.sum(axis=1) - puntiluce[
#         'LED']  # aggiungo colonna con somma dei punti luce non led
#     if puntiluce_sostituibili > puntiluce['TOT_no_led'][2019]:
#         puntiluce_sostituibili = puntiluce['TOT_no_led'][
#             2019]  # SE SI POSSONO ACQUISTARE PIù PUNTI LUCE LED DI QUANTI PUNTI LUCE NON_LED SONO PRESENTI, IL LIMITE DIVENTA IL NUMERO DI PUNTI LUCE NON_LED
#         investimento = puntiluce_sostituibili * costo_puntoluce
#
#     puntiluce_2020, ripartizione_consumi_, riduzione_consumi_ = calcola_puntiluce_da_sostituire_rd(puntiluce, anni,
#                                                                                                    tecnologie, eta,
#                                                                                                    consumi,
#                                                                                                    puntiluce_sostituibili)
#
#     risparmioenergia, risparmio_economico_annuo, tee, spbt = print_risultati_rd(puntiluce, puntiluce_2020,
#                                                                                 ripartizione_consumi,
#                                                                                 ripartizione_consumi_,
#                                                                                 riduzione_consumi_, investimento,
#                                                                                 puntiluce_sostituibili)

if __name__ == "__main__":
    # app.debug = True
    # app.run()
    if os.environ.get('APP_LOCATION') == 'heroku':
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        app.run(debug=True)
    # app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))

