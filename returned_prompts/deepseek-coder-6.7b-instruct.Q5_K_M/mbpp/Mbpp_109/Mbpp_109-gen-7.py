
def odd_Equivalent(binary_string:str, rotations:int)->int:
  binary_string *= rotations
  count = 0
  for i in range(rotations):
    rotated_binary = binary_string[i:] + binary_string[:i]
    for j in range(0, len(rotated_binary), 2):
      if int(rotated_binary[j:j+2], 2) % 2 != 0:
        count += 1
  return count


