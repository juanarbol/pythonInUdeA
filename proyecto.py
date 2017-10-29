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

Q = k*A*DT*(dT/dl)
Q = (T2-T1)*(dT/R)
k = 205 [W/m.K]
Lambda = 237 aluminio
c = 910 [J/kg.K] (calor especifico)
Q = mc(T2-T1)

"""

plt.close() # kill the previous plot
fig, ax = plt.subplots() # plot declaration?

###### constants
dT = 1e5 # dT (changes of temperatura)
final_temperature = 20e7 # temperature limit (the animation finish when current_temperature = final_temperature)
k = 205 # K constant
c = 910 # C constant
rho = 2700 # rho constant
ambient_temperature = 30.0 # Ambient temperature

###### Prompt values
font_temperature = 100 # Font temperature
matrix_x_axis = 10 # Size of board in x axis
matrix_y_axis = 10 # Size of board in y axis

dl = 1 # ????
thickness = 1 # thickness
A = thickness**2 # Area

temperature_matrix = np.ones((matrix_x_axis,matrix_y_axis))*(ambient_temperature) # Fill the matrix with 1*(ambient_temperature)
temperature_matrix[9,5] = font_temperature # Set the font position ?? [x,y]

updated_temperature_matrix = temperature_matrix.copy()
heat_transfer_plot = ax.imshow(temperature_matrix, cmap = plt.get_cmap("magma"))

m = (rho*matrix_x_axis*matrix_y_axis*thickness)
current_temperature = 0 # temperature counter
while current_temperature < final_temperature:
  for i in range(matrix_x_axis):
    for j in range(matrix_y_axis):
      ti = temperature_matrix[i,j]
      Q=[]
      if i+1 <= (matrix_x_axis-1):
        Q.append(k*A*(temperature_matrix[i+1,j] - ti)*(dT/dl))
      if i-1 >= 0:
        Q.append(k*A*(temperature_matrix[i-1,j] - ti)*(dT/dl))
      if j+1 <= (matrix_y_axis-1):
        Q.append(k*A*(temperature_matrix[i,j+1] - ti)*(dT/dl))
      if j-1 >= 0:
        Q.append(k*A*(temperature_matrix[i,j-1]-ti)*dT/dl)
      Qt = sum(Q)
      tem = ti+Qt/(m*c)
      if tem <= font_temperature:
        updated_temperature_matrix[i,j] = tem
      else:
        updated_temperature_matrix[i,j] = font_temperature
    temperature_matrix = updated_temperature_matrix.copy()
    temperature_matrix[0,5] = font_temperature
    heat_transfer_plot.set_data(temperature_matrix)
    plt.title(current_temperature)
    plt.pause(0.07)
    current_temperature =+ dT # advance dT in current_temperature
