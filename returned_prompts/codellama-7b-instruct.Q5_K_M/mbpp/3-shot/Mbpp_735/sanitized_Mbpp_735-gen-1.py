def toggle_middle_bits(n):
  return (n ^ 0xffffffff ^ (n >> 1) ^ (n >> 2)) & 0xffffffff