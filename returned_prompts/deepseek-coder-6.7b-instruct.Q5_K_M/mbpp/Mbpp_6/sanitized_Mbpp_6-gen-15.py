def differ_At_One_Bit_Pos(x,y):
  bin_x = bin(x)[2:]
  bin_y = bin(y)[2:]
  return abs(len(bin_x) - len(bin_y)) == 1 and bin_x.startswith(bin_y) or bin_y.startswith(bin_x)