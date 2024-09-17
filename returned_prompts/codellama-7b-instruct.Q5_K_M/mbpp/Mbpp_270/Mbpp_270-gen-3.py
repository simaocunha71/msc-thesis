
def sum_even_and_even_index(my_list):
  sum = 0
  for i, x in enumerate(my_list):
    if i % 2 == 0 and x % 2 == 0:
      sum += x
  return sum


