def toggle_middle_bits(n):
  mask = 0b1111111111111110
  return (n & mask) ^ mask