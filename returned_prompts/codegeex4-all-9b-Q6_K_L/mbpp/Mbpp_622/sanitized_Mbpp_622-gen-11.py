def get_median(list1: list, list2: list, n: int) -> float:
  merged_list = sorted(list1 + list2)
  return merged_list[n // 2] if n % 2 != 0 else (merged_list[n // 2 - 1] + merged_list[n // 2]) / 2