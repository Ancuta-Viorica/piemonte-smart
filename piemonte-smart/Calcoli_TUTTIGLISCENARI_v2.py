####################################################                                      FUNZIONI                                     ####################################################
import pandas as pd
import copy
from IPython.display import clear_output

####################################################                             FUNZIONI PER TUTTI GLI SCENARI                               ####################################################
def scelta_scenario(): #1 = risparmio 50% | 2 = tutto led | 3 = risorse disponibili
  print("CALCOLA IL TUO RISPARMIO SULL'ILLUMINAZIONE PUBBLICA\nQuesto tool ti aiuterà a stimare il risparmio energetico ed economico derivante dalla sostituzione dei vecchi punti luce dell'illuminazione pubblica con LED nonchè le risorse economiche necessarie ad effettuare la sostituzione.")
  print("Puoi simulare 3 diversi scenari relativamente alle esigenze della tua Città:")
  print("\nSCENARIO 1: Calcolo del numero di punti luce da sostituire a LED e le risorse economiche necessarie per ridurre i consumi della tua Città del 50%.")
  print("SCENARIO 2: Calcolo delle risorse economiche necessarie, del risparmio energetico ed economico ottenibile convertendo a LED tutti i punti luce della tua città.")
  print("SCENARIO 3: Partendo dalle risorse economiche che la tua Città può dedicarvi, viene calcolato il numero di punti luce che puoi convertire a LED,il risparmio energetico ed economico ottenibile per la tua Città.")
  while True:
    try:
      scenario = int(input("\nInserisci il numero dello scenario che vuoi simulare:"))
      if scenario <1 or scenario > 3:
        print("Input errato, si prega di inserire un valore numerico fra 1 e 3")
        continue
    except ValueError:
      print("Input errato, si prega di inserire un valore numerico fra 1 e 3")
      continue
    break

  return scenario

def input_dati(anni,tecnologie):
  consumi = pd.DataFrame(index=anni, columns=['kWh'])
  spesa_annua =  pd.DataFrame(index=anni, columns=['€'])
  puntiluce = pd.DataFrame(index=anni, columns=tecnologie)
  #RICEZIONE DATI DI INPUT
  for riga,r in puntiluce.iterrows():
    while True:
      try:
        consumi['kWh'][riga] =   (float(input("ANNO {0}\nInserire consumo per illuminazione pubblica [kWh] : ".format(str(riga)))))
        spesa_annua['€'][riga] = (float(input("Inserire spesa per illuminazione pubblica [€] : ")))
      except ValueError:
        clear_output(wait=True)
        print("Input errato, si prega di inserire valori numerici")
        continue
      break
    for columns in puntiluce:
      while True:
        try:
          puntiluce[columns][riga]=(float(input("Inserire numero punti luce con tecnologia {0} : ".format(columns))))
        except ValueError:
          print("Input errato, si prega di inserire valori numerici")
          continue
        break
  return consumi,puntiluce,spesa_annua

# CALCOLO PESI
def calcola_pesi(anni,tecnologie,eta,puntiluce):
  pesi = 1/eta
  Pesi = ripartizione_consumi = pd.DataFrame(index=anni, columns=tecnologie)

  for riga,r in Pesi.iterrows():
      for columns in Pesi:
        Pesi[columns][riga] = int(puntiluce[columns][riga])*pesi[columns][0]
  Pesi["somma"] = Pesi.sum(axis=1)
  return Pesi

def calcola_ripartizione_consumi(tecnologie,Pesi,consumi):
  # CALCOLO RIPARTIZIONE CONSUMI
  ripartizione_consumi = pd.DataFrame(index=[2015,2016,20152016,2019], columns=tecnologie)
  for riga,r in ripartizione_consumi.iterrows():
      for columns in ripartizione_consumi:
        if riga == 2015 or riga == 2016 or riga == 2019:
          ripartizione_consumi[columns][riga] = (Pesi[columns][riga]*float(consumi['kWh'][riga])) / Pesi['somma'][riga]
        elif riga == 20152016:
          ripartizione_consumi[columns][riga] = (ripartizione_consumi[columns][2015]+ripartizione_consumi[columns][2016])/2
  # CALCOLO SOMMA RIPARTIZIONE CONSUMI
  ripartizione_consumi['TOT_no_led'] = 0
  ripartizione_consumi['TOT_no_led'] = ripartizione_consumi.sum(axis=1) - ripartizione_consumi['LED'] 
  return ripartizione_consumi

def calcola_potenza_media(ripartizione_consumi,puntiluce):
  # CALCOLO POTENZA MEDIA
  potenza_media = pd.DataFrame(index=anni, columns=tecnologie)
  for riga,r in potenza_media.iterrows():
      for columns in potenza_media:
        if int(puntiluce[columns][riga]) > 0:
          potenza_media[columns][riga] = ripartizione_consumi[columns][riga] / ore_esercizio / 1000 / int(puntiluce[columns][riga]) * 1000000
        else: potenza_media[columns][riga] = 0
  return potenza_media

####################################################                             FUNZIONI PER SCENARIO 1                             ####################################################
def calcola_ripartizione_consumi_2020(tecnologie,Pesi,consumi,puntiluce,potenza_media):
  # CALCOLO RIPARTIZIONE CONSUMI
  ripartizione_consumi = pd.DataFrame(index=[2015,2016,20152016,2019], columns=tecnologie)
  for riga,r in ripartizione_consumi.iterrows():
      for columns in ripartizione_consumi:
        if riga == 2015 or riga == 2016 or riga == 2019:
          ripartizione_consumi[columns][riga] = (Pesi[columns][riga]*float(consumi['kWh'][riga])) / Pesi['somma'][riga]
        elif riga == 20152016:
          ripartizione_consumi[columns][riga] = (ripartizione_consumi[columns][2015]+ripartizione_consumi[columns][2016])/2
  for riga,r in ripartizione_consumi.iterrows():
    if riga == 2019:
      for columns in ripartizione_consumi:
        ripartizione_consumi[columns][riga] = puntiluce[columns][riga]*potenza_media[columns][riga]*ore_esercizio/1000

  # CALCOLO SOMMA RIPARTIZIONE CONSUMI
  ripartizione_consumi['TOT_no_led'] = 0
  ripartizione_consumi['TOT_no_led'] = ripartizione_consumi.sum(axis=1) - ripartizione_consumi['LED'] 
  return ripartizione_consumi

def calcola_riduzione_consumi(ripartizione_consumi):
  riduzione_consumi = (1-(ripartizione_consumi['TOT_no_led'][2019]/ripartizione_consumi['TOT_no_led'][20152016]))*100
  return round(riduzione_consumi,3)

def calcola_riduzione_50(puntiluce,anni,tecnologie,eta,consumi):
  puntiluce_2020 = copy.deepcopy(puntiluce)
  puntiluce_2020.drop(columns='TOT_no_led',inplace=True)
  riduzione_consumi_ = 0
  flag_puntiluceinsufficienti = 0

  for i in range(1,int(puntiluce['TOT_no_led'][2019])+1): #possono essere sostituiti al massimo il numero di lampioni non led presenti al 2019
    for columns in puntiluce_2020:
      if columns == 'LED': break
      for j in range(1,int(puntiluce[columns][2019])+1): #per ogni tecnologia posso sostituire al massimo in numero di lampioni presenti al 2019
        puntiluce_2020[columns][2019] -= 1
        puntiluce_2020['LED'][2019] += 1
        Pesi_ = calcola_pesi(anni,tecnologie,eta,puntiluce_2020)
        ripartizione_consumi_ = calcola_ripartizione_consumi_2020(tecnologie,Pesi_,consumi,puntiluce_2020,potenza_media)
        riduzione_consumi_ = calcola_riduzione_consumi(ripartizione_consumi_)
        if riduzione_consumi_ > 50: break
      if riduzione_consumi_ > 50: break
    if riduzione_consumi_ > 50: break
  
  if i ==  int(puntiluce['TOT_no_led'][2019]) and riduzione_consumi_ < 50: flag_puntiluceinsufficienti = 1 # SE SI ARRIVA ALLA FINE DEL CICLO E LA RIDUZIONE CONSUMI è < 50% > ATTIVO FLAG
  
  return puntiluce_2020,ripartizione_consumi_,riduzione_consumi_, flag_puntiluceinsufficienti

def print_risultati_riduzione50(puntiluce,puntiluce_2020,ripartizione_consumi,ripartizione_consumi_,riduzione_consumi,riduzione_consumi_):
  #CALCOLO PARAMETRI DELLO SCENARIO
  costo_puntoluce = 700
  #costo_energia = 0.2
  costo_energia = spesa['€'][2019] / consumi['kWh'][2019]

  #CALCOLO INVESTIMENTI
  investimento = costo_puntoluce * int(puntiluce_2020['LED'][2019] - puntiluce['LED'][2019])
  #CALCOLO RISPARMIO ECONOMICO ANNUALE
  ripartizione_consumi['TOT'] = 0; ripartizione_consumi_['TOT'] = 0
  ripartizione_consumi['TOT'] = ripartizione_consumi.sum(axis=1) - ripartizione_consumi['TOT_no_led']
  ripartizione_consumi_['TOT'] = ripartizione_consumi_.sum(axis=1) - ripartizione_consumi_['TOT_no_led']

  risparmioenergia = round(ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019])
  risparmio_economico_annuo = round((ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019]) * costo_energia)
  #CALCOLO TEE (TITOLI DI EFFICIENZA ENERGETICA)
  tee = round(((ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019]) * 0.187 * 0.001)) * 200 * 5
  # CALCOLO SPBT (SIMPLE PAYBACK TIME)
  if investimento > tee:
    spbt = round((investimento - tee) / risparmio_economico_annuo,2)

  #PRINT  
  print("\nRiduzione consumi fra media 2015-2016 e 2019: {0} %".format(riduzione_consumi))
  print("Per arrivare ad un risparmio del 50% occorre sostituire:")
  for columns in puntiluce_2020:
    if puntiluce_2020[columns][2019] < puntiluce[columns][2019]:
      print("{0} punti luce con tecnologia {1}".format(int((puntiluce[columns][2019]-puntiluce_2020[columns][2019])),columns))
  print("\nRiduzione consumo energetico: {0} %".format(riduzione_consumi_))
  print("Investimento necessario: {0} €".format(investimento))
  print("Risparmio energetico: {0} kWh".format(risparmioenergia))
  print("Risparmio economico annuo: {0} €".format(risparmio_economico_annuo))
  print("TEE: {0} €".format(tee))
  print("Simple Pay Back Time: {0} anni".format(spbt))

  return investimento, risparmioenergia, risparmio_economico_annuo, tee, spbt

####################################################                             FUNZIONI PER SCENARIO 2                             ####################################################
def calcola_ripartizione_consumi_tuttoled(anni,tecnologie,Pesi,consumi):
  # CALCOLO RIPARTIZIONE CONSUMI
  ripartizione_consumi = pd.DataFrame(index=anni, columns=tecnologie)
  for riga,r in ripartizione_consumi.iterrows():
      for columns in ripartizione_consumi:
        ripartizione_consumi[columns][riga] = (Pesi[columns][riga]*float(consumi['kWh'][riga])) / Pesi['somma'][riga]
  # CALCOLO SOMMA RIPARTIZIONE CONSUMI
  ripartizione_consumi['TOT'] = 0
  ripartizione_consumi['TOT'] = ripartizione_consumi.sum(axis=1)
  return ripartizione_consumi

def calcola_ripartizione_consumi_tuttoled_2020(anni,tecnologie,Pesi,consumi,puntiluce,potenza_media):
  # CALCOLO RIPARTIZIONE CONSUMI
  ripartizione_consumi = pd.DataFrame(index=anni, columns=tecnologie)

  for riga,r in ripartizione_consumi.iterrows():
    for columns in ripartizione_consumi:
      ripartizione_consumi[columns][riga] = puntiluce[columns][riga]*potenza_media[columns][riga]*ore_esercizio/1000

  # CALCOLO SOMMA RIPARTIZIONE CONSUMI
  ripartizione_consumi['TOT'] = 0
  ripartizione_consumi['TOT'] = ripartizione_consumi.sum(axis=1)
  return ripartizione_consumi

def calcola_riduzione_tuttoled(puntiluce,anni,tecnologie,eta,consumi):
  puntiluce_2020 = copy.deepcopy(puntiluce)
  for columns in puntiluce_2020:
    if columns == 'LED': puntiluce_2020[columns][2019] += puntiluce_2020['TOT_no_led'][2019]
    elif columns == 'TOT_no_led': continue
    else: puntiluce_2020[columns][2019] = 0
  puntiluce_2020.drop(columns='TOT_no_led',inplace=True)

  Pesi_ = calcola_pesi(anni,tecnologie,eta,puntiluce_2020)
  ripartizione_consumi_ = calcola_ripartizione_consumi_tuttoled_2020(anni,tecnologie,Pesi_,consumi,puntiluce_2020,potenza_media)
  return puntiluce_2020,ripartizione_consumi_

def calcola_riduzione_consumi_tuttoled(ripartizione_consumi,ripartizione_consumi_):
  riduzione_consumi = (1-(ripartizione_consumi_['TOT'][2019]/ripartizione_consumi['TOT'][2019]))*100
  return round(riduzione_consumi,3)

def print_risultati_tuttoled(puntiluce,puntiluce_2020,ripartizione_consumi,ripartizione_consumi_,riduzione_consumi):
  #CALCOLO PARAMETRI DELLO SCENARIO
  costo_puntoluce = 700  
  #costo_energia = 0.2
  costo_energia = spesa['€'][2019] / consumi['kWh'][2019]

  #CALCOLO INVESTIMENTI
  investimento = costo_puntoluce * int(puntiluce_2020['LED'][2019] - puntiluce['LED'][2019])
  #CALCOLO RISPARMIO ECONOMICO ANNUALE
  risparmioenergia = round(ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019])
  risparmio_economico_annuo = round((ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019]) * costo_energia)
  #CALCOLO TEE (TITOLI DI EFFICIENZA ENERGETICA)
  tee = round(((ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019]) * 0.187 * 0.001)) * 200 * 5
  # CALCOLO SPBT (SIMPLE PAYBACK TIME)
  if investimento > tee: spbt = round((investimento - tee) / risparmio_economico_annuo,2)
  else: spbt = 0

  #PRINT  
  print("\nRiduzione consumo energetico  ottenibile convertendo a LED tutti i punti luce della tua città: {0} %".format(riduzione_consumi))
  print("I punti luce da convertire sono {}".format(int(puntiluce['TOT_no_led'][2019])))
  print("Investimento necessario: {0} €".format(investimento))
  print("Risparmio energetico: {0} kWh".format(int(risparmioenergia)))
  print("Risparmio economico annuo: {0} €".format(int(risparmio_economico_annuo)))
  print("TEE: {0} €".format(int(tee)))
  print("Simple Pay Back Time: {0} anni".format(spbt))

  return investimento, risparmioenergia, risparmio_economico_annuo, tee, spbt

####################################################                             FUNZIONI PER SCENARIO 3                             ####################################################
def calcola_ripartizione_consumi_rd(anni,tecnologie,Pesi,consumi):
  # CALCOLO RIPARTIZIONE CONSUMI
  ripartizione_consumi = pd.DataFrame(index=anni, columns=tecnologie)
  for riga,r in ripartizione_consumi.iterrows():
      for columns in ripartizione_consumi:
        ripartizione_consumi[columns][riga] = (Pesi[columns][riga]*float(consumi['kWh'][riga])) / Pesi['somma'][riga]
  # CALCOLO SOMMA RIPARTIZIONE CONSUMI
  ripartizione_consumi['TOT'] = 0
  ripartizione_consumi['TOT'] = ripartizione_consumi.sum(axis=1)
  return ripartizione_consumi

def calcola_ripartizione_consumi_rd_2020(anni,tecnologie,Pesi,consumi,puntiluce,potenza_media):
  # CALCOLO RIPARTIZIONE CONSUMI
  ripartizione_consumi = pd.DataFrame(index=anni, columns=tecnologie)

  for riga,r in ripartizione_consumi.iterrows():
    for columns in ripartizione_consumi:
      ripartizione_consumi[columns][riga] = puntiluce[columns][riga]*potenza_media[columns][riga]*ore_esercizio/1000

  # CALCOLO SOMMA RIPARTIZIONE CONSUMI
  ripartizione_consumi['TOT'] = 0
  ripartizione_consumi['TOT'] = ripartizione_consumi.sum(axis=1)
  return ripartizione_consumi

def calcola_puntiluce_da_sostituire_rd(puntiluce,anni,tecnologie,eta,consumi,puntiluce_sostituibili):
  puntiluce_sostituiti = 0
  puntiluce_2020 = copy.deepcopy(puntiluce)
  puntiluce_2020.drop(columns='TOT_no_led',inplace=True)

  while True:
    for columns in puntiluce_2020:
      if columns == 'LED': break
      for j in range(1,int(puntiluce[columns][2019])+1): #per ogni tecnologia posso sostituire al massimo in numero di lampioni presenti al 2019
        puntiluce_2020[columns][2019] -= 1
        puntiluce_2020['LED'][2019] += 1
        puntiluce_sostituiti += 1
        if puntiluce_sostituiti == puntiluce_sostituibili: break#possono essere sostituiti al massimo il numero di lampioni pari a "puntiluce_sostituibili"
      if puntiluce_sostituiti == puntiluce_sostituibili: break
    if puntiluce_sostituiti == puntiluce_sostituibili: break
  
  Pesi_ = calcola_pesi(anni,tecnologie,eta,puntiluce_2020)
  ripartizione_consumi_ = calcola_ripartizione_consumi_rd_2020(anni,tecnologie,Pesi_,consumi,puntiluce_2020,potenza_media)
  riduzione_consumi = calcola_riduzione_consumi_tuttoled(ripartizione_consumi,ripartizione_consumi_)

  return puntiluce_2020,ripartizione_consumi_,riduzione_consumi

def print_risultati_rd(puntiluce, puntiluce_2020, ripartizione_consumi,ripartizione_consumi_,riduzione_consumi,risorse_usate,puntiluce_sostituibili):
  #CALCOLO PARAMETRI DELLO SCENARIO
  #costo_energia = 0.2
  costo_energia = spesa['€'][2019] / consumi['kWh'][2019]

  #CALCOLO RISPARMIO ECONOMICO ANNUALE
  risparmioenergia = round(ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019])
  risparmio_economico_annuo = round((ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019]) * costo_energia)
  #CALCOLO TEE (TITOLI DI EFFICIENZA ENERGETICA)
  tee = round(((ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019]) * 0.187 * 0.001)) * 200 * 5
  # CALCOLO SPBT (SIMPLE PAYBACK TIME)
  if risorse_usate > tee: spbt = round((risorse_usate - tee) / risparmio_economico_annuo,2)
  else: spbt = 0

  #PRINT  
  print("I punti luce LED acquistabili sono {}".format(int(puntiluce_sostituibili)))
  print("I punti luce da sostituire sono:")
  for columns in puntiluce_2020:
    if puntiluce_2020[columns][2019] < puntiluce[columns][2019]:
      print("     {0} con tecnologia {1}".format(int((puntiluce[columns][2019]-puntiluce_2020[columns][2019])),columns))
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
tecnologie = ['Incandescenza ','Mercurio alta pressione ', 'Ioduri e Alogenuri Metallici (MH) ','Sodio ad alta pressione (SAP) ','Sodio a bassa pressione (SBP) ','LED']
eta_ = [[3.90456,11.484,18.3744,21.8196,32.1552,53.8384]]
eta = pd.DataFrame(data=eta_,columns=tecnologie)
anni = [2015,2016,2019]
ore_esercizio = 4200

##########################                   SCELTA SCENARIO DA SIMULARE                   ##########################
scenario = scelta_scenario()

if scenario == 1:
  ####################################################                                      SCENARIO RISPARMIO 50 %                                      ####################################################

  ##########################                   MAIN                   ##########################
  tecnologie = ['Incandescenza ','Mercurio alta pressione ', 'Ioduri e Alogenuri Metallici (MH) ','Sodio ad alta pressione (SAP) ','Sodio a bassa pressione (SBP) ','LED']
  eta_ = [[3.90456,11.484,18.3744,21.8196,32.1552,53.8384]]
  eta = pd.DataFrame(data=eta_,columns=tecnologie)
  anni = [2015,2016,2019]
  ore_esercizio = 4200

  #1 - Ricezione dati di input
  consumi,puntiluce,spesa = input_dati(anni,tecnologie)

  #2 - Calcolo pesi
  Pesi = calcola_pesi(anni,tecnologie,eta,puntiluce)

  #3 - Calcolo ripartizione consumi
  ripartizione_consumi = calcola_ripartizione_consumi(tecnologie,Pesi,consumi)

  #4 - Calcolo potenza media
  potenza_media = calcola_potenza_media(ripartizione_consumi,puntiluce)

  #5 CALCOLO RIDUZIONE CONSUMI FRA MEDIA 205-2016 E 2019
  riduzione_consumi = calcola_riduzione_consumi(ripartizione_consumi)
  if riduzione_consumi >= 50: print("\nLa tua Città ha già raggiunto la riduzione del 50% dei consumi nel 2019! Complimenti!")
  else:
    #6 - CALCOLO PUNTI LUCE DA SOSTITUIRE PER ARRIVARE A RISPARMIO = 50%
    puntiluce['TOT_no_led'] = 0; puntiluce['TOT_no_led'] = puntiluce.sum(axis=1) - puntiluce['LED'] #aggiungo colonna con somma dei punti luce non led

    puntiluce_2020,ripartizione_consumi_,riduzione_consumi_,flag_puntiluceinsufficienti = calcola_riduzione_50(puntiluce,anni,tecnologie,eta,consumi)

    if flag_puntiluceinsufficienti == 1: print("ATTENZIONE!!!\nNumero punti luce da sostituire risulta insufficiente per poter raggiungere il risparmio energetico del 50%.\n")
    
    investimento, risparmioenergia, risparmio_economico_annuo, tee, spbt = print_risultati_riduzione50(puntiluce, puntiluce_2020, ripartizione_consumi, ripartizione_consumi_, riduzione_consumi, riduzione_consumi_)


if scenario == 2:
  ####################################################                                      SCENARIO TUTTO LED                                     ####################################################
  anni = [2019]

  #1 - Ricezione dati di input
  consumi,puntiluce,spesa = input_dati(anni,tecnologie)

  #2 - Calcolo pesi
  Pesi = calcola_pesi(anni,tecnologie,eta,puntiluce)

  #3 - Calcolo ripartizione consumi
  ripartizione_consumi = calcola_ripartizione_consumi_tuttoled(anni,tecnologie,Pesi,consumi)

  #4 - Calcolo potenza media
  potenza_media = calcola_potenza_media(ripartizione_consumi,puntiluce)

  #5 CONVERTO I PUNTI LUCE IN TUTTO LED E CALCOLO I CONSUMI
  puntiluce['TOT_no_led'] = 0; puntiluce['TOT_no_led'] = puntiluce.sum(axis=1) - puntiluce['LED'] #aggiungo colonna con somma dei punti luce non led

  puntiluce_2020,ripartizione_consumi_ = calcola_riduzione_tuttoled(puntiluce,anni,tecnologie,eta,consumi)

  # CALCOLO RISPARMIO %
  riduzione_consumi = calcola_riduzione_consumi_tuttoled(ripartizione_consumi,ripartizione_consumi_)

  investimento, risparmioenergia, risparmio_economico_annuo, tee, spbt = print_risultati_tuttoled(puntiluce, puntiluce_2020, ripartizione_consumi, ripartizione_consumi_, riduzione_consumi)


if scenario == 3:
  ####################################################                                      SCENARIO RISORSE DISPONIBILI                                    ####################################################
  anni = [2019]
  costo_puntoluce = 700  

  #1 - Ricezione dati di input
  consumi,puntiluce,spesa = input_dati(anni,tecnologie)
  while True:
    risorse = (float(input("Risorse disponibili [€] : ")))
    if risorse < costo_puntoluce:
      print("Risorse insufficienti, inserire valore valido")
      continue
    else: break
  
  puntiluce_sostituibili = int(risorse/costo_puntoluce) #CALCOLO NUMERO DI PUNTI LUCE ACQUISTABILI CON LE RISORSE DATE
  investimento = puntiluce_sostituibili*costo_puntoluce #CALCOLO DELLA SPESA EFFETTIVA, CONSIDERATO L'ARROTONDAMENTO PER DIFETTO APPLICATO ALLA DIVISIONE risorse/costo_puntoluce

  #2 - Calcolo pesi
  Pesi = calcola_pesi(anni,tecnologie,eta,puntiluce)

  #3 - Calcolo ripartizione consumi
  ripartizione_consumi = calcola_ripartizione_consumi_rd(anni,tecnologie,Pesi,consumi)

  #4 - Calcolo potenza media
  potenza_media = calcola_potenza_media(ripartizione_consumi,puntiluce)

  #5 - CALCOLO PUNTI LUCE DA SOSTITUIRE
  puntiluce['TOT_no_led'] = 0; puntiluce['TOT_no_led'] = puntiluce.sum(axis=1) - puntiluce['LED'] #aggiungo colonna con somma dei punti luce non led
  if puntiluce_sostituibili > puntiluce['TOT_no_led'][2019]:
    puntiluce_sostituibili = puntiluce['TOT_no_led'][2019] #SE SI POSSONO ACQUISTARE PIù PUNTI LUCE LED DI QUANTI PUNTI LUCE NON_LED SONO PRESENTI, IL LIMITE DIVENTA IL NUMERO DI PUNTI LUCE NON_LED
    investimento = puntiluce_sostituibili*costo_puntoluce
  
  puntiluce_2020,ripartizione_consumi_,riduzione_consumi_ = calcola_puntiluce_da_sostituire_rd(puntiluce,anni,tecnologie,eta,consumi,puntiluce_sostituibili)

  risparmioenergia, risparmio_economico_annuo, tee, spbt = print_risultati_rd(puntiluce, puntiluce_2020, ripartizione_consumi, ripartizione_consumi_, riduzione_consumi_, investimento, puntiluce_sostituibili)
