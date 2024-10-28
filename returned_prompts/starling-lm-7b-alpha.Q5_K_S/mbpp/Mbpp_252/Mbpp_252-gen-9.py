
import cmath
def convert(num):
  mod = cmath.polar(num)[0]
  angle = cmath.polar(num)[1]*180/math.pi
  return (mod, angle)


