##########################                   FUNZIONI                   ##########################
import pandas as pd
import copy
from IPython.display import clear_output


def input_dati(anni,tecnologie):
  consumi = pd.DataFrame(index=anni, columns=['kWh'])
  puntiluce = pd.DataFrame(index=anni, columns=tecnologie)
  #RICEZIONE DATI DI INPUT
  for riga,r in puntiluce.iterrows():
    while True:
      try:
        consumi['kWh'][riga] = (float(input("ANNO {0}\nInserire consumo per illuminazione pubblica [kWh] : ".format(str(riga)))))
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
  return consumi,puntiluce


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


def calcola_potenza_media(ripartizione_consumi,puntiluce):
  # CALCOLO POTENZA MEDIA
  potenza_media = pd.DataFrame(index=anni, columns=tecnologie)
  for riga,r in potenza_media.iterrows():
      for columns in potenza_media:
        if int(puntiluce[columns][riga]) > 0:
          potenza_media[columns][riga] = ripartizione_consumi[columns][riga] / ore_esercizio / 1000 / int(puntiluce[columns][riga]) * 1000000
        else: potenza_media[columns][riga] = 0
  return potenza_media


def calcola_riduzione_consumi(ripartizione_consumi):
  riduzione_consumi = (1-(ripartizione_consumi['TOT_no_led'][2019]/ripartizione_consumi['TOT_no_led'][20152016]))*100
  return round(riduzione_consumi,3)


def calcola_riduzione_50(puntiluce,anni,tecnologie,eta,consumi):
  puntiluce_2020 = copy.deepcopy(puntiluce)
  puntiluce_2020.drop(columns='TOT_no_led',inplace=True)

  for i in range(1,int(puntiluce['TOT_no_led'][2019])+1): #possono essere sostituiti al massimo il numero di lampioni non led presenti al 2019
    for columns in puntiluce_2020:
      if columns == 'LED': break
      for j in range(1,int(puntiluce[columns][2019])+1): #per ogni tecnologia posso sostituire al massimo in numero di lampioni presenti al 2019
        #puntiluce_2020[columns][2019] = puntiluce[columns][2019] - j
        puntiluce_2020[columns][2019] -= 1
        #puntiluce_2020['LED'][2019] = puntiluce['LED'][2019] + j
        puntiluce_2020['LED'][2019] += 1
        Pesi_ = calcola_pesi(anni,tecnologie,eta,puntiluce_2020)
        ripartizione_consumi_ = calcola_ripartizione_consumi_2020(tecnologie,Pesi_,consumi,puntiluce_2020,potenza_media)
        riduzione_consumi_ = calcola_riduzione_consumi(ripartizione_consumi_)
        if riduzione_consumi_ > 50: break
      if riduzione_consumi_ > 50: break
    if riduzione_consumi_ > 50: break
  return puntiluce_2020,ripartizione_consumi_,riduzione_consumi_

##########################                   MAIN                   ##########################

tecnologie = ['Incandescenza ','Mercurio alta pressione ', 'Ioduri e Alogenuri Metallici (MH) ','Sodio ad alta pressione (SAP) ','Sodio a bassa pressione (SBP) ','LED']
eta_ = [[3.90456,11.484,18.3744,21.8196,32.1552,53.8384]]
eta = pd.DataFrame(data=eta_,columns=tecnologie)
anni = [2015,2016,2019]
ore_esercizio = 4200

#1 - Ricezione dati di input
consumi,puntiluce = input_dati(anni,tecnologie)

#2 - Calcolo pesi
Pesi = calcola_pesi(anni,tecnologie,eta,puntiluce)

#3 - Calcolo ripartizione consumi
ripartizione_consumi = calcola_ripartizione_consumi(tecnologie,Pesi,consumi)

#4 - Calcolo potenza media
potenza_media = calcola_potenza_media(ripartizione_consumi,puntiluce)

#5 CALCOLO RIDUZIONE CONSUMI FRA MEDIA 205-2016 E 2019
riduzione_consumi = calcola_riduzione_consumi(ripartizione_consumi)

#6 - CALCOLO PUNTI LUCE DA SOSTITUIRE PER ARRIVARE A RISPARMIO = 50%
puntiluce['TOT_no_led'] = 0; puntiluce['TOT_no_led'] = puntiluce.sum(axis=1) - puntiluce['LED'] #aggiungo colonna con somma dei punti luce non led

puntiluce_2020,ripartizione_consumi_,riduzione_consumi_ = calcola_riduzione_50(puntiluce,anni,tecnologie,eta,consumi)

##########################                   CALCOLO PARAMETRI DELLO SCENARIO                   ##########################
#CALCOLO INVESTIMENTI
costo_puntoluce = 700
investimento = costo_puntoluce * int(puntiluce_2020['LED'][2019] - puntiluce['LED'][2019])
#CALCOLO RISPARMIO ECONOMICO ANNUALE
costo_energia = 0.2
ripartizione_consumi['TOT'] = 0; ripartizione_consumi_['TOT'] = 0
ripartizione_consumi['TOT'] = ripartizione_consumi.sum(axis=1) - ripartizione_consumi['TOT_no_led']
ripartizione_consumi_['TOT'] = ripartizione_consumi_.sum(axis=1) - ripartizione_consumi_['TOT_no_led']

risparmioenergia = round(ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019])
risparmio_economico_annuo = round((ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019]) * costo_energia)
#CALCOLO TEE (TITOLI DI EFFICIENZA ENERGETICA)
tee = round(((ripartizione_consumi['TOT'][2019] - ripartizione_consumi_['TOT'][2019]) * 0.187 * 0.001) * 200 * 5)
# CALCOLO SPBT (SIMPLE PAYBACK TIME)
if investimento > tee:
  spbt = round((investimento - tee) / risparmio_economico_annuo,3)

##########################                   PRINT                   ##########################
print("\nRiduzione consumi fra media 2015-2016 e 2019: {0} %".format(riduzione_consumi))
print("Per arrivare ad un risparmio del 50% occorre sostituire:")
for columns in puntiluce_2020:
  if puntiluce_2020[columns][2019] < puntiluce[columns][2019]:
    print("{0} punti luce con tecnologia {1}".format(int((puntiluce[columns][2019]-puntiluce_2020[columns][2019])),columns))
print("\nRisparmio energetico: {0} %".format(riduzione_consumi_))
print("Investimento necessario: {0} €".format(investimento))
print("Risparmio energetico: {0} kWh".format(risparmioenergia))
print("Risparmio economico annuo: {0} €".format(risparmio_economico_annuo))
print("TEE: {0} €".format(tee))
print("Simple Pay Back Time: {0} anni".format(spbt))