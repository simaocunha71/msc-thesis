
def count_element_in_list(arr: list,n: int) -> int:
  count = 0
  for i in arr:
    if n in i:
      count += 1
  return count


