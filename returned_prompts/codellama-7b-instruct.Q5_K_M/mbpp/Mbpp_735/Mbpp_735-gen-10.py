
def toggle_middle_bits(n):
  return bin(n)[:2] + bin(n)[3:-2] + bin(n)[-1]


