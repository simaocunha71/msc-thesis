def sum_of_digits(lst):
  return sum(sum(int(d) for d in str(x)) for x in lst)