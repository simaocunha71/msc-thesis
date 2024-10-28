
def toggle_middle_bits(n):
  binary_n = bin(n)[2:]
  middle_bits = list(binary_n[1:-1])
  for i in range(len(middle_bits)):
    if middle_bits[i] == '1':
      middle_bits[i] = '0'
    else:
      middle_bits[i] = '1'
  middle_bits_str = ''.join(middle_bits)
  new_n_bin = binary_n[0] + middle_bits_str + binary_n[-1]
  new_n = int(new_n_bin, 2)
  return new_n


