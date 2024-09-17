def sum_even_and_even_index(my_list):
  sum = 0
  for index, element in enumerate(my_list):
    if index % 2 == 0 and element % 2 == 0:
      sum += element
  return sum