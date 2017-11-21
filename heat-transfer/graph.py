from heat_transfer_loop import heat_transfer_loop
import matplotlib.pyplot as plt

def graph(heat_transfer_plot, temperature_matrix, constants, current_time):
  font_temperature = constants['font_temperature']
  font_x_position = constants["font_x_position"]
  font_y_position = constants["font_y_position"]

  new_temperature_matrix = heat_transfer_loop(temperature_matrix, constants).copy()
  new_temperature_matrix[font_x_position, font_y_position] = font_temperature # Set the font position ?? [x,y]
  heat_transfer_plot.set_data(new_temperature_matrix)
  plt.title("dT: %d" %(current_time))
  plt.pause(0.0007)

  return new_temperature_matrix