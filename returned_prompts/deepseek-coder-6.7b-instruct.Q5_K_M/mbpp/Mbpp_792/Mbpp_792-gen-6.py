
def count_list(num_list):
  count = 0
  for i in num_list:
    if isinstance(i, list):
      count += 1
  return count


