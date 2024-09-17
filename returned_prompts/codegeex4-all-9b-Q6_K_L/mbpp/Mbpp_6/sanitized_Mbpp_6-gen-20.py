def differ_At_One_Bit_Pos(n1,n2):
  return bin(n1^n2).count('1') == 1