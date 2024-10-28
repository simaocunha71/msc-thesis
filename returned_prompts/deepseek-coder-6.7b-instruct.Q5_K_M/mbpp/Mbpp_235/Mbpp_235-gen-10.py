
def even_bit_set_number(n):
  bin_num = bin(n)[2:]
  new_bin = ''
  for i in range(len(bin_num)):
    if i % 2 == 0:
      new_bin += '1'
    else:
      new_bin += bin_num[i]
  return int(new_bin, 2)


