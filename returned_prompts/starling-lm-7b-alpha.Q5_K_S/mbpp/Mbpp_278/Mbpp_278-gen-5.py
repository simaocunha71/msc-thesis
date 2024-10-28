
def count_first_elements(tup_list: list) -> int:
  count = 0
  for elem in tup_list:
    if isinstance(elem, tuple):
      count += len(elem)
    else:
      count += 1
  return count


