def sum_of_digits(lst):
  return sum(map(lambda x: sum(map(int, str(x))), lst))