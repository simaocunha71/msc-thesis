def sum_even_and_even_index(lst):
  return sum(n for i, n in enumerate(lst) if i % 2 == 0 and n % 2 == 0)