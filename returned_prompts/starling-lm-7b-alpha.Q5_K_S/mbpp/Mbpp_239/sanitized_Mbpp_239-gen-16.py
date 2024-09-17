def get_total_number_of_sequences(m, n):
  # Initialize result
  res = 0
  # Initialize current number
  curr = 1
  for i in range(n):
    # If current number is greater than m, return 0
    if curr > m:
      return 0
    # If current number is less than or equal to m, increment result and update current number
    res += 1
    curr = 2*curr
  return res