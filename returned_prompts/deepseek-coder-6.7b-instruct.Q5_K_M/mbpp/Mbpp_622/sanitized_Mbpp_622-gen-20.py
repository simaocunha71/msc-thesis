def get_median(list1: list, list2: list, n: int) -> float:
  merged_list = sorted(list1 + list2)
  if n % 2 == 0:
    median = (merged_list[n//2] + merged_list[n//2 - 1]) / 2
  else:
    median = merged_list[n//2]
  return median