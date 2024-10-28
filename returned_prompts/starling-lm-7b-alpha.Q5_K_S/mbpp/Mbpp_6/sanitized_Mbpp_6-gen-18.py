def differ_At_One_Bit_Pos(num1: int, num2: int) -> bool:
  diff = num1 ^ num2
  while diff:
    if diff & 0b00000001:
      return True
    diff >>= 1
  return False