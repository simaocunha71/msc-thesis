
def get_median(list1, list2, size):
  list_sum = 0
  for i in range(size):
    list_sum += list1[i] + list2[i]
  median = list_sum / (2 * size)
  return median


