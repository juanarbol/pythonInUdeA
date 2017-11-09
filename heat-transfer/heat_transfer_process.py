from numpy import array

def heat_transfer(matrix_coor, temperature_matrix, constants):
  matrix_coor = array(matrix_coor)
  position_x = matrix_coor[0]
  position_y = matrix_coor[1]

  font_temperature = constants['font_temperature']
  matrix_x_axis = constants['matrix_x_axis']
  matrix_y_axis = constants['matrix_y_axis']
  A = constants["A"]
  dT = constants["dT"]
  dl = constants["dl"]
  c = constants["c"]
  k = constants["k"]
  m = constants["m"]

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