
def find_length(binary_string):
  count_zero = 0
  count_one = 0
  max_diff = 0

  for char in binary_string:
    if char == '0':
      count_zero += 1
    else:
      count_one += 1

    if count_zero > count_one:
      max_diff = max(max_diff, count_zero - count_one)
    else:
      max_diff = max(max_diff, count_one - count_zero)

  return max_diff


