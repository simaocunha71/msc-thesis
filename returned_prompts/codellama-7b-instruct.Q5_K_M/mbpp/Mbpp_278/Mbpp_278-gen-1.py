
def count_first_elements(my_tuple):
  count = 0
  for i in my_tuple:
    if type(i) == tuple:
      break
    count += 1
  return count


