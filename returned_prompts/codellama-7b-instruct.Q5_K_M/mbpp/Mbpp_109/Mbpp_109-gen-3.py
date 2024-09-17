
def odd_Equivalent(binary_string, n):
  rotated_binary_string = binary_string[-n:] + binary_string[:-n]
  return rotated_binary_string.count("1")


