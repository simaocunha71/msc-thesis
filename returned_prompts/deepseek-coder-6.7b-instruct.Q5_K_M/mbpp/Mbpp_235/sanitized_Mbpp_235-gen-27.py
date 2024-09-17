def even_bit_set_number(n):
  binary_n = bin(n)[2:]
  even_set_binary = ''.join([binary_n[i]+'0' if i%2 == 0 else binary_n[i] for i in range(len(binary_n))])
  return int(even_set_binary, 2)