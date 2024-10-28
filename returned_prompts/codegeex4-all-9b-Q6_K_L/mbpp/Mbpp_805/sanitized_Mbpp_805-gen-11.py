def max_sum_list(lists: list) -> list:
  max_sum = max([sum(lst) for lst in lists])
  max_sum_index = [i for i, lst in enumerate(lists) if sum(lst) == max_sum]
  return lists[max_sum_index[0]]