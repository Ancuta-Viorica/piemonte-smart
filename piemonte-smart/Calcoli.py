import math
import datetime
from math import factorial
import numpy
from decimal import *
#today = datetime.date.today()

######################################### RUDUZIONE 50 ######################################
import self as self


class Riduzione50():
    inp=(str(input("Tipologia l'illuminazione: ")))

    if inp != 'led':
        downLightOutputRatio = 0.8
        perditaEfficienzaLuminosa = 0.6
        utilizzo = 0.55
        efficienzaAlimentatore = 0.87
    else:
        downLightOutputRatio = 0.95
        perditaEfficienzaLuminosa = 0.8
        utilizzo = 0.7
        efficienzaAlimentatore = 0.88

    def tipologia(inp):
        switcher = {
            'incandescenza': 17,
            'mercurio': 50,
            'ioduriAlogenuriMetallici': 80,
            'sodioAltaPressione': 95,
            'sodioBassaPressione': 140,
            'led': 115
        }
        efficienzaLuminosa = switcher[inp]
        return efficienzaLuminosa

    puntiLuce = int(input("Punti Luce:" ))
    energiaTotale = int()
    efficienzaLuminosa = tipologia(inp)


#1. Stima efficienza complessiva media 𝜼_𝑖  per ogni tecnologia
    # di punto luce a partire dall’efficienza luminosa media
    # utilizzando la relazione(*):

    totale = efficienzaLuminosa * downLightOutputRatio * \
             perditaEfficienzaLuminosa * utilizzo * efficienzaAlimentatore
    print("totale RUDUZIONE: ", totale)

# 2. Definizione di pesi per la ripartizione dei consumi totali
    # per ogni tecnologia «i» in funzione del numero di punti luce 𝑁_𝑖
    # e dell’efficienza complessiva 𝜂_𝑖  :

    print("--------Consimi 2015-------------")

    def PesiRipartizione15(totale, puntiLuce):      ###### def 15
        # if totaleInc == 0 and puntiLuce == 0:
        #     return 1
        # else:
            n=(puntiLuce * (1 / totale))
            print("pesi ",n)
            # Ni =range (6)
            # for i in (Ni):
            #     print (i)
            #ni = [3.9, 11.5, 18.4, 21.8, 32.2, 53.8]
            ### for i in float(n):
            ###     print("tot pesi:",type(i))

            #pesiTot=9.01575752

           ##### return somma(n)/float(len(n)

            # out = 0
            # for k in range(len(totale)):
            #     out += totale[k] * puntiLuce[k]
            # return out
            # # out=d0(v1,v2)
            # print("outt", out)

            # risultato = 0
            # tot = puntiLuce * (1 / totale)
            # tot += risultato
            # w = n / (tot) # ????
            w=n
            return w

    w = PesiRipartizione15(totale, puntiLuce)
    print("Ripartizione consumi 2015",w)

    # def pesi(totale, puntiLuce):
    #     risultato=0
    #     tot=puntiLuce*(1/totale)
    #     tot+=risultato
    #     print(tot)


    #
    # def somma(n):
    #     risultato = 0
    #     for i in float(n):
    #         risultato += i
    #         print("‘pesi pesi:’", i)
    #     print(len("‘La somma è: ‘", risultato))




# 3. Calcolo della quota di energia da assegnare
    # ad una specifica tecnologia «i» a partire dai consumi totali:

    def calcoloQuotaEnergia( w):
        energiaTotale=0.2
        e = w * energiaTotale
        return e
    e = calcoloQuotaEnergia(w )
    print("consumi", e)

# 4. Stima della potenza media dei singoli punti
    # luce per ogni tecnologia «i» considerando un numero di ore di esercizio annue pari a 4200

    def stimaPotenziaMedia(e,puntiLuce):
        p = e/(4200 * puntiLuce)
        return p
    p = stimaPotenziaMedia(e,puntiLuce)
    print("potenzia Media", p)

# 5. Calcolo dei consumi di energia per illuminazione
    # pubblica al netto dei consumi dovuti ai punti luce a LED:

    # def sommaTotaleConsumiLed(energiaTotale,e, puntiLuce):
    #     w=65648,8406
    #     ledTot =w * e
    #
    #     tot= ledTot - energiaTotale + puntiLuce
    #
    #     return tot
    #
    #     ##solo Led
    #     ##Somma Consumi None
    #     # def sommaTotaleConsumiLed(tipologia, energiaTotale, e, puntiLuce):
    #     # inp = 'led'
    #     # w = 65648, 8406
    #     # if tipologia(inp) == inp:
    #     #     ledTot = w * e - energiaTotale + puntiLuce
    #     #     print("Led", ledTot)
    #     #     return ledTot
    #     # else:
    #     #     print("solo Led")
    #
    #
    #     # if  tipologia(inp)!= inp:
    #     #     print("solo Led")
    #     # else:
    #     #     ledTot = e - energiaTotale + puntiLuce
    #     #
    #     #     return ledTot
    #
    # tot = sommaTotaleConsumiLed(energiaTotale,e, puntiLuce)
    # print("Somma Consumi", tot)

# 6. Calcolo dei consumi medi per illuminazione pubblica
    # al netto dei consumi dovuti ai punti luce a LED
    # per il periodo 2015/2016:

    def mediLuminosa(self, energiaTotale16,energiaTotale15):
        e56 = (energiaTotale16 + energiaTotale15)/2
        return e56

# 7. Calcolo della variazione dei consumi per illuminazione pubblica
    # (al netto dei consumi dovuti ai punti luce a LED)
    # tra il 2019 e la media del periodo 2015/2016:
    def variazioneluminosa(self,e56, e19):
        deltaEnergiaTotale=1-(e19/e56)
        return deltaEnergiaTotale

# 8. Calcolo del numero di punti luce da sostituire con tecnologia a LED,
    # rispetto ai punti luce 2019, per raggiungere 〖∆𝐸〗_(𝑡𝑜𝑡−𝐿𝐸𝐷)≥0.5 mediante
    # macro Excel, utilizzando la potenza media 𝑃_𝑖 calcolata
    # al punto 4. Sostituzione dei punti luce a partire da quelli con tecnologia
    # a minore efficienza complessiva (Incandescenza, Mercurio alta pressione, etc.).
# 8. Stima dell’investimento necessario alla sostituzione dei punti luce
    # considerando un costo medio di circa 700€(*) per punto luce a LED.

    def sostituire(self, totale , p,deltaEnergiaTotale): #???
        sost=p+totale
        e19=deltaEnergiaTotale >= 0.5
        (e19+p)/2
        costo=700
        inp = int(input("stima dell'investimento"))
        if inp =='led':
            investimento=(sost+costo)/2
        return investimento  #non va bene

# 9. Stima dei Titoli di Efficienza Energetica (TEE)
    # ottenibili per 5 anni a partire dal risparmio
    # conseguito sostituendo i punti luce
    # convenzionali con punti luce a tecnologia LED.

    def titoliEfficienzaEnergetica(self, puntiLuce): #??
        tee=5
        for i in range(tee+1):
            print(tee,i)
            tee-=1
        #??
       # return #?

# 10. Stima del risparmio economico annuale ottenibile
    # a partire dal risparmio energetico conseguito
    # sostituendo i punti luce convenzionali
    # con punti luce a tecnologia LED considerando un costo medio
    # per l’energia elettrica pari a 0.2€/kWh.

    def risparmioEconomicoAnnuale(self, totale):
        energetico=1
        elettrica=0.2
        for i in range(energetico+1):
            print(energetico, i)
        puntiLuce=(totale+elettrica)/2

        return puntiLuce

# 11. Stima del Simple Pay Back Time per l’investimento
# necessario alla sostituzione dei punti luce.

    def simplePayBackTime(self ):
        investimento=int()
        puntiLuce=investimento
        return puntiLuce

    print("---------------Consimi 2016--------------")

    puntiLuce = int(input('Punti Luce: '))
    energiaTotale = int()
    efficienzaLuminosa = tipologia(inp)

    def PesiRipartizione16(totale, puntiLuce):  ###### def 16
        if totale == 0 and puntiLuce == 0:
            return 1
        else:
            n = (puntiLuce * (1 / totale))
            print("pesi 2016", n)
            # Ni =range (6)
            # for i in (Ni):
            #     print (i)
            # ni = [3.9, 11.5, 18.4, 21.8, 32.2, 53.8]
            pesiTot = 6.640390519
            w = ((puntiLuce * (1 / totale)) / (pesiTot))
            return w

    w = PesiRipartizione16(totale, puntiLuce)
    print("Ripartizione consumi", w)

    # 3. Calcolo della quota di energia da assegnare
    # ad una specifica tecnologia «i» a partire dai consumi totali:

    def calcoloQuotaEnergia(w, energiaTotale):
        energiaTotale = 0.2
        e = w * energiaTotale
        return e

    e = calcoloQuotaEnergia(w, energiaTotale)
    print("consumi", e)

    # 4. Stima della potenza media dei singoli punti
    # luce per ogni tecnologia «i» considerando un numero di ore di esercizio annue pari a 4200

    def stimaPotenziaMedia(e, puntiLuce):
        p = e / (4200 * puntiLuce)
        return p

    p = stimaPotenziaMedia(e, puntiLuce)
    print("potenzia Media", p)

    # 5. Calcolo dei consumi di energia per illuminazione
    # pubblica al netto dei consumi dovuti ai punti luce a LED:

    def sommaTotaleConsumiLed(energiaTotale):
        e = energiaTotale * 5
        return e

    e = sommaTotaleConsumiLed(energiaTotale)
    print("Somma Consumi", e)

    # 6. Calcolo dei consumi medi per illuminazione pubblica
    # al netto dei consumi dovuti ai punti luce a LED
    # per il periodo 2015/2016:

    def mediLuminosa(self, energiaTotale16, energiaTotale15):
        e56 = (energiaTotale16 + energiaTotale15) / 2
        return e56

    # 7. Calcolo della variazione dei consumi per illuminazione pubblica
    # (al netto dei consumi dovuti ai punti luce a LED)
    # tra il 2019 e la media del periodo 2015/2016:
    def variazioneluminosa(self, e56, e19):
        deltaEnergiaTotale = 1 - (e19 / e56)
        return deltaEnergiaTotale

    # 8. Calcolo del numero di punti luce da sostituire con tecnologia a LED,
    # rispetto ai punti luce 2019, per raggiungere 〖∆𝐸〗_(𝑡𝑜𝑡−𝐿𝐸𝐷)≥0.5 mediante
    # macro Excel, utilizzando la potenza media 𝑃_𝑖 calcolata
    # al punto 4. Sostituzione dei punti luce a partire da quelli con tecnologia
    # a minore efficienza complessiva (Incandescenza, Mercurio alta pressione, etc.).
    # 8. Stima dell’investimento necessario alla sostituzione dei punti luce
    # considerando un costo medio di circa 700€(*) per punto luce a LED.

    def sostituire(self, totale, p, deltaEnergiaTotale):  # ???
        sost = p + totale
        e19 = deltaEnergiaTotale >= 0.5
        (e19 + p) / 2
        costo = 700
        inp = int(input("stima dell'investimento"))
        if inp == 'led':
            investimento = (sost + costo) / 2
        return investimento  # non va bene

    # 9. Stima dei Titoli di Efficienza Energetica (TEE)
    # ottenibili per 5 anni a partire dal risparmio
    # conseguito sostituendo i punti luce
    # convenzionali con punti luce a tecnologia LED.

    def titoliEfficienzaEnergetica(self, puntiLuce):  # ??
        tee = 5
        for i in range(tee + 1):
            print(tee, i)
            tee -= 1
        # ??

    # return #?

    # 10. Stima del risparmio economico annuale ottenibile
    # a partire dal risparmio energetico conseguito
    # sostituendo i punti luce convenzionali
    # con punti luce a tecnologia LED considerando un costo medio
    # per l’energia elettrica pari a 0.2€/kWh.

    def risparmioEconomicoAnnuale(self, totale):
        energetico = 1
        elettrica = 0.2
        for i in range(energetico + 1):
            print(energetico, i)
        puntiLuce = (totale + elettrica) / 2

        return puntiLuce

    # 11. Stima del Simple Pay Back Time per l’investimento
    # necessario alla sostituzione dei punti luce.

    def simplePayBackTime(self):
        investimento = int()
        puntiLuce = investimento
        return puntiLuce

    print("-------------Consimi 2019----------------")

    puntiLuce = int(input('Punti Luce: '))
    energiaTotale = int()
    efficienzaLuminosa = tipologia(inp)

    def PesiRipartizione19(totale, puntiLuce):  ###### def 19
        if totale == 0 and puntiLuce == 0:
            return 1
        else:
            n = (puntiLuce * (1 / totale))
            print("pesi 2019", n)
            # Ni =range (6)
            # for i in (Ni):
            #     print (i)
            # ni = [3.9, 11.5, 18.4, 21.8, 32.2, 53.8]
            pesiTot = 5.892754606
            w = ((puntiLuce * (1 / totale)) / (pesiTot))  # ????
            return w

    w = PesiRipartizione19(totale, puntiLuce)
    print("Ripartizione consumi", w)

    # 3. Calcolo della quota di energia da assegnare
    # ad una specifica tecnologia «i» a partire dai consumi totali:

    def calcoloQuotaEnergia(w, energiaTotale):
        energiaTotale = 0.2
        e = w * energiaTotale
        return e

    e = calcoloQuotaEnergia(w, energiaTotale)
    print("consumi", e)

    # 4. Stima della potenza media dei singoli punti
    # luce per ogni tecnologia «i» considerando un numero di ore di esercizio annue pari a 4200

    def stimaPotenziaMedia(e, puntiLuce):
        p = e / (4200 * puntiLuce)
        return p

    p = stimaPotenziaMedia(e, puntiLuce)
    print("potenzia Media", p)

    # 5. Calcolo dei consumi di energia per illuminazione
    # pubblica al netto dei consumi dovuti ai punti luce a LED:

    def sommaTotaleConsumiLed(energiaTotale):
        e = energiaTotale * 5
        return e

    e = sommaTotaleConsumiLed(energiaTotale)
    print("Somma Consumi", e)

    # 6. Calcolo dei consumi medi per illuminazione pubblica
    # al netto dei consumi dovuti ai punti luce a LED
    # per il periodo 2015/2016:

    def mediLuminosa(self, energiaTotale16, energiaTotale15):
        e56 = (energiaTotale16 + energiaTotale15) / 2
        return e56

    # 7. Calcolo della variazione dei consumi per illuminazione pubblica
    # (al netto dei consumi dovuti ai punti luce a LED)
    # tra il 2019 e la media del periodo 2015/2016:
    def variazioneluminosa(self, e56, e19):
        deltaEnergiaTotale = 1 - (e19 / e56)
        return deltaEnergiaTotale

    # 8. Calcolo del numero di punti luce da sostituire con tecnologia a LED,
    # rispetto ai punti luce 2019, per raggiungere 〖∆𝐸〗_(𝑡𝑜𝑡−𝐿𝐸𝐷)≥0.5 mediante
    # macro Excel, utilizzando la potenza media 𝑃_𝑖 calcolata
    # al punto 4. Sostituzione dei punti luce a partire da quelli con tecnologia
    # a minore efficienza complessiva (Incandescenza, Mercurio alta pressione, etc.).
    # 8. Stima dell’investimento necessario alla sostituzione dei punti luce
    # considerando un costo medio di circa 700€(*) per punto luce a LED.

    def sostituire(self, totale, p, deltaEnergiaTotale):  # ???
        sost = p + totale
        e19 = deltaEnergiaTotale >= 0.5
        (e19 + p) / 2
        costo = 700
        inp = int(input("stima dell'investimento"))
        if inp == 'led':
            investimento = (sost + costo) / 2
        return investimento  # non va bene

    # 9. Stima dei Titoli di Efficienza Energetica (TEE)
    # ottenibili per 5 anni a partire dal risparmio
    # conseguito sostituendo i punti luce
    # convenzionali con punti luce a tecnologia LED.

    def titoliEfficienzaEnergetica(self, puntiLuce):  # ??
        tee = 5
        for i in range(tee + 1):
            print(tee, i)
            tee -= 1
        # ??

    # return #?

    # 10. Stima del risparmio economico annuale ottenibile
    # a partire dal risparmio energetico conseguito
    # sostituendo i punti luce convenzionali
    # con punti luce a tecnologia LED considerando un costo medio
    # per l’energia elettrica pari a 0.2€/kWh.

    def risparmioEconomicoAnnuale(self, totale):
        energetico = 1
        elettrica = 0.2
        for i in range(energetico + 1):
            print(energetico, i)
        puntiLuce = (totale + elettrica) / 2

        return puntiLuce

    # 11. Stima del Simple Pay Back Time per l’investimento
    # necessario alla sostituzione dei punti luce.

    def simplePayBackTime(self):
        investimento = int()
        puntiLuce = investimento
        return puntiLuce


######################################## TUTTO LED ################################


class TuttoLED():
    inp = str(input("Tipologia Illuminazione TUTTO LED: "))

    if inp != 'led':
        downLightOutputRatio = 0.8
        perditaEfficienzaLuminosa = 0.6
        utilizzo = 0.55
        efficienzaAlimentatore = 0.87
    else:
        downLightOutputRatio = 0.95
        perditaEfficienzaLuminosa = 0.8
        utilizzo = 0.7
        efficienzaAlimentatore = 0.88

    def tipologia(inp):
        switcher = {
            'incandescenza': 17,
            'mercurio': 50,
            'ioduriAlogenuriMetallici': 80,
            'sodioAltaPressione': 95,
            'sodioBassaPressione': 140,
            'led': 115
        }
        efficienzaLuminosa = switcher[inp]
        return efficienzaLuminosa

    puntiLuce = int(input('Punti Luce Led: '))
    energiaTotale = int()
    efficienzaLuminosa = tipologia(inp)


    totale = efficienzaLuminosa * downLightOutputRatio * \
             perditaEfficienzaLuminosa * utilizzo * efficienzaAlimentatore
    print("totale Led: ", totale)

    # 2. Definizione di pesi per la ripartizione dei consumi totali
    # per ogni tecnologia «i» in funzione del numero di punti luce 𝑁_𝑖
    # e dell’efficienza complessiva 𝜂_𝑖  :

    def pesiRipartizioneLed(totale, puntiLuce):
        #x = factorial(6)
        if totale==0 and puntiLuce==0:
            return 1
        else:
            n=(puntiLuce * (1 / totale))
            print(n)
        pesiTotLed=8.09790505
        w = ((puntiLuce * (1 / totale)) / (pesiTotLed))  # ????
        return w

    w = pesiRipartizioneLed(totale, puntiLuce)
    print("Ripartizione consumi Led", w)

    # 3. Calcolo della quota di energia da assegnare
    # ad una specifica tecnologia «i» a partire dai consumi totali:

    def calcoloQuotaEnergia(w, energiaTotale):
        energiaTotale=0.2
        e = w * energiaTotale
        return e

    e = calcoloQuotaEnergia(w, energiaTotale)
    print("consumi", e)

    # 4. Stima della potenza media dei singoli punti
    # luce per ogni tecnologia «i» considerando un numero di ore di esercizio
    # annue pari a 4200

    def stimaPotenziaMedia(e, puntiLuce):
        p = e / (4200 * puntiLuce)
        return p

    p = stimaPotenziaMedia(e, puntiLuce)
    print("potenzia Media", p)

    # 5. Calcolo dei consumi di energia per illuminazione
    # pubblica al netto dei consumi dovuti ai punti luce a LED:

    def sommaTotaleConsumiLed(e, energiaTotale):
        e = energiaTotale * 5
        return e

    e = sommaTotaleConsumiLed(e, energiaTotale)
    print("Somma Consumi", e)

    # 6. Calcolo del numero di punti luce da sostituire con tecnologia a LED.
    def num(puntiLuce):
        inp=int()
        if inp=='led':
            puntiLuce=inp
        return puntiLuce

    puntiLuce = num(puntiLuce)
    print("numero di punti", puntiLuce)

    # 7. Stima dell’investimento necessario alla sostituzione
    # dei punti luce considerando un costo medio di circa 700€(*)
    # per punto luce a LED.

    def investimento(self):
        costo=700
        inp = int(input("stima dell'investimento"))
        if inp == 'led':
            investimento = (inp + costo) / 2
        return investimento  # non va bene

    # 8.Stima del risparmio energetico annuale ottenibile
    # sostituendo tutti i punti luce convenzionali con punti luce
    # a tecnologia LED utilizzando la potenza media 𝑃_𝑖 calcolata al punto 4.

    def risparmioEconomicoAnnuale(self, totale, e, puntiLuce):
        energetico = 1
        elettrica = 0.2
        p = e / (4200 * puntiLuce)
        for i in range(energetico + 1):
            print(energetico, i)
        puntiLuce = (totale + elettrica) / 2
        return (p,puntiLuce)

    # 8. Stima del risparmio economico annuale ottenibile
    # a partire dal risparmio energetico conseguito
    # sostituendo i punti luce convenzionali
    # con punti luce a tecnologia LED considerando un costo medio
    # per l’energia elettrica pari a 0.2€/kWh.

    def risparmioEconomicoAnnuale(self, totale):
        energetico = 1
        elettrica = 0.2
        for i in range(energetico + 1):
            print(energetico, i)
        puntiLuce = (totale + elettrica) / 2

        return puntiLuce

    # 9. Stima dei Titoli di Efficienza Energetica (TEE)
    # ottenibili per 5 anni a partire dal risparmio
    # conseguito sostituendo i punti luce
    # convenzionali con punti luce a tecnologia LED.

    def titoliEfficienzaEnergetica(self, puntiLuce):  # ??
        tee = 5
        for i in range(tee + 1):
            print(tee, i)
            tee -= 1
            puntiLuce=tee
        return puntiLuce # non va bene

    # 9.Stima del Simple Pay Back Time per l’investimento
    # necessario alla sostituzione dei punti luce.

    def simplePayBackTime(self):
        investimento = int()
        puntiLuce = investimento
        return puntiLuce
############################################# RISORSE DISPONIBILI #################################


class RisorseDisponibili():
    inp = str(input("Tipologia Illuminazione Risorse Disponibili: "))

    if inp != 'led':
        downLightOutputRatio = 0.8
        perditaEfficienzaLuminosa = 0.6
        utilizzo = 0.55
        efficienzaAlimentatore = 0.87
    else:
        downLightOutputRatio = 0.95
        perditaEfficienzaLuminosa = 0.8
        utilizzo = 0.7
        efficienzaAlimentatore = 0.88

    def tipologia(inp):
        switcher = {
            'incandescenza': 17,
            'mercurio': 50,
            'ioduriAlogenuriMetallici': 80,
            'sodioAltaPressione': 95,
            'sodioBassaPressione': 140,
            'led': 115
        }
        efficienzaLuminosa = switcher[inp]
        return efficienzaLuminosa

    puntiLuce = int(input('Punti Luce: '))
    energiaTotale = int()
    efficienzaLuminosa = tipologia(inp)

    totale = efficienzaLuminosa * downLightOutputRatio * \
             perditaEfficienzaLuminosa * utilizzo * efficienzaAlimentatore
    print("totale Risorse: ", totale)

# 2. Definizione di pesi per la ripartizione dei consumi totali
    # per ogni tecnologia «i» in funzione del numero di punti luce 𝑁_𝑖
    # e dell’efficienza complessiva 𝜂_𝑖  :

    def pesiRipartizioneRisorse(totale, puntiLuce):
        if totale==0 and puntiLuce==0:
            return 1
        else:
            n=(puntiLuce * (1 / totale))
            print(n)
        pesiTotLed=5.89275461
        w = ((puntiLuce * (1 / totale)) / (pesiTotLed))  # ????
        return w
    w = pesiRipartizioneRisorse(totale,puntiLuce)
    print("Ripartizione consumi Risorse", w)


# 3. Calcolo della quota di energia da assegnare
    # ad una specifica tecnologia «i» a partire dai consumi totali:

    # def calcoloQuotaEnergia(self,w,energiaTotale):
    #     e = w * energiaTotale
    #     return e
    #
    # e = calcoloQuotaEnergia(w,energiaTotale)

# 4. Stima della potenza media dei singoli punti
    # luce per ogni tecnologia «i» considerando un numero di ore di esercizio annue pari a 4200

    def stimaPotenziaMedia(self, e, puntiLuce):
        p = e/(4200 * puntiLuce)
        return p

# 5. Calcolo dei consumi di energia per illuminazione
    # pubblica al netto dei consumi dovuti ai punti luce a LED:

    def sommaTotaleConsumiLed(self,energiaTotale):
        e = energiaTotale * 5
        return e

# 6. Calcolo del numero di punti luce da sostituire con tecnologia a LED
# in funzione delle risorse economiche disponibili,
# considerando un costo medio di sostituzione di circa 700€(*) per punto luce.
# Sostituzione dei punti luce a partire da quelli con tecnologia a minore
# efficienza complessiva (Incandescenza, Mercurio alta pressione, etc.).

    def risorseEconomicheDisp(self, puntiLuce, risorseEconomiche):
        inp = int()
        costo=700+("euro")
        if inp == 'led':
            puntiLuce = inp
            costoMedio=(puntiLuce+costo)/2
        return (costoMedio)
            #if puntiLuce < (self.tipologia()) ?? #Sostituzione dei punti luce a partire da quelli con tecnologia a minore efficienza complessiva (Incandescenza, Mercurio alta pressione, etc.).

# 7. Stima del risparmio energetico annuale ottenibile sostituendo i punti luce
# convenzionali calcolati al punto 6 con punti luce a tecnologia LED
# utilizzando la potenza media 𝑃_𝑖 calcolata al punto 4.

    def StimaRispEnergiaAnnuale(self):
        puntiLuce=self.risorseEconomicheDisp()
        P_i= self.stimaPotenziaMedia()
        return puntiLuce, P_i

# 8. Stima dei Titoli di Efficienza Energetica (TEE) ottenibili
# per 5 anni a partire dal risparmio conseguito sostituendo i punti luce
# convenzionali con punti luce a tecnologia LED.

    def TEE(self,rispConseguito): ## non va bene
        tee=5
        rispConseguito > tee
        puntiLuce = rispConseguito
        puntiluceLed= (self.tipologia(), puntiLuce)
       # puntiluceLed = puntiLuce
        return puntiluceLed

    # def titoliEfficienzaEnergetica(self, puntiLuce):  # ??
    #     tee = 5
    #     for i in range(tee + 1):
    #         print(tee, i)
    #         tee -= 1
    #         puntiLuce=tee
    #     return puntiLuce # non va bene

# 8. Stima del risparmio economico annuale ottenibile a partire
# dal risparmio energetico conseguito sostituendo i punti luce convenzionali
# con punti luce a tecnologia LED considerando un costo medio
# per l’energia elettrica pari a 0.2€/kWh

    def risparmioEconomicoAnnuale(self, totale):
        energetico = 1
        elettrica = 0.2
        for i in range(energetico + 1):
            print(energetico, i)
        puntiLuce = (totale + elettrica) / 2

        return puntiLuce

# 9. Stima del Simple Pay Back Time per l’investimento necessario
# alla sostituzione dei punti luce.

    def simplePayBackTime(self):
        investimento=int()
        puntiLuce=investimento
        return puntiLuce