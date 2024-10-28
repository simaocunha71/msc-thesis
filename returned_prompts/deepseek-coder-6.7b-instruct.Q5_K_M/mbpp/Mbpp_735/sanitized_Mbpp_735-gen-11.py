def toggle_middle_bits(n):
  binary = bin(n)[2:]
  middle_bits = list(binary[1:-1])
  for i in range(len(middle_bits)):
    middle_bits[i] = '0' if middle_bits[i] == '1' else '1'
  toggled_binary = binary[0] + ''.join(middle_bits) + binary[-1]
  return int(toggled_binary, 2)