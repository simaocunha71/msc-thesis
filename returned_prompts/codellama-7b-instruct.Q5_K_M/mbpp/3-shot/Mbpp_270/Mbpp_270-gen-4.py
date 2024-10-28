
def sum_even_and_even_index(my_list):
  even_nums = [num for ind, num in enumerate(my_list) if ind % 2 == 0 and num % 2 == 0]
  return sum(even_nums)


