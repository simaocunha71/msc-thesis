
def count_integer(input_list):
  integer_count = 0
  for i in input_list:
    if isinstance(i, int):
      integer_count += 1
  return integer_count


