def sum_even_and_even_index(my_list: list) -> int:
  sum_even_indices = 0
  sum_even_numbers = 0
  for index, number in enumerate(my_list):
    if index % 2 == 0:
      sum_even_indices += number
    if number % 2 == 0:
      sum_even_numbers += number
  return sum_even_indices + sum_even_numbers