from heat_transfer_loop import heat_transfer_loop
import matplotlib.pyplot as plt

def graph(heat_transfer_plot, temperature_matrix, constants, current_temperature):
  font_temperature = constants['font_temperature']

  new_temperature_matrix = heat_transfer_loop(temperature_matrix, constants).copy()
  new_temperature_matrix[9,5] = font_temperature # Set the font position ?? [x,y]
  heat_transfer_plot.set_data(new_temperature_matrix)
  plt.title("%d Cº" %(current_temperature))
  plt.pause(0.0007)

  return new_temperature_matrix