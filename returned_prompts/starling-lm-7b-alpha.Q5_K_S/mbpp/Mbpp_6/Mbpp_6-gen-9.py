
def differ_At_One_Bit_Pos(n1: int, n2: int) -> bool:
  n1_binary = bin(n1)
  n2_binary = bin(n2)
  if len(n1_binary) != len(n2_binary):
    return False
  for i in range(len(n1_binary)):
    if n1_binary[i] != n2_binary[i]:
      if i == 0:
        if n1_binary[i] == "0" and n2_binary[i] == "1":
          return True
      elif i == len(n1_binary)-1:
        if n1_binary[i] == "1" and n2_binary[i] == "0":
          return True
      else:
        if n1_binary[i] != n2_binary[i]:
          return True
  return False


