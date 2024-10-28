def count_list(lst: list) -> int:
  count = 0
  for i in lst:
    if isinstance(i, list):
      count += 1
  return count