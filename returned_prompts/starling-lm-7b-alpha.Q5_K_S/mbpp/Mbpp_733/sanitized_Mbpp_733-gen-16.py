def find_first_occurrence(sorted_arr:list, num:int) -> int:
  if num not in sorted_arr:
    return -1
  else:
    return sorted_arr.index(num)