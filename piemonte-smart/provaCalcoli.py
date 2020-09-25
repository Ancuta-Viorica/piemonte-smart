





import math
import datetime
from math import factorial
import numpy
from decimal import *
#today = datetime.date.today()

######################################### RUDUZIONE 50 ######################################
import self as self


class Riduzione50():
    inp=()
    if inp =="incandescenza":
        #inp = self.tipologia(totaleInc)
        # self.totaleInc()
        inp = 'incandescenza'
    if inp=='mercurio' :
        inp = ('mercurio')
    if inp=='ioduriAlogenuriMetallici':
        inp=('ioduriAlogenuriMetallici')
    if inp=='sodioAltaPressione':
        inp= ('sodioAltaPressione')
    if inp=='sodioBassaPressione':
        inp = ('sodioBassaPressione')
    if inp == 'led':
        inp = ('led')
    # #breakpoint()
    else: inp == 'null'
    inp='null'

    # inp = (('mercurio'))
    # inp = (('ioduriAlogenuriMetallici'))
    # inp = (('sodioAltaPressione'))
    # inp = (('sodioBassaPressione'))
    # inp = (('led'))

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

    puntiLuceInc = int(input('Numero punti luce ad Incandescenza: '))
    energiaTotale = int()
    efficienzaLuminosa = tipologia(inp='incandescenza')

    totaleInc = efficienzaLuminosa * downLightOutputRatio * \
             perditaEfficienzaLuminosa * utilizzo * efficienzaAlimentatore
    print("totale RUDUZIONE: ", totaleInc)

    puntiLuceMerc = int(input('Numero punti luce a Mercurio alta pressione : '))
    energiaTotale = int()
    efficienzaLuminosa = tipologia(inp='mercurio')

    totaleMerc = efficienzaLuminosa * downLightOutputRatio * \
                perditaEfficienzaLuminosa * utilizzo * efficienzaAlimentatore
    print("totale RUDUZIONE mercurio: ", totaleMerc)

    puntiLuceMH = int(input('Numero punti luce ad Ioduri e Alogenuri Metallici (MH) : '))
    energiaTotale = int()
    efficienzaLuminosa = tipologia(inp='ioduriAlogenuriMetallici')

    totaleMH = efficienzaLuminosa * downLightOutputRatio * \
                 perditaEfficienzaLuminosa * utilizzo * efficienzaAlimentatore
    print("totale RUDUZIONE MH: ", totaleMH)

    puntiLuceSAP = int(input('Numero punti luce a Sodio ad alta pressione (SAP) : '))
    energiaTotale = int()
    efficienzaLuminosa = tipologia(inp='sodioAltaPressione')

    totaleSAP = efficienzaLuminosa * downLightOutputRatio * \
               perditaEfficienzaLuminosa * utilizzo * efficienzaAlimentatore
    print("totale RUDUZIONE SAP: ", totaleSAP)

    puntiLuceSBP = int(input('Numero punti luce a Sodio a bassa pressione (SBP): '))
    energiaTotale = int()
    efficienzaLuminosa = tipologia(inp='sodioBassaPressione')

    totaleSBP = efficienzaLuminosa * downLightOutputRatio * \
               perditaEfficienzaLuminosa * utilizzo * efficienzaAlimentatore
    print("totale RUDUZIONE SBP: ", totaleSBP)

    puntiLuceLED = int(input('Numero punti luce a Led: '))
    energiaTotale = int()
    efficienzaLuminosa = tipologia(inp='led')
    totaleLED = efficienzaLuminosa * downLightOutputRatio * \
                perditaEfficienzaLuminosa * utilizzo * efficienzaAlimentatore
    print("totale RUDUZIONE LED: ", totaleLED)

#1. Stima efficienza complessiva media 𝜼_𝑖  per ogni tecnologia
    # di punto luce a partire dall’efficienza luminosa media
    # utilizzando la relazione(*):

    # totale = efficienzaLuminosa * downLightOutputRatio * \
    #          perditaEfficienzaLuminosa * utilizzo * efficienzaAlimentatore
    # print("totale RUDUZIONE: ", totale)

# 2. Definizione di pesi per la ripartizione dei consumi totali
    # per ogni tecnologia «i» in funzione del numero di punti luce 𝑁_𝑖
    # e dell’efficienza complessiva 𝜂_𝑖  :

    print("--------Consimi 2015-------------")

    def PesiRipartizione15(totaleInc,puntiLuceInc,totaleMerc,puntiLuceMerc, totaleMH, puntiLuceMH, totaleSAP,puntiLuceSAP, totaleSBP,puntiLuceSBP, totaleLED, puntiLuceLED):      ###### def 15
        # if totaleInc == 0 and puntiLuce == 0:
        #     return 1
        # else:
        pesiINC=(puntiLuceInc * (1 / totaleInc))
        print("pesi INC",pesiINC)
        pesiMerc=(puntiLuceMerc * (1/ totaleMerc))
        print("pesi Merc", pesiMerc)
        pesiMH = (puntiLuceMH * (1 / totaleMH))
        print("pesi MH", pesiMH)
        pesiSAP = (puntiLuceSAP * (1 / totaleSAP))
        print("pesi SAP", pesiSAP)
        pesiSBP = (puntiLuceSBP * (1 / totaleSBP))
        print("pesi SBP", pesiSBP)
        pesiLED = (puntiLuceLED * (1 / totaleLED))
        print("pesi LED", pesiLED)
        # risultato = 0
        # tot = puntiLuce * (1 / totaleInc)
        # tot += risultato
        # w = PesiINC / (tot) # ????
        i = pesiINC
        m = pesiMerc
        mh = pesiMH
        sap = pesiSAP
        sbp = pesiSBP
        led = pesiLED
       # return i, m, mh, sap, sbp, led
        totPesi=i+m+mh+sap+sbp+led
        print("Pesi TOTALE",totPesi)

        if pesiINC:
            TOTINC=pesiINC/totPesi
            print(" Totale w incandescenza",TOTINC)
            w=TOTINC
            return w
        if pesiMerc:
            TOTMERC=pesiMerc/totPesi
            print("Totale w mercurio", TOTMERC)
            w=TOTMERC
            return w
        if pesiMH:
            TOTMH=pesiMH/totPesi
            print("Totale w ioduri Alogenuri Metallici",TOTMH)
            return TOTMH
        if pesiSAP:
            TOTSAP=pesiSAP/totPesi
            print("totale w sodio Alta Pressione", TOTSAP)
            return TOTSAP
        if pesiSBP:
            TOTSBP=pesiSBP/totPesi
            print("totale w Sodio a bassa pressione",TOTSBP)
            return TOTSBP
        if pesiLED:
            TOTLED=pesiLED/totPesi
            print("totale w led",TOTLED)
            return TOTLED


        #return w
        #return
    w=PesiRipartizione15(totaleInc,puntiLuceInc,totaleMerc,puntiLuceMerc, totaleMH, puntiLuceMH, totaleSAP,puntiLuceSAP,totaleSBP,puntiLuceSBP,totaleLED, puntiLuceLED)
    print("Ripartizione consumi 2015",w)
    # i, m, mh, sap, sbp, led = PesiRipartizione15(totaleInc,puntiLuceInc,totaleMerc,puntiLuceMerc, totaleMH, puntiLuceMH, totaleSAP,puntiLuceSAP,totaleSBP,puntiLuceSBP,totaleLED, puntiLuceLED)
    # print("Ripartizione consumi 2015", i, m, mh, sap, sbp, led)


# 3. Calcolo della quota di energia da assegnare
    # ad una specifica tecnologia «i» a partire dai consumi totali:

    def calcoloQuotaEnergia( i):
        energiaTotale=0.2
        e = i * energiaTotale
        return e
    e = calcoloQuotaEnergia(i )
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


















# class Riduzione50():
#
#     def incandescenza(inp):
#         inp = int(input("Punti Luce incandescenza: "))
#         return "incandescenza"
#
#     def mercurio(inp):
#         inp = int(input("Punti Luce mercurio: "))
#         return "mercurio"
#
#     def ioduriAlogenuriMetallici(inp):
#         inp = int(input("Punti Luce ioduri Alogenuri Metallici: "))
#         return "ioduri Alogenuri Metallic"
#
#     def sodioAltaPressione(inp):
#         inp = int(input("Punti Luce sodio Alta Pressione: "))
#         return "sodio Alta Pressione"
#
#     def sodioBassaPressione(inp):
#         inp = int(input("Punti Luce sodio Bassa Pressione "))
#         return "sodio Bassa Pressione"
#
#     def led(inp):
#         inp = int(input("Punti Luce Led "))
#         return "led"
#
#     inp=int(input("incandescenza"))
#
#     if inp != 'led':
#         downLightOutputRatio = 0.8
#         perditaEfficienzaLuminosa = 0.6
#         utilizzo = 0.55
#         efficienzaAlimentatore = 0.87
#     else:
#         downLightOutputRatio = 0.95
#         perditaEfficienzaLuminosa = 0.8
#         utilizzo = 0.7
#         efficienzaAlimentatore = 0.88
#
#     def tipologia(inp):
#         incandescenza = 17,
#         mercurio = 50,
#         ioduriAlogenuriMetallici = 80,
#         sodioAltaPressione = 95,
#         sodioBassaPressione = 140,
#         led = 115
#
#         switcher = {
#             1: incandescenza,
#             2: mercurio,
#             3: ioduriAlogenuriMetallici,
#             4: sodioAltaPressione,
#             5: sodioBassaPressione,
#             6: led
#         }
#         efficienzaLuminosa = switcher[inp]
#         return efficienzaLuminosa
#
#     energiaTotale = int()
#     efficienzaLuminosa = tipologia(inp)
#
#     totale = efficienzaLuminosa * downLightOutputRatio * \
#              perditaEfficienzaLuminosa * utilizzo * efficienzaAlimentatore
#     print("totale RUDUZIONE: ", totale)