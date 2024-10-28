import cmath
def convert(complex_number):
  magnitude = abs(complex_number)
  angle = cmath.phase(complex_number)
  return (magnitude, angle)  # return magnitude and angle in radians
  #return (magnitude, angle * 180 / cmath.pi)  # return magnitude and angle in degrees if needed