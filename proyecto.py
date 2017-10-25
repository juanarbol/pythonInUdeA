#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

"""

In this algorithm we want to explain how to heat
is transfer through a board

"""

"""
Ecuations used, listed bellow:

Q = k*A*DT*(dt/dl)
Q = (T2-T1)*(dt/R)
k = 205 [W/m.K]
Lambda = 237 aluminio
c = 910 [J/kg.K] (calor especifico)
Q = mc(T2-T1)

"""

t = 0
dt = 1e5
tf = 20e7

TFuente = 100 # Font temperature
temp = 30.0 # Ambient temperature

tamx = 10 # Size of board in x axis
tamy = 10 # Size of board in y axis
dl = 1
esp = 1 # thickness
A = esp**2 # Area

k = 205 # K constant
c = 910 # C constant
rho = 2700 # rho constant

m = (rho*tamx*tamy*esp)

TS = np.ones((tamx,tamy))*(temp)
TF = np.full((tamx,tamy),False)

TS[9,5] = TFuente

TFin = TS.copy()
plt.close()
fig, ax = plt.subplots()
pl1 = ax.imshow(TS, cmap = plt.get_cmap("magma"))
while t < tf:
  for i in range(tamx):
    for j in range(tamy):
      ti = TS[i,j]
      Q=[]
      if i+1 <= (tamx-1):
        Q.append(k*A*(TS[i+1,j] - ti)*(dt/dl))
      if i-1 >= 0:
        Q.append(k*A*(TS[i-1,j] - ti)*(dt/dl))
      if j+1 <= (tamy-1):
        Q.append(k*A*(TS[i,j+1] - ti)*(dt/dl))
      if j-1 >= 0:
        Q.append(k*A*(TS[i,j-1]-ti)*dt/dl)
      Qt = sum(Q)
      tem = ti+Qt/(m*c)
      if tem <= TFuente:
          TFin[i,j] = tem
      else:
          TFin[i,j] = TFuente
    TS = TFin.copy()
    TS[0,5] = TFuente
   # TS[9,5] = TFuente
    pl1.set_data(TS)
    plt.title(t)
    plt.pause(0.07)
    t =+ dt
#pl1=ax.imshow(TS)    
#print(TS)
