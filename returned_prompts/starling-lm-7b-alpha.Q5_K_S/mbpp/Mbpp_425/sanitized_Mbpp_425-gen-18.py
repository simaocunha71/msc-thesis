def count_element_in_list(sub_lists: list, target: object) -> int:
  count = 0
  for sub_list in sub_lists:
    if target in sub_list:
      count += 1
  return count