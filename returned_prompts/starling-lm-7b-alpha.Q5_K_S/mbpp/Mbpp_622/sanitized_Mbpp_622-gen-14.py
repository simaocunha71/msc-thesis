def get_median(list_one: list, list_two: list, size: int) -> float:
  combined_list = list_one + list_two
  combined_list.sort()
  median = len(combined_list) // 2
  if median % 2 == 0:
    return (combined_list[median - 1] + combined_list[median]) / 2
  else:
    return combined_list[median]