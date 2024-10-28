def even_bit_set_number(n):
  bin_n = bin(n)[2:]
  even_bit_set = ''.join(["1" if i%2 == 0 else bit for i, bit in enumerate(bin_n)])
  return int(even_bit_set, 2)