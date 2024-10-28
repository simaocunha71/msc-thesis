
def differ_At_One_Bit_Pos(num1: int,num2: int) -> bool:
  return bin(num1 ^ num2).count('1') == 1


