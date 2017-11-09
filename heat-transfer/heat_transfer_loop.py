from heat_transfer_process import heat_transfer
from itertools import product
from numpy import array

def heat_transfer_loop(temperature_matrix, constants):
  matrix_x_axis = constants['matrix_x_axis']
  matrix_y_axis = constants['matrix_y_axis']

  product_cartesian = product(range(matrix_x_axis), range(matrix_y_axis))

  updated_temperature_matrix = [heat_transfer(matrix_coor, temperature_matrix, constants) for matrix_coor in product_cartesian]
  updated_temperature_matrix = array(updated_temperature_matrix)
  updated_temperature_matrix_values = updated_temperature_matrix[0]

  return updated_temperature_matrix_values