def count_element_in_list(list_of_lists: list, element: int) -> int:
  count = 0
  for i in list_of_lists:
    if element in i:
      count += 1
  return count