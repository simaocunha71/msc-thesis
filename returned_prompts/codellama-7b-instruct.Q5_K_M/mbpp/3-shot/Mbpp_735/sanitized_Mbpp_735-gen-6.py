def toggle_middle_bits(n: int) -> int:
  binary = bin(n)
  binary = binary[2:]
  binary = binary.replace('0', '2')
  binary = binary.replace('1', '0')
  binary = binary.replace('2', '1')
  return int(binary, 2)