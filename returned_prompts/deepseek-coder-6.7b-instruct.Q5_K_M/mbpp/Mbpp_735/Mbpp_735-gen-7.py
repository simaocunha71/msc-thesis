
def toggle_middle_bits(n):
  binary_n = bin(n)[2:]
  middle_bits = list(binary_n[1:-1])
  for i in range(len(middle_bits)):
    if middle_bits[i] == '1':
      middle_bits[i] = '0'
    else:
      middle_bits[i] = '1'
  binary_n = binary_n[0] + "".join(middle_bits) + binary_n[-1]
  return int(binary_n, 2)


