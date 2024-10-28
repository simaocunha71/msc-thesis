
def get_median(list_1: list, list_2: list, size: int) -> float:
  median = 0.0
  for i in range(0, size):
      median = (list_1[i] + list_2[i]) / 2
  return median


