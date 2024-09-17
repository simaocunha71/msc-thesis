
def count_element_in_list(lst:list,ele:int) -> int:
  count = 0
  for i in lst:
    if ele in i:
      count += 1
  return count


