def toggle_middle_bits(n: int):
  return (n | (n >> 1)) + ((n & (~(n >> 1))) >> 1)