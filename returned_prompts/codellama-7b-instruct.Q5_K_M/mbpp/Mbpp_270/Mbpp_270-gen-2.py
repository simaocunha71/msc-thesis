
def sum_even_and_even_index(my_list):
  sum_even_index = 0
  sum_even_positions = 0
  for index, value in enumerate(my_list):
    if index % 2 == 0:
      sum_even_index += value
    if value % 2 == 0:
      sum_even_positions += value
  return sum_even_index, sum_even_positions


