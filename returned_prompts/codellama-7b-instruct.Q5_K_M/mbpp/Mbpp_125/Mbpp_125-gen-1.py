
def find_length(binary_str: str) -> int:
  count_zero = 0
  count_one = 0
  max_length = 0
  for i in binary_str:
    if i == '0':
      count_zero += 1
    elif i == '1':
      count_one += 1
    else:
      continue
    if count_zero > count_one:
      max_length = max(max_length, count_zero - count_one)
    else:
      max_length = max(max_length, count_one - count_zero)
    count_zero = 0
    count_one = 0
  return max_length


