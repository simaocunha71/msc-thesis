def toggle_middle_bits(n):
  bin_str = bin(n)[2:]
  bin_str = '1' + '0' * (len(bin_str) - 2) + '1'
  return int(bin_str, 2) if bin_str else 0