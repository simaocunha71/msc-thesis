def merge_sorted_list(list1: list,list2: list,list3: list) -> list:
  merged_list = list1 + list2 + list3
  merged_list.sort()
  return merged_list