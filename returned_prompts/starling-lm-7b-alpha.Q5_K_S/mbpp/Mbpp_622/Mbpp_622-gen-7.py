
def get_median(list1: list, list2: list, size: int) -> float:
  combined_list = list1 + list2
  combined_list.sort()
  return combined_list[size//2]


