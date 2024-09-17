def convert(num):
  real, imag = num.real, num.imag
  magnitude = (real ** 2 + imag ** 2) ** 0.5
  angle = (180 / math.pi) * math.atan2(imag, real)
  return (magnitude, angle)