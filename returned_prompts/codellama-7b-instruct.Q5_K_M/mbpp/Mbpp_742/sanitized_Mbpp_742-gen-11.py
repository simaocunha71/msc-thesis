from math import sqrt
def area_tetrahedron(side_length: float) -> float:
  area = (3 * sqrt(2)) / 2 * pow(side_length, 2)
  return area