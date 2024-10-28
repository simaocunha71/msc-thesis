def left_rotate(x: int,d: int) -> int:
  return (x << d) | (x >> (32-d))