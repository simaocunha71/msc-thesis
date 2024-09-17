
def even_bit_set_number(n):
  binary_n = bin(n)[2:]
  binary_n = '0'+ binary_n[1:] if len(binary_n) % 2 else binary_t
  for i in range(0, len(binary_n), 2):
    binary_n = binary_n[:i] + '1' + binary_n[i+1:]
  return int(binary_n, 2)


