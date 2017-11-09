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

fig, ax = plt.subplots() # plot declaration

###### Prompt values
matrix_x_axis = input('Digite el tamaño de la placa con respecto al eje x: ') # Size of board in x axis
matrix_x_axis = int(matrix_x_axis)

matrix_y_axis = input('Digite el tamaño de la placa con respecto al eje y: ') # Size of board in y axis
matrix_y_axis = int(matrix_y_axis)

font_temperature_input = int(input('Digite la temperatura de la fuente (Cº): '))
font_temperature = font_temperature_input if font_temperature_input > 30 else 35

font_x_position_input = int(input('Digite la posición de la fuente (x): '))
font_x_position = font_x_position_input if font_x_position_input < matrix_x_axis else int(matrix_x_axis/2)

font_y_position_input = int(input('Digite la posición de la fuente (y): '))
font_y_position = font_y_position_input if font_y_position_input < matrix_y_axis else int(matrix_y_axis/2)

###### constants
dT = 1e5 # dT (changes of temperatura)
final_temperature = 20e7 # temperature limit (the animation finish when current_temperature = final_temperature)
k = 205 # K constant
c = 910 # C constant
rho = 2700 # rho constant
ambient_temperature = 30.0 # Ambient temperature
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
  "A": A,
  "font_x_position": font_x_position,
  "font_y_position": font_y_position
}

temperature_matrix = ones((matrix_x_axis,matrix_y_axis))*(ambient_temperature) # Fill the matrix with 1*(ambient_temperature)
temperature_matrix[font_x_position, font_y_position] = font_temperature # Set the font position ?? [x,y]

heat_transfer_plot = ax.imshow(temperature_matrix, cmap = plt.get_cmap("magma"))
    
current_temperature = 0 # temperature counter
while current_temperature < final_temperature:
  temperature_matrix = graph(heat_transfer_plot, temperature_matrix, constants, current_temperature)
  current_temperature += dT # advance dT in current_temperature