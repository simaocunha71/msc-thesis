def convert(complex_num):
  a, b = complex_num.real, complex_num.imag
  r = (a**2 + b**2)**0.5
  theta = math.atan2(b, a)
  return (r, theta)