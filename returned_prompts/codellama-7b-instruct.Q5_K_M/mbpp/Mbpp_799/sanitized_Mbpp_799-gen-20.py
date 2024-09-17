def left_rotate(n: int,d: int) -> int:
  mask = (1 << 32) - 1
  return (n << d) & mask | (n >> (32 - d)) & mask