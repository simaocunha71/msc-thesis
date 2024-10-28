
def sum_even_and_even_index(lst):
  return sum(num for index, num in enumerate(lst) if index % 2 == 0 and num % 2 == 0)


