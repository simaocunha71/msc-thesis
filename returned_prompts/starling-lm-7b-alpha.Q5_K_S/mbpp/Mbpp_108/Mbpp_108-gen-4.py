
def merge_sorted_list(list_one: list, list_two: list, list_three: list) -> list:
  merged_list = []
  while list_one:
    merged_list.append(list_one.pop(0))
  while list_two:
    merged_list.append(list_two.pop(0))
  while list_three:
    merged_list.append(list_three.pop(0))
  return merged_list


