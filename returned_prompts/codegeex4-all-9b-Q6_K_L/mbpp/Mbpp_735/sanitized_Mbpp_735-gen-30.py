def toggle_middle_bits(n):
  binary_str = bin(n)[2:]
  toggled_binary_str = ''.join(['1' if bit == '0' else '0' for bit in binary_str[1:-1]])
  toggled_num = int(toggled_binary_str, 2)
  return toggled_num