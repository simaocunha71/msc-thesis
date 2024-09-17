
import cmath
def convert(num: complex) -> tuple:
  r = cmath.polar(num)
  return (r.real, r.imag)


