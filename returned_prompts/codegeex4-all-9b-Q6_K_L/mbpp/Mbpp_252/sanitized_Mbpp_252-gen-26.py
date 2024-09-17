def convert(n: complex):
  return (abs(n), math.atan2(n.imag, n.real))