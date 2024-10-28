def get_median(list1, list2, size):
  merged_list = sorted(list1 + list2)
  mid = size // 2
  if size % 2 == 0:
    return (merged_list[mid - 1] + merged_list[mid]) / 2
  else:
    return merged_list[mid]  # Return the middle element