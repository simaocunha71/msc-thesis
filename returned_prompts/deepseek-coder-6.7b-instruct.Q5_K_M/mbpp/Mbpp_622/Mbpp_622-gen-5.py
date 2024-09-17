
def get_median(list1: list, list2: list, size: int) -> float:
  merged_list = sorted(list1 + list2)
  if size % 2 != 0:
    return float(merged_list[size // 2])
  return (merged_list[(size - 1) // 2] + merged_list[size // 2]) / 2.0


