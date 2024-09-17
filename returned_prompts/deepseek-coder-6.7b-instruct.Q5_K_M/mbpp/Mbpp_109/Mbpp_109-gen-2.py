
def odd_Equivalent(binary_string: str, rotations: int) -> int:
  binary_string = binary_string * rotations
  count = 0
  for i in range(rotations):
    rotated_binary = binary_string[i:len(binary_string)] + binary_string[0:i]
    count += sum(int(x) % 2 for x in rotated_binary)
  return count


