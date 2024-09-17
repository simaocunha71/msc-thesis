
def max_sum_list(list_of_lists: list) -> list:
  max_sum = -float('inf')
  result = []
  for l in list_of_lists:
    if sum(l) > max_sum:
      max_sum = sum(l)
      result = l
  return result


