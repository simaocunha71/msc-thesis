import math
def triangle_area(radius):
  if radius < 0:
    return None
  else:
    return (radius * radius * math.sqrt(3)) / 2

