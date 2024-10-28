def differ_At_One_Bit_Pos(x:int,y:int) -> bool:
  x_bin = bin(x)[2:]
  y_bin = bin(y)[2:]
  if len(x_bin) > len(y_bin):
    x_bin = "0" * (len(y_bin) - len(x_bin)) + x_bin
  else:
    y_bin = "0" * (len(x_bin) - len(y_bin)) + y_bin
  return x_bin != y_bin