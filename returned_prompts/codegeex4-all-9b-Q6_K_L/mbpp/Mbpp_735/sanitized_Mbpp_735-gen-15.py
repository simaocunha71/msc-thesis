def toggle_middle_bits(n):
  binary_num = bin(n)[2:]
  toggled_num = binary_num[0] + ''.join('1' if x == '0' else '0' for x in binary_num[1:-1]) + binary_num[-1]
  return int(toggled_num, 2)