
def even_bit_set_number(n):
  binary_n = bin(n)[2:]
  even_bit_set_binary = ''.join(['1' if i % 2 == 0 else bit for i, bit in enumerate(binary_n)])
  return int(even_bit_set_binary, 2)


