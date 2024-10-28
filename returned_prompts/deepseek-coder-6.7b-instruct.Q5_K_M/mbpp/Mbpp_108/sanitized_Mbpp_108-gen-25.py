def merge_sorted_list(list1, list2, list3):
  result = []
  result.extend(list1)
  result.extend(list2)
  result.extend(list3)
  result.sort()
  return result