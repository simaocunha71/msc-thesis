def left_rotate(num: int, d: int) -> int:
  return ((num << d) & 0xFFFFFFFF) | (num >> (32 - d))