def left_rotate(num: int, rotate: int) -> int:
  return (num << rotate) | (num >> (32 - rotate))