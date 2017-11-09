#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import ones
from numpy import array
from numpy import reshape
from itertools import product
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

temperature_matrix = ones((matrix_x_axis,matrix_y_axis))*(ambient_temperature) # Fill the matrix with 1*(ambient_temperature)
temperature_matrix[9,5] = font_temperature # Set the font position ?? [x,y]

heat_transfer_plot = ax.imshow(temperature_matrix, cmap = plt.get_cmap("magma"))

def heat_transfer_loop(temperature_matrix):
  product_cartesian = product(range(matrix_x_axis), range(matrix_y_axis))

  updated_temperature_matrix = [heat_transfer(matrix_coor) for matrix_coor in product_cartesian]
  updated_temperature_matrix = array(updated_temperature_matrix)
  updated_temperature_matrix_values = updated_temperature_matrix[0]

  return updated_temperature_matrix_values
  
    
m = (rho*matrix_x_axis*matrix_y_axis*thickness)
def heat_transfer(matrix_coor):
  matrix_coor = array(matrix_coor)
  position_x = matrix_coor[0]
  position_y = matrix_coor[1]

  ti = temperature_matrix[position_x,position_y]
  Q = []

  if position_x+1 <= (matrix_x_axis-1):
    Q.append(k*A*(temperature_matrix[position_x+1,position_y] - ti)*(dT/dl))

  if position_x-1 >= 0:
    Q.append(k*A*(temperature_matrix[position_x-1,position_y] - ti)*(dT/dl))

  if position_y+1 <= (matrix_y_axis-1):
    Q.append(k*A*(temperature_matrix[position_x,position_y+1] - ti)*(dT/dl))

  if position_y-1 >= 0:
    Q.append(k*A*(temperature_matrix[position_x,position_y-1]-ti)*dT/dl)
    
  Qt = sum(Q)
  tem = ti+Qt/(m*c)

  if tem <= font_temperature:
    temperature_matrix[position_x, position_y] = tem
  else:
    temperature_matrix[position_x, position_y] = font_temperature

  return temperature_matrix

def graph(temperature_matrix):
  new_temperature_matrix = heat_transfer_loop(temperature_matrix).copy()
  new_temperature_matrix[9,5] = font_temperature # Set the font position ?? [x,y]
  heat_transfer_plot.set_data(new_temperature_matrix)
  plt.title(int(current_temperature))
  plt.pause(0.0007)

  return new_temperature_matrix

current_temperature = 0 # temperature counter
while current_temperature < final_temperature:
  temperature_matrix = graph(temperature_matrix)
  current_temperature += dT # advance dT in current_temperature