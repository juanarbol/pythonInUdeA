from math import pi
from math import asin, sin, radians, degrees

def refractor(n1, n2, thetha):
  theta_radians = radians(thetha)
  operation = (n1/n2)*sin(theta_radians)
  return degrees(operation)


n1 = int(input("Digite el valor de n1: "))
n2 = int(input("Digite el valor de n2: "))
thetha = int(input("Digite el valor del ángulo thetha: ")) 

print("El valor de thetha2 es: %f" %(refractor(n1, n2, thetha)))
