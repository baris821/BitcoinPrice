from numpy import exp,array,random,dot,mean,abs

import numpy as np

girdi = array([[0,0,1],[1,1,1],[1,0,1]])
gercekSonuc = array([[0,1,1]]).T

agirlik = array([[1.0,1.0,1.0]]).T

for tekrar in range(100):
    #print(dot(girdi,agirlik))
    tahmin = 1 / (1+exp(-(dot(girdi,agirlik))))
    #print(tahmin)
    agirlik += dot(girdi.T , ((gercekSonuc - tahmin)*tahmin*(1-tahmin)))
    #print(agirlik)
    #print(tekrar , str(mean(abs(gercekSonuc-tahmin))))

#print(1/(1+exp(-(dot(array([1,0,0]),agirlik)))))
