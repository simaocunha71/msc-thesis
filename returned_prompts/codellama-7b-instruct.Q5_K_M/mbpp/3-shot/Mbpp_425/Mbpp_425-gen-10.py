
def count_element_in_list(lst, elem):
  count = 0
  for sublist in lst:
    if elem in sublist:
      count += 1
  return count


