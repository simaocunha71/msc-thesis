def convert(c):
  r = (c.real**2 + c.imag**2)**0.5
  theta = math.atan2(c.imag, c.real)
  return (r, theta)