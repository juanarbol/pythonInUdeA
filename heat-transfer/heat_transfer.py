#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from graph import graph
from numpy import ones
from numpy import allclose
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
matrix_x_axis = input('Digite el tamaño de la placa con respecto al eje x (en metros): ') # Size of board in x axis
matrix_x_axis = int(matrix_x_axis)*10 # we've to multiply by 10 cuz' we're diviving it in dm's not metters

matrix_y_axis = input('Digite el tamaño de la placa con respecto al eje y (en metros): ') # Size of board in y axis
matrix_y_axis = int(matrix_y_axis)*10 # we've to multiply by 10 cuz' we're diviving it in dm's not metters

thickness_input = int(input('Digite el espesor de la placa: '))
thickness = thickness_input if thickness_input > 0 else 1

font_temperature_input = int(input('Digite la temperatura de la fuente (Cº): '))
font_temperature = font_temperature_input if font_temperature_input > 30 else 35

font_x_position_input = int(input('Digite la posición de la fuente (x cm\'s): '))
font_x_position = font_x_position_input//10 if font_x_position_input < matrix_x_axis else int(matrix_x_axis/2)

font_y_position_input = int(input('Digite la posición de la fuente (y cm\'s): '))
font_y_position = font_y_position_input//10 if font_y_position_input < matrix_y_axis else int(matrix_y_axis/2)

###### constants
dT = 1e5 # dT (changes of temperatura)
k = 205 # K constant
c = 910 # C constant
rho = 2700 # rho constant
ambient_temperature = 30.0 # Ambient temperature
dl = 1 # size of cuadricula
A = thickness**2 # Area

constants = {
  "dT": 1e5, # dT (changes of temperatura)
  "dl": 1, 
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
temperature_matrix[font_x_position, font_y_position] = font_temperature # set the font location
expected_value = ones((matrix_x_axis,matrix_y_axis))*(font_temperature-0.1)

heat_transfer_plot = ax.imshow(temperature_matrix, cmap = plt.get_cmap("magma"))

## Loop conditionals
process_of_graph = False
completed = True
current_time = 0 # temperature counter
while process_of_graph is not completed:
  temperature_matrix = graph(heat_transfer_plot, temperature_matrix, constants, current_time)
  process_of_graph = allclose(temperature_matrix, expected_value, 1e-2) # this validates if process has ended with a relative tolerance of 1e-2
  current_time += dT # advance dT in current_temperature

# Pause the plot (30secs) when it is finished
plt.title("La animación ha terminado.")
plt.pause(30)