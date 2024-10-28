
import cmath
def angle_complex(real: float, imag: float) -> float:
  return cmath.phase(complex(real, imag))


