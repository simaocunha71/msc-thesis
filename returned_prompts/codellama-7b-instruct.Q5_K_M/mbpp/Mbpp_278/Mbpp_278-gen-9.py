
def count_first_elements(my_tuple):
  count = 0
  for item in my_tuple:
    if isinstance(item, tuple):
      break
    count += 1
  return count


