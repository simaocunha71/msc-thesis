def odd_Equivalent(binary_string: str, rotate: int) -> int:
  binary_string = binary_string * rotate
  binary_list = list(binary_string)
  odd_count = 0
  for i in range(len(binary_list)):
    if int(binary_list[i])%2 == 1:
      odd_count += 1
  return odd_count