#json parse etmek için kütüphane
import json
from numpy import exp,array,random,dot,mean,abs
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures


#okunacak dosya
with open('market-price.json') as data_file:
    data = json.load(data_file)

#Tüm fiyat değerlerini y listesine atama
y = []
for i in data["values"]:
    y.append(i["y"])

girdi = array([range(len(y))])

yMatris = array([y],float)
gercekSonuc = yMatris.T

agirlik = np.ones((len(y),1),dtype=np.float)



for tekrar in range(100):
    #print(dot(girdi,agirlik))
    tahmin = 1 / (1+exp(-(dot(girdi,agirlik))))
    print(dot(girdi,agirlik))
    agirlik += dot(girdi , ((gercekSonuc - tahmin)*tahmin*(1-tahmin)))
    #print(agirlik)
    #print(tekrar , str(mean(abs(gercekSonuc-tahmin))))
