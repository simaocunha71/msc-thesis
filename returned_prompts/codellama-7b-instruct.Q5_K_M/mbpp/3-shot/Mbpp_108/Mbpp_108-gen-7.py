
def merge_sorted_list(list1: list, list2: list, list3: list) -> list:
  list_of_lists = [list1, list2, list3]
  final_list = []
  while any(list_of_lists):
    current_min = min(x for x in list_of_lists if x)
    final_list.append(current_min.pop(0))
  return sorted(final_list)


