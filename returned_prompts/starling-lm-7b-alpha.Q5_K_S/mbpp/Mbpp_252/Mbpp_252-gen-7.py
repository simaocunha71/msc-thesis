
import cmath
def convert(num: complex) -> tuple:
  return (cmath.polar(num)[0], cmath.polar(num)[1])


