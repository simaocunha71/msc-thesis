def odd_Equivalent(binary: str, rotate: int) -> int:
  binary = binary * rotate
  count = 0
  for i in range(rotate):
    rotated_binary = binary[i:] + binary[:i]
    if int(rotated_binary, 2) % 2 != 0:
      count += 1
  return count