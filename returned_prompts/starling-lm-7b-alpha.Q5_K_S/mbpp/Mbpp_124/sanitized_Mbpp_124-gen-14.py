import math
def angle_complex(real_part,imag_part):
  angle = math.atan(imag_part / real_part)
  if real_part < 0:
    angle += math.pi
  if imag_part < 0:
    angle += 2 * math.pi
  return angle