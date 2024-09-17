
import cmath
def convert(n: complex):
  r = abs(n)
  theta = cmath.phase(n)
  return (r, theta)


