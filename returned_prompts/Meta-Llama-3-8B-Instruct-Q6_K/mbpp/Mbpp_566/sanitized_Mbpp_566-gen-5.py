def sum_digits(n):
  return sum(int(i) for i in str(n))  # convert the number to a string, then sum up the digits