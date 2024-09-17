from math import sqrt
from math import pow
def area_tetrahedron(side):
  a = pow(side, 2)
  b = pow(side, 2)
  c = pow(side, 2)
  s = (a + b + c) / 2
  area = sqrt(s * (s - a) * (s - b) * (s - c))
  return area