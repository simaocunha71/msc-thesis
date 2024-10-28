def left_rotate(num: int,d: int) -> int:
  return (num << d) | (num >> (32 - d))