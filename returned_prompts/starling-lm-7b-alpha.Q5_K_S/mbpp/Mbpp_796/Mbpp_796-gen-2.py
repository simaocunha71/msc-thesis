
def return_sum(dictionary: dict) -> int:
  sum_of_items = 0
  for key in dictionary:
    sum_of_items += dictionary[key]
  return sum_of_items


