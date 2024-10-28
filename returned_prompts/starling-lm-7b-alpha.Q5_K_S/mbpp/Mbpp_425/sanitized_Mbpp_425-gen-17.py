def count_element_in_list(list_of_list, element):
  count = 0
  for i in list_of_list:
    if element in i:
      count += 1
  return count