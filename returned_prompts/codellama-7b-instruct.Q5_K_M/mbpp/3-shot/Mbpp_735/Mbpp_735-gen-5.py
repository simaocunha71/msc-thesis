
def toggle_middle_bits(n):
  first, last = n & 1, n & 128
  return last | (first ^ 1) | (n & 253)


