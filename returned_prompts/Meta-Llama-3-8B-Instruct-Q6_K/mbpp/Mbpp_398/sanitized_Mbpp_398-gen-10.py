def sum_of_digits(lst):
  return sum(sum(map(int, str(i))) for i in lst)