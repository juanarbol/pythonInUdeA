#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from graph import graph
from numpy import ones
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

dl = 1 # size of cuadricula
thickness = 1 # thickness
A = thickness**2 # Area

constants = {
  "dT": 1e5, # dT (changes of temperatura)
  "dl": 1, 
  "final_temperature": 20e7, # temperature limit (the animation finish when current_temperature = final_temperature)
  "k": 205, # K constant
  "c": 910, # C constant
  "rho": 2700, # rho constant
  "ambient_temperature": 30.0, # Ambient temperature
  "font_temperature": font_temperature,
  "matrix_x_axis": matrix_x_axis,
  "matrix_y_axis": matrix_y_axis,
  "m": (rho*matrix_x_axis*matrix_y_axis*thickness),
  "A": A
}

temperature_matrix = ones((matrix_x_axis,matrix_y_axis))*(ambient_temperature) # Fill the matrix with 1*(ambient_temperature)
temperature_matrix[9,5] = font_temperature # Set the font position ?? [x,y]

heat_transfer_plot = ax.imshow(temperature_matrix, cmap = plt.get_cmap("magma"))
    
current_temperature = 0 # temperature counter
while current_temperature < final_temperature:
  temperature_matrix = graph(heat_transfer_plot, temperature_matrix, constants, current_temperature)
  current_temperature += dT # advance dT in current_temperature