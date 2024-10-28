
def toggle_middle_bits(n: int) -> int:
  n = (n >> 1) + (n & 1)
  return (n << 1) + 1


