
def toggle_middle_bits(n: int):
  first_bit = n & 1
  last_bit = (n >> 31) & 1
  middle_bits = (n >> 1) | (n >> 32)
  return (first_bit << 31) | (last_bit << 1) | middle_bits


