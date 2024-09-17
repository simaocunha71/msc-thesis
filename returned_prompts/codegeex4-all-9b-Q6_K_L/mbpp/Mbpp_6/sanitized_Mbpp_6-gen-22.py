def differ_At_One_Bit_Pos(num1: int, num2: int) -> bool:
  xor = num1 ^ num2
  return xor & (xor - 1) == 0