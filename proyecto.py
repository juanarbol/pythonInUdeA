# -*- coding: utf-8 -*-
"""
Q=k*A*DT*dt/dl
Q=(T2-T1)*dt/R
k=205 W/m.K
Lambda=237 aluminio
c=910 J/kg.K calor especifico
Q=mc(T2-T1)
"""
import numpy as np
import matplotlib.pyplot as plt


t=0
dt=1e5
tf=20e7

TFuente=100
temp=30.0

tamx=10
tamy=10
dl=1
esp=1
A=esp**2

k=205
c=910
rho=2700
m=rho*tamx*tamy*esp

nx=tamx//dl
ny=tamy//dl

TS=np.ones((nx,ny))*temp
TF=np.full((nx,ny),False)
#TF[5,5]=True
#TF[0,0]=True
TS[0,5]=TFuente
#TS[9,5]=TFuente
TFin=TS.copy()
plt.close()
fig, ax = plt.subplots()
pl1=ax.imshow(TS,cmap=plt.get_cmap("magma"))
while t<tf:
    for i in range(nx):
       # Q=[]
        for j in range(ny):
            ti=TS[i,j]
            Q=[]
            if i+1<=(nx-1):
                Q.append(k*A*(TS[i+1,j]-ti)*dt/dl)
            if i-1>=0:
                Q.append(k*A*(TS[i-1,j]-ti)*dt/dl)
            if j+1<=(ny-1):
                Q.append(k*A*(TS[i,j+1]-ti)*dt/dl)
            if j-1>=0:
                Q.append(k*A*(TS[i,j-1]-ti)*dt/dl)
            #print(Q)    
            Qt=sum(Q)
            tem=ti+Qt/(m*c)
            if tem<=TFuente:
                TFin[i,j]=tem
            else:
                TFin[i,j]=TFuente
    TS=TFin.copy()
    TS[0,5]=TFuente
   # TS[9,5]=TFuente
    pl1.set_data(TS)
    plt.title(t)
    plt.pause(0.07)
    t=t+dt
#pl1=ax.imshow(TS)    
#print(TS)
