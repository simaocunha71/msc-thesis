def find_length(s):
  max_diff = 0
  count_zero = 0
  count_one = 0
  for i in range(len(s)):
    if s[i] == '0':
      count_zero += 1
    else:
      count_one += 1
    if count_zero != 0 and count_one != 0:
      max_diff = max(max_diff, abs(count_zero - count_one))
    elif count_one == 0 or count_zero == 0:
      count_zero = 0
      count_one = 0
  return max_diff