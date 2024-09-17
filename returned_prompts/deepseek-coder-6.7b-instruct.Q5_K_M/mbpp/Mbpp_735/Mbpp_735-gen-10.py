
def toggle_middle_bits(n):
  binary_n = bin(n)[2:]
  binary_n = '1' + binary_n[1:-1] + '1'
  return int(binary_n, 2)


