
def sum_even_and_even_index(lst):
  return sum(val for idx, val in enumerate(lst) if idx % 2 == 0 and val % 2 == 0)


