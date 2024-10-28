import cmath
def angle_complex(real: float, imag: float) -> float:
  angle = cmath.phase(complex(real, imag))
  return angle