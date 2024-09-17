def find_length(binary_str: str) -> int:
  count_zero = 0
  count_one = 0
  for char in binary_str:
    if char == "0":
      count_zero += 1
    else:
      count_one += 1
    if count_zero > count_one:
      count_one = count_zero
    elif count_one > count_zero:
      count_zero = count_one
  return max(count_zero, count_one)