def count_element_in_list(lst, element):
  return sum(1 for sublist in lst if element in sublist)