
def get_median(test_list1: list, test_list2: list, k: int) -> float:
  list_sum = sum(test_list1[:k]) + sum(test_list2[:k])
  median = list_sum / 2.0
  return median


