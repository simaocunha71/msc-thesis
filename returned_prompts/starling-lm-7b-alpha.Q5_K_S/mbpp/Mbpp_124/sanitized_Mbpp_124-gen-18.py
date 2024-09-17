import math
def angle_complex(real: float, imag: float) -> float:
  angle = math.atan2(imag, real)
  return angle