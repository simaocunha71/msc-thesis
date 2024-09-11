def sum_digits(n):
  return sum(int(i) for i in str(n))  # convert to string, iterate over each character, convert back to int, sum them up