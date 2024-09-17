
def toggle_middle_bits(n: int) -> int:
  return n ^ (n >> 1) ^ (n >> 20)


