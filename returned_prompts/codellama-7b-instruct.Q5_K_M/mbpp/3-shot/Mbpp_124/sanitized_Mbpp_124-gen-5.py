import math
def angle_complex(a: complex) -> float:
  return math.degrees(math.atan(a.imag/a.real))