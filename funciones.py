#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import arange, array

def parabola(x0, xf, step):
  par = []
  for i in arange(x0, xf, step):
    par.append([i, i**2])
  return par

# print(parabola(1,10, 0.5))
# print(array(parabola(1,10, 0.5)))

"""
Función para calcular el área de un trapecio,
con número de argumentos definido
"""

B=2
b=1
h=3

def Area(B,b,h):
  return (B+b)*h/2
# print("Área de un trapecio ",Area(B,b,h))

"""
Función para calcular el perímetro de cualquier polígono
Lo que se busca, es usar la sintaxis de funciones sin número de parámetros definidos
"""

def perimeter(*sides):
  total = 0
  for i in sides:
    total += i
  return total
print("El perímetro de tu polígono es: %d" %(perimeter(1,2,3)))