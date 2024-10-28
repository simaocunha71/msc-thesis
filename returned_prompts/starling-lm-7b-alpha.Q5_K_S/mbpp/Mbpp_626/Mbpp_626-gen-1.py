
from math import pi
def triangle_area(r: float) -> float:
  if r < 0:
    return None
  else:
    return (2/3) * r * r * pi


